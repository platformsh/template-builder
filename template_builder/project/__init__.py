import os
import os.path
from sys import stderr, stdout

from template_builder.helpers.color import color

import json
from glob import glob
from collections import OrderedDict
import time
import requests
import shlex
import shutil
import subprocess
from pathlib import Path

from requests.models import Response

UPDATER_BRANCH_NAME = "update"
UPDATER_SOURCEOP_NAME = "platform_update_dependencies"

class CliException(Exception):
    pass

class CliNoActivitiesException(CliException):
    pass

class CliEnvironmentNotExistException(CliException):
    pass

class BaseProject(object):
    '''
    Base class storing task actions.

    Each @property method corresponds to a DoIt task of the same name.
    In practice, platformify is usually the only one that most projects will need
    to override.
    '''

    # A dictionary of conditional commands to run for package updaters.
    # The key is a file name. If that file exists, then its value will be run in the
    # project build directory to update the corresponding lock file.
    updateCommands = {
        'composer.json': 'composer update',
        'Pipfile': 'pipenv lock',
        'Gemfile': 'bundle update',
        'package.json': 'npm update',
        'go.mod': 'go get -u all',
        'yarn.lock': 'yarn upgrade'
    }

    '''Amount of seconds to delay test execution after target_url is available.
    This is due to the fact that some apps take longer to really deploy than what is reported back to the status check.
    '''
    TEST_DELAY = 10

    def composer_defaults(self):
        """
        Composer needs to be told to ignore extensions when installing so that the person running
        this script doesn't have to have them all installed. If there are more composer dependencies
        to ignore for a new app, add them to the list here.
        """
        return [' --prefer-dist --no-interaction',
                '--ignore-platform-req=ext-redis',
                '--ignore-platform-req=ext-apcu',
                '--ignore-platform-req=ext-intl',
                '--ignore-platform-req=ext-bcmath',
                '--ignore-platform-req=ext-exif',
                '--ignore-platform-req=ext-gd',
                '--ignore-platform-req=ext-imagick',
                '--ignore-platform-req=ext-mbstring',
                '--ignore-platform-req=ext-memcache',
                '--ignore-platform-req=ext-pdo',
                '--ignore-platform-req=ext-openssl',
                '--ignore-platform-req=ext-zip',
                '--ignore-platform-req=php',
                ]

    def __init__(self, name, location="local"):
        self.name = name
        self.location = location


        self.repo = "platformsh-templates/{0}".format(self.name)
        self.use_integration = False

        # @todo move this to a separate method?
        if 'remote' == self.location:
            # @todo this makes me feel super icky
            self.templatedir = os.getcwd()
            if os.getenv('PLATFORMSH_CLI_TOKEN', None) == None:
                raise BaseException("env:PLATFORMSH_CLI_TOKEN not set, unable to continue")

            self.platform_path = self.get_platform_cli_path()

            # look for integration
            if self.platform_path:
                for integration in json.loads(subprocess.check_output([self.platform_path, "project:curl", "/integrations"]).decode("utf-8").strip()):
                    if integration.get("type") != "github":
                        continue
                    self.repo = integration["repository"]
                    print("integration found: {0}".format(integration['repository']))
                    self.use_integration = True
                    break

            self.builddir = os.getcwd()
            # Parses the github authorization token from env var by default.
            self.github_token = os.getenv('GITHUB_TOKEN', None)

            # A list containing function references which will be executed against a test url, bootstrapped with a basic smoke test.
            self.TEST_FUNCTIONS = [self.basic_smoke_test]
            self.test_results = {}

        else:
            self.rootdir = Path(__file__).parents[2]
            print("root dir is ")
            print(self.rootdir)
            #self.rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.templatedir = os.path.join(self.rootdir, 'templates')
            self.builddir = os.path.join(self.templatedir, self.name, 'build/')

        # Include default switches on all composer commands. This can be over-ridden per-template in a subclass.
        if 'composer.json' in self.updateCommands:
            self.build_update_commands()

    def get_platform_cli_path(self):
        if getattr(self, "platform_path", None):
            return self.platform_path

        if shutil.which("platform"):
            return "platform"
        elif os.path.exists("/app/.platformsh/bin/platform"):
            return "/app/.platformsh/bin/platform"
        else:
            self._install_platform_cli()
            return self.get_platform_cli_path() # recheck the path

    def install_cli(self):
        if self.platform_path is None:
            self._install_platform_cli()

    @property
    def cleanup(self):
        if 'remote' == self.location:
            if os.path.exists(self.builddir):
                shutil.rmtree(self.builddir)
        else:
            return ['rm -rf {0}'.format(self.builddir)]

    @property
    def init(self):
        if hasattr(self, 'github_name'):
            name = self.github_name
        else:
            name = self.name.replace('_', '-')

        if 'remote' == self.location:
            subprocess.call(["git", "clone", "git@github.com:platformsh-templates/{0}.git".format(name), self.builddir])
        else:
            return ['git clone git@github.com:platformsh-templates/{0}.git {1}'.format(
                name, self.builddir)
            ]

    @property
    def update(self):
        if 'remote' == self.location:
            self.package_update()
        else:
            actions = [
                'cd {0} && git checkout master && git pull --prune'.format(self.builddir)
            ]
            actions.extend(self.package_update_actions())
            return actions

    @property
    def platformify(self):
        """
        The default implementation of this method will
        1) Copy the contents of the files/ directory in the project over the
           application, replacing what's there.
        2) Apply any *.patch files found in the project directory, in alphabetical order.

        Individual projects may expand on these tasks as needed.
        """
        if 'remote' == self.location:
            print(os.path.join(self.templatedir, self.name, 'files/'))
            print(self.builddir)
            subprocess.call(["rsync", "-aP", os.path.join(self.templatedir, self.name, 'files/'), self.builddir])
        else:
            actions = ['rsync -aP {0} {1}'.format(
                os.path.join(self.templatedir, self.name, 'files/'), self.builddir
            )]

        patches = glob(os.path.join(self.templatedir, self.name, "*.patch"))
        for patch in patches:
            if 'remote' == self.location:
                with open(os.path.join(self.templatedir, self.name, 'files', patch), "r") as stream:
                    subprocess.call(["patch", "-p1"], cwd=self.builddir, stdin=stream)
            else:
                actions.append('cd {0} && patch -p1 < {1}'.format(
                    self.builddir, patch)
                )
        # In some cases the package updater needs to be run after we've platform-ified the
        # template, so run it a second time. Worst case it's a bit slower to build but doesn't
        # hurt anything.
        if 'remote' == self.location:
            self.package_update()
        else:
            actions.extend(self.package_update_actions())
            return actions

    def trigger_update_dependencies(self, token=None):
        """
        Check if we have a github integration set up and direct the call to the correct code path.
        If a github integration is set, we assume it is running to auto update platformsh templates
        """
        if self.use_integration:
            print("Using github integration")
            return self._trigger_update_dependencies_with_github_integration(token)
    @property
    def branch(self):
        if 'remote' == self.location:
            if subprocess.call(["git", "rev-parse", "--verify", "--quiet", UPDATER_BRANCH_NAME],
                               cwd=self.builddir) == 0:
                subprocess.call(["git", "checkout", "master"], cwd=self.builddir)
                subprocess.call(["git", "branch", "-D", UPDATER_BRANCH_NAME], cwd=self.builddir)
            subprocess.call(["git", "checkout", "-b", UPDATER_BRANCH_NAME], cwd=self.builddir)
            subprocess.call(["git", "add", "-A"], cwd=self.builddir)
            subprocess.call(["git", "commit", "-m", "Update to latest upstream"], cwd=self.builddir)
        else:
            return [
                'cd {0} && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;'.format(
                    self.builddir),
                'cd {0} && git checkout -b update'.format(self.builddir),
                # git commit exits with 1 if there's nothing to update, so the diff-index check will
                # short circuit the command if there's nothing to update with an exit code of 0.
                'cd {0} && git add -A && git diff-index --quiet HEAD || git commit -m "Update to latest upstream"'.format(
                    self.builddir),
            ]

    @property
    def push(self):
        if 'remote' == self.location:
            if subprocess.check_output(["git", "rev-parse", UPDATER_BRANCH_NAME], cwd=self.builddir) != subprocess.check_output(["git", "rev-parse", "master"], cwd=self.builddir):
                subprocess.call(["git", "checkout", UPDATER_BRANCH_NAME], cwd=self.builddir)
                subprocess.call(["git", "push", "--force", "-u", "origin", UPDATER_BRANCH_NAME], cwd=self.builddir)
        else:
            return [
                'cd {0} && if [ `git rev-parse update` != `git rev-parse master` ] ; then git checkout update && git push --force -u origin update; fi'.format(
                    self.builddir)
            ]


    def create_pull_request(self, token=None):
        """
        Creates a pull request from the "UPDATER_BRANCH_NAME" branch to master.
        """

        pulls_api_url = 'https://api.github.com/repos/{0}/pulls'.format(self.repo)

        body = {"head": UPDATER_BRANCH_NAME, "base": "master", "title": "Update to latest upstream"}

        print("Creating pull request.")

        response = requests.post(pulls_api_url, headers=self._get_github_auth_header(token), data=json.dumps(body))

        if response.status_code == 201:
            return True

        # the PR creation can fail if the PR already exists, we should skip the creation and continue
        if response.status_code == 422 and response.json()['message']=="Validation Failed" and "A pull request already exists for" in response.text:
            return True

        print("Failed to create pull request.")
        print(response.content)
        return False

    def run_tests(self, urls_to_test):
        # Delays execution by specified amount of seconds
        print("Delaying execution of tests by {0} seconds.".format(self.TEST_DELAY))
        time.sleep(self.TEST_DELAY)

        print("Running {0} tests.".format(len(self.TEST_FUNCTIONS)))
        for test in self.TEST_FUNCTIONS:
            if isinstance(urls_to_test, list):
                self.test_results[0] = urls_to_test
            else:
                for pull_number, url in urls_to_test.items():
                    self.test_results[pull_number] = test(url)

        return self.test_results

    def test_pull_requests(self, token=None):
        """
        Calls all the tests defined in self.TEST_FUNCTIONS on the test urls.
        """
        # Build a list of urls to test
        urls_to_test = self.get_test_urls(token)
        if not urls_to_test:
            print("No pull requests to test for {0}".format(self.name))
            return

        return self.run_tests(urls_to_test)

    def merge_pull_requests(self, token=None):
        """
        Merges pull requests that pass tests.
        """
        if not self.test_results:
            self.test_pull_requests(token=token)

        authorization_header = self._get_github_auth_header(token)
        pulls_api_url = 'https://api.github.com/repos/{0}/pulls'.format(self.repo)
        pulls = requests.get(pulls_api_url, headers=authorization_header).json()

        responses = []
        for pull in pulls:
            if self.test_results.get(pull["number"]):
                merge_url = "{0}/{1}/merge".format(pulls_api_url, pull['number'])
                response = requests.put(merge_url, headers=authorization_header)
                self._print_and_flush("Merging pull request {0}".format(merge_url))

                if response.status_code in [200, 204]:
                    self._print_ok(" [MERGED]")
                else:
                    self._print_failed()
                    print(response.json())

                responses.append(response)

        return all(response.status_code in [200, 204] for response in responses)

    def package_update(self):
        """
        Generates a list of package updater commands based on the updateCommands property.
        Update commands generated for each app by walking build directory checking for presence of `.platform.app.yaml` file.
        :return: List of package update commands to include.
        """
        for directory in os.walk(self.builddir):
            if '.platform.app.yaml' in directory[2]:
                for file, command in self.updateCommands.items():
                    if os.path.exists(os.path.join(directory[0], file)):
                        subprocess.check_call(shlex.split(command), cwd=directory[0])

    def modify_composer(self, mod_function):
        """
        Wordpress requires more Composer modification than can be done
        with the Composer command line.  This function modifies the composer.json
        file as raw JSON instead.
        """

        with open('{0}/composer.json'.format(self.builddir), 'r') as f:
        # The OrderedDict means that the property orders in composer.json will be preserved.
            composer = json.load(f, object_pairs_hook=OrderedDict)

        composer = mod_function(composer)

        with open('{0}/composer.json'.format(self.builddir), 'w') as out:
            json.dump(composer, out, indent=2)

    def get_test_urls(self, token):
        """
        Returns URLs of environments integrated to active pull requests.
        """
        authorization_header = self._get_github_auth_header(token)

        pulls_api_url = 'https://api.github.com/repos/{0}/pulls'.format(self.repo)
        pulls = requests.get(pulls_api_url, headers=authorization_header)
        urls = {}
        for pull in pulls.json():
            if "dependabot" in pull["user"]["login"]:
                print("skipping dependabot pull request")
                continue
            statuses_api_url = pull["statuses_url"]
            deployment_status = "pending"
            while deployment_status != "success":
                status = requests.get(statuses_api_url, headers=authorization_header)
                if not status.json():
                    continue
                try:
                    data = status.json()[0]
                    url = data["target_url"]
                    deployment_status = data["state"]

                    if deployment_status == "failed":
                        print("Pull request {0} was not built on Platform.sh".format(pull["url"]))
                    if deployment_status == "success":
                        break

                except Exception as e:
                    print("Error retrieving build status of pull request {0} on Platform.sh".format(pull["url"]))
                    print(e)

                print("Waiting for build {0} to finish on Platform.sh...".format(pull["url"]))
                time.sleep(20)

            print("Pull request {0} has finished building on Platform.sh.".format(url))
            urls[pull["number"]] = url

        return urls

    def _reset_update_branch(self, token=None):
        refs_api_url = "https://api.github.com/repos/{0}/git/refs".format(self.repo)

        self._print_and_flush("Resetting '{0}' branch".format(UPDATER_BRANCH_NAME))

        master_sha = subprocess.check_output([self.platform_path, "environment:info", "--environment", "master", "head_commit"]).decode("utf-8").strip()

        body = {"ref": "refs/heads/{0}".format(UPDATER_BRANCH_NAME), "sha": master_sha}
        response = requests.post(refs_api_url, headers=self._get_github_auth_header(token), data=json.dumps(body))

        if response.status_code == 201 or (response.status_code == 422 and response.json()['message'] == "Reference already exists"):
            return self._print_ok()

        # if we get here, it failed, show a bit of debug info
        self._print_failed()
        print(response.content)
        return False

    def _set_github_token(self, token):
       # CMD line token overrides env var token.
       if token is not None:
           self.github_token = token
       # If token is still not set, alert user. Pd: Cannot failt gracefully as it is not on main task code.
       if self.github_token is None:
           raise BaseException("Github token not provided. Please provide via --token argument or via env:GITHUB_TOKEN var.")

    def _install_platform_cli(self):
        proc1 = subprocess.Popen(["curl","-fsS","https://platform.sh/cli/installer"], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(["php"], shell=True, stdin=proc1.stdout)
        proc1.stdout.close()
        proc2.wait(timeout=300) # 5 minutes should be enough for everybody

    def _print_and_flush(self, txt):
        print(txt, end='')
        os.sys.stdout.flush()

    def _print_ok(self, txt=' [OK]'):
        color.print(color.green, txt)
        return True

    def _print_failed(self, txt=' [FAILED]'):
        color.print(color.red, txt)
        return False

    def _wait_until_environment_is_ready(self, env, wait_time=30):
        self._print_and_flush("Wait until environment '{0}' is ready...".format(env))

        # Using an internal function so I can better handle the loop and failures
        def _wait_and_check(env, wait_time, fail_counter=0):
            time.sleep(wait_time)

            # platform activity:list -e "$ENV_NAME" --incomplete --format=csv | wc -l
            p = subprocess.run([self.platform_path, "activity:list", "--environment", env, "--incomplete", "--format=csv"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            if p.stdout:
                lines = p.stdout.decode("utf-8").strip().splitlines()
                # Check if env is dirty, and wait a few seconds before rechecking
                while (len(lines) > 0):
                    self._print_and_flush(".")
                    return _wait_and_check(env, wait_time, fail_counter)

            else:
                if(p.stderr.decode("utf-8").strip() == "No activities found"):
                    return True

                self._print_and_flush('F')
                # If we get an error code, chances are that we don't have the environment created yet (possible that the integration didnt push it yet)
                if fail_counter > 3:
                    self._print_failed()
                    raise CliEnvironmentNotExistException("Environment doesn't seem to exist.")
                return _wait_and_check(env, wait_time, fail_counter+1)


        if _wait_and_check(env, wait_time):
            self._print_ok()

    def _trigger_update_dependencies_with_github_integration(self, token=None):
        print("Preparing to update {0}".format(self.name))
        self._reset_update_branch(token)

        try:
            self._wait_until_environment_is_ready(UPDATER_BRANCH_NAME)
        except CliEnvironmentNotExistException as e:
            print("")
            print("Environment {0} doesn't exist yet, please create the branch first with the following command: ".format(UPDATER_BRANCH_NAME))
            print("  platform environment:branch {0} --force --no-clone-parent -e master --wait --yes".format(UPDATER_BRANCH_NAME))
            return
        except Exception as e:
            import sys, traceback
            print(e)
            traceback.print_exc(file=sys.stdout)
            return

        print("Activating environment '{0}'".format(UPDATER_BRANCH_NAME))
        subprocess.check_call([self.platform_path, "environment:activate", UPDATER_BRANCH_NAME, "--yes", "--wait"]) # platform environment:activate update --yes;
        if not self._run_source_operation(UPDATER_BRANCH_NAME):
            return

        self._wait_until_environment_is_ready(UPDATER_BRANCH_NAME)

        # we need to stop on a failure
        if not self.create_pull_request(token):
            return

        # cleaning up UPDATER BRANCH, probably not a good idea because then we have to clone the master every time
        # print(f"Deactivating environment '{UPDATER_BRANCH_NAME}'")
        # subprocess.run([self.platform_path, "environment:delete", UPDATER_BRANCH_NAME, "--yes"]) # no need to wait here

        if not self.test_pull_requests(token):
            return

        if not self.merge_pull_requests(token):
            return

    def _run_source_operation(self, branch_name):
        self._print_and_flush("Running source operation '{0}' on environment '{1}'".format(UPDATER_SOURCEOP_NAME, branch_name))

        p = subprocess.run([self.platform_path, "source-operation:run", UPDATER_SOURCEOP_NAME, "--environment", branch_name, "--wait"], stderr=subprocess.PIPE, stdout=subprocess.PIPE) # platform source-operation:run update --environment update;

        if p.returncode != 0 and p.stderr:
            self._print_failed()
            print(p.stderr.decode("utf-8").strip())
            return False

        return self._print_ok()

    def _get_github_auth_header(self,token=None):
        self._set_github_token(token)

        return {"Authorization": "token {0}".format(self.github_token)}



    @staticmethod
    def basic_smoke_test(url):
        """
        Basic smoke test for a single PR. Only checks for a 200 OK response.
        """
        try:
            response = requests.get(url)
        except requests.exceptions.SSLError:
            response = requests.get(url, verify=False)

        if response.status_code != 200:
            print("Test failed on {0} with code {1}".format(response.url, response.status_code))
        return response.status_code == 200

    def build_update_commands(self):
        self.updateCommands['composer.json'] += " ".join(self.composer_defaults())
        # if 'remote' == self.location:
        #     self.updateCommands['composer.json'] += " ".join(self.composer_defaults())
        # else:
        #     self.updateCommands['composer.json'] += self.composer_defaults()


    def package_update_actions(self):
        """
        Generates a list of package updater commands based on the updateCommands property.
        Update commands generated for each app by walking build directory checking for presence of `.platform.app.yaml` file.
        :return: List of package update commands to include.
        """
        actions = []
        for directory in os.walk(self.builddir):
            if '.platform.app.yaml' in directory[2]:
                for file, command in self.updateCommands.items():
                    actions.append(
                        'cd {0} && [ -f {1} ] && {2} || echo "No {1} file found, skipping."'.format(directory[0], file,
                                                                                                    command))
        return actions

