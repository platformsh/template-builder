import os
import os.path
from os.path import exists
from . import BaseProject
from .remote import RemoteProject
from pprint import pprint
from functools import wraps
from . import TEMPLATEDIR
import yaml
import re


class ComposerProject(RemoteProject):
    unPinDependencies = []

    def __init__(self, name):
        super(ComposerProject, self).__init__(name)
        # Include default switches on all composer commands. This can be over-ridden per-template in a subclass.
        if 'composer.json' in self.updateCommands:
            self.updateCommands['composer.json'] += self.composer_defaults()

        # @todo what about multiapps?
        if exists(os.path.join(TEMPLATEDIR, self.name, 'files/', '.platform.app.yaml')):
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
            with open(os.path.join(TEMPLATEDIR, self.name, 'files/', '.platform.app.yaml'), "r") as stream:
                try:
                    platformAppYaml = yaml.safe_load(stream)
                    # @todo should we check to make sure we have a type key before using it?
                    # @todo is there ever a situation where we might end up with more than two parts?
                    self.type, self.typeVersion = platformAppYaml['type'].split(':')
                    try:
                        composer_version = platformAppYaml['dependencies']['php']['composer/composer']
                        composer_version = int(re.findall(r'\d+', composer_version)[0])
                    except KeyError:
                        composer_version = 1

                    self.composer_version = composer_version
                except yaml.YAMLError as exc:
                    print(exc)

    # Upstream script locks a specific version in composer.json, keeping users from updating locally.
    # @todo should this be a classmethod?
    def unlock_version(self, locked_version):
        if '^' not in locked_version:
            return '^{}'.format(locked_version)
        else:
            return locked_version

    # until we convert all php templates to use this method, we need to remove the 'ignore platform' composer param
    def composer_defaults(self):
        # get the default list from parent
        composerDefaults = super(ComposerProject, self).composer_defaults()
        # remove the ignore platform php line
        composerDefaults = composerDefaults.replace(' --ignore-platform-req=php', '')

        return composerDefaults

    def unpin_dependencies(self, composer, dependencies=[]):
        for dependency in dependencies:
            if dependency in composer['require']:
                composer['require'][dependency] = self.unlock_version(composer['require'][dependency])

        return composer

    def modify_composer_config(self, composer, dependencies=[]):
        composer = self.unpin_dependencies(composer, dependencies)
        return composer

    def composer_platformify(func):
        """ Decorator to inject composer commands to ensure the targeted php version matches the platform container image

        The original developer used --ignore-platform-req=php to ensure the locally installed version of php when running
        the update didn't prevent or interfere with composer being able to update. Now that we support 4 php container
        images (7.3, 7.4, 8.0, and 8.1 + 7.2 on dedicated) we needed to be sure that we were running composer commands
        restricted to the same version of php that will be deployed.

        WHERE we inject our composer config platform:php command depends on whether we're running an update, or platformify.
        For update, we can't inject until right before we run composer update since doing it before can cause a merge
        conflict. We CAN run it first for platformify since at that point we've already performed update and have a
        working directory to use.

        @TODO change the name since this adjusts both update and platformify?
        """

        @wraps(func)
        def wrapper(self):
            validFuncs = ['platformify', 'update']
            if hasattr(self, 'type') and hasattr(self,
                                                 'typeVersion') and 'php' == self.type and func.__name__ in validFuncs:
                preActions = ["echo 'Adding composer config:platform:php'",
                              "cd {0} && composer config platform.php {1}".format(self.builddir,
                                                                                  self.typeVersion)]
                postActions = ["echo 'Removing composer config:platform'",
                               "cd {0} && composer config --unset platform".format(self.builddir)]

                """
                Some of the templates still require version 1 of composer. If they havent updated the platform.app.yaml
                file to v2 of composer, then we'll need to downgrade the local version to v1 and then roll it back at the
                end
                """
                if self.composer_version is not None and self.composer_version < 2 :
                    preActions = ['echo "Downgrading composer to v1"', 'composer self-update --1'] + preActions
                    postActions += ['echo "Upgrading composer back to version2"', 'composer self-update --2']

                if 'platformify' == func.__name__:
                    # our actions first
                    actions = preActions
                    # now the rest
                    actions += func(self)
                elif 'update' == func.__name__:
                    # get the list of all the steps first
                    actions = func(self)

                    if len(actions) > 0:
                        # pprint(actions)
                        try:
                            # find the index of where composer update is included
                            composerIndex = next(index for index, string in enumerate(actions) if
                                                 isinstance(string, str) and 'composer update' in string)
                            # now slice in our newActions right after the first step
                            actions = actions[0:composerIndex] + preActions + actions[composerIndex:]
                        except StopIteration:
                            pass

                # now add our ending commands
                actions += postActions
            else:
                actions = func()

            return actions

        return wrapper

    @property
    @composer_platformify
    def update(self):
        return super(ComposerProject, self).update
