import os
import os.path
from os.path import exists
import sys
import json
import yaml
from glob import glob
from collections import OrderedDict

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
        
        if os.environ.get("UPDATES_BRANCH"):
            self.updateBranch = os.environ.get("UPDATES_BRANCH")
        else:
            self.updateBranch = 'updatesLocal'

        if os.environ.get("UPDATE_COMMIT_MSG"):
            self.commitMessage = os.environ.get("UPDATE_COMMIT_MSG")
        else:
            self.commitMessage = "Update to latest upstream."

        # Include default switches on all composer commands. This can be over-ridden per-template in a subclass.
        if 'composer.json' in self.updateCommands:
            self.updateCommands['composer.json'] += self.composer_defaults()

        # @todo what about multiapps?
        if exists(os.path.join(TEMPLATEDIR, self.name, 'files/','.platform.app.yaml')):
            """
            prevents pyyaml from complaining about !include tags in our platform.app.yaml
            Please note that it will NOT follow and load those include files.
            Blatantly ~stolen~ borrowed from https://stackoverflow.com/a/52241794/17151558
            """
            def any_constructor(loader, tag_suffix, node):
                if isinstance(node, yaml.MappingNode):
                    return loader.construct_mapping(node)
                if isinstance(node, yaml.SequenceNode):
                    return loader.construct_sequence(node)
                return loader.construct_scalar(node)

            yaml.add_multi_constructor('', any_constructor, Loader=yaml.SafeLoader)

            # @todo should we define the file name and location elsewhere?
            with open(os.path.join(TEMPLATEDIR, self.name, 'files/','.platform.app.yaml'), "r") as stream:
                try:
                    platformAppYaml = yaml.safe_load(stream)
                    # @todo should we check to make sure we have a type key before using it?
                    # @todo is there ever a situation where we might end up with more than two parts?
                    self.type, self.typeVersion = platformAppYaml['type'].split(':')
                except yaml.YAMLError as exc:
                    print(exc)

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
        1) Copy the contents of common files that we want in all templates.
        2) Copy the contents of the files/ directory in the project over the
           application, replacing what's there.
        3) Apply any *.patch files found in the project directory, in alphabetical order.

        Individual projects may expand on these tasks as needed.
        """
        actions = ['rsync -aP {0} {1}'.format(
            os.path.join(ROOTDIR,'common/all/'),  self.builddir
        ),
        'rsync -aP {0} {1}'.format(
            os.path.join(TEMPLATEDIR, self.name, 'files/'),  self.builddir
        )
        ]
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
            'cd {0} && if git rev-parse --verify --quiet {1}; then git checkout master && git branch -D {1}; fi;'.format(
                self.builddir, self.updateBranch),
            'cd {0} && git checkout -b {1}'.format(self.builddir, self.updateBranch),
            # git commit exits with 1 if there's nothing to update, so the diff-index check will
            # short circuit the command if there's nothing to update with an exit code of 0.
            'cd {0} && git add -A && git diff-index --quiet HEAD || git commit -m "{1}"'.format(
                self.builddir, self.commitMessage),
        ]

    @property
    def push(self):
        return ['cd {0} && if [ `git rev-parse {1}` != `git rev-parse master` ] ; then git checkout {1} && git push --force -u origin {1}; fi'.format(
            self.builddir, self.updateBranch)
        ]

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
