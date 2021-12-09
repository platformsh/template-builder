from . import BaseProject
from .remote import RemoteProject
from pprint import pprint
from functools import wraps


class ComposerProject(RemoteProject):
    unPinDependencies = []

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

    def composer_platformify(position=0):
        """ Decorator to inject composer commands to ensure the targeted php version matches the platform container image

        :var position indicates the location of where our first set of commands should be injected. platformify() needs
        them at the beginning (0); update() needs it as 1

        The original developer used --ignore-platform-req=php to ensure the locally installed version of php when running
        the update didn't prevent or interfere with composer being able to update. Now that we support 4 php container
        images (7.3, 7.4, 8.0, and 8.1 + 7.2 on dedicated) we needed to be sure that we were running composer commands
        restricted to the same version of php that will be deployed.

        @TODO I was unsure if this should be one decorator with parameters, or two separate methods. Might need to be split
        """
        def wrapper(func):
            @wraps(func)
            def inject_config(self):
                # if we're a php project and we have a version, let's add in our extra commands
                if hasattr(self, 'type') and hasattr(self, 'typeVersion') and 'php' == self.type:
                    newActions = ["echo 'Adding composer config:platform:php'",
                               "cd {0} && composer config platform.php {1}".format(self.builddir,
                                                                                   self.typeVersion)]
                    if 0 == position:
                        # our actions first
                        actions = newActions
                        # now the rest
                        actions += func(self)
                    else:
                        # get the list of all the steps first
                        actions = func(self)
                        if len(actions) > 0 :
                            # find the index of where composer update is included
                            composerIndex = next(i for i, string in enumerate(actions) if 'composer update' in string)
                            # now slice in our newActions right after the first step
                            actions = actions[0:composerIndex] + newActions + actions[composerIndex:]

                    # now add our ending commands
                    actions += ["echo 'Removing composer config:platform'",
                                "cd {0} && composer config --unset platform".format(self.builddir)]
                else:
                    actions = func()

                return actions
            return inject_config
        return wrapper

    @composer_platformify(1)
    def package_update_actions(self):
        return super(ComposerProject, self).package_update_actions()

    @property
    @composer_platformify()
    def platformify(self):
        return super(ComposerProject, self).platformify
