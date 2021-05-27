import os
import os.path
import json
from glob import glob
from collections import OrderedDict
import time
import requests

ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATEDIR = os.path.join(ROOTDIR, 'templates')

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
        'Pipfile': 'pipenv update',
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
        return (' --prefer-dist --no-interaction '
                '--ignore-platform-req=ext-redis '
                '--ignore-platform-req=ext-apcu '
                '--ignore-platform-req=ext-intl '
                '--ignore-platform-req=ext-bcmath '
                '--ignore-platform-req=ext-exif '
                '--ignore-platform-req=ext-gd '
                '--ignore-platform-req=ext-imagick '
                '--ignore-platform-req=ext-mbstring '
                '--ignore-platform-req=ext-memcache '
                '--ignore-platform-req=ext-pdo '
                '--ignore-platform-req=ext-openssl '
                '--ignore-platform-req=ext-zip '
                '--ignore-platform-req=php'
                )

    def __init__(self, name):
        self.name = name
        self.builddir = os.path.join(TEMPLATEDIR, self.name, 'build/')
        # Parses the github authorization token from env var by default.
        self.github_token = os.getenv('GITHUB_TOKEN', None)

       
        # A list containing function references which will be executed against a test url, bootstrapped with a basic smoke test.
        self.TEST_FUNCTIONS = [self.basic_smoke_test]

        # Include default switches on all composer commands. This can be over-ridden per-template in a subclass.
        if 'composer.json' in self.updateCommands:
            self.updateCommands['composer.json'] += self.composer_defaults()

    @property
    def cleanup(self):
        return ['rm -rf {0}'.format(self.builddir)]

    @property
    def init(self):
        if hasattr(self, 'github_name'):
            name = self.github_name
        else:
            name = self.name.replace('_', '-')
        return ['git clone git@github.com:platformsh-templates/{0}.git {1}'.format(
            name, self.builddir)
        ]

    @property
    def update(self):
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
        actions = ['rsync -aP {0} {1}'.format(
            os.path.join(TEMPLATEDIR, self.name, 'files/'),  self.builddir
        )]
        patches = glob(os.path.join(TEMPLATEDIR, self.name, "*.patch"))
        for patch in patches:
            actions.append('cd {0} && patch -p1 < {1}'.format(
                self.builddir, patch)
            )

        # In some cases the package updater needs to be run after we've platform-ified the
        # template, so run it a second time. Worst case it's a bit slower to build but doesn't
        # hurt anything.
        actions.extend(self.package_update_actions())

        return actions

    @property
    def branch(self):
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
        return ['cd {0} && if [ `git rev-parse update` != `git rev-parse master` ] ; then git checkout update && git push --force -u origin update; fi'.format(
            self.builddir)
        ]

    def pull_request(self, token=None):
        """
        Creates a pull request from the "update" branch to master.
        """
        self.set_github_token(token)

        authorization_header = {"Authorization": "token " + self.github_token}

        pulls_api_url = 'https://api.github.com/repos/platformsh-templates/{0}/pulls'.format(self.name)

        body = {"head": "update", "base": "master", "title": "Update to latest upstream"}
        response = requests.post(pulls_api_url, headers=authorization_header, data=json.dumps(body))
        print(response)
        print(response.text)
        print(response.headers)
        return response.status_code in [201, 422]

    def test(self, token=None):
        """
        Calls all the tests defined in self.TEST_FUNCTIONS on the test urls.
        """
        self.set_github_token(token)

        self.results = {}

        urls_to_test = self.get_test_urls()
        if not urls_to_test:
            print("No pull requests to test for {0}".format(self.name))
            return

        print(f"Running {len(self.TEST_FUNCTIONS)} tests.")
        for test in self.TEST_FUNCTIONS:
            for pull_number, url in urls_to_test.items():
                self.results[pull_number] = test(url)

        return self.results

    def merge_pull_request(self, token=None):
        """
        Merges pull requests that pass tests.
        """
        self.set_github_token(token)
        print(self.results)
        authorization_header = {"Authorization": "token " + self.github_token}
        pulls_api_url = 'https://api.github.com/repos/platformsh-templates/{0}/pulls'.format(self.name)

        pulls = requests.get(pulls_api_url, headers=authorization_header).json()
        responses = []
        for pull in pulls:
            if self.results.get(pull["number"]):
                merge_url = f"{pulls_api_url}/{pull['number']}/merge"
                responses.append(requests.put(merge_url, headers=authorization_header))
                print(f"Merged pull request {merge_url}")
        return all(response.status_code in [200, 204] for response in responses)


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
                    actions.append('cd {0} && [ -f {1} ] && {2} || echo "No {1} file found, skipping."'.format(directory[0], file, command))

        return actions

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

    def get_test_urls(self):
        """
        Returns URLs of environments integrated to active pull requests.
        """
        authorization_header = {"Authorization": "token " + self.github_token}

        pulls_api_url = 'https://api.github.com/repos/platformsh-templates/{0}/pulls'.format(self.name)
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
                    print(data)
                    url = data["target_url"]
                    deployment_status = data["state"]

                    if deployment_status == "failed":
                        print("Pull request {0} was not built on Platform.sh".format(pull["url"]))
                    if deployment_status == "success":
                        break

                except Exception as e:
                    print("Error retrieving build status of pull request {0} on Platform.sh".format(pull["url"]))
                    print(e)

                print("Pull request {0} is still building on Platform.sh".format(pull["url"]))
                time.sleep(10)
            
            print(f"Pull request {url} has finished building on Platform.sh")
            urls[pull["number"]] = url
        
        # Delays execution by specified amount of seconds    
        if urls:
            print(f"Delaying execution of tests by {self.TEST_DELAY} seconds.")
            time.sleep(self.TEST_DELAY)
        return urls
   
    def set_github_token(self, token):
       # CMD line token overrides env var token.
       if token is not None:
           self.github_token = token
       # If token is still not set, alert user. Pd: Cannot failt gracefully as it is not on main task code.
       if self.github_token is None:
           print("Github token not provided. Please provide via --token argument or via GITHUB_TOKEN env var.")
