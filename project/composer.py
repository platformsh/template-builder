from . import BaseProject
from .remote import RemoteProject
from pprint import pprint


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

    def composer_platformify(func):
        def wrapper(self):

            # if we're a php project and we have a version, let's add in our extra commands
            if hasattr(self, 'type') and hasattr(self, 'typeVersion') and 'php' == self.type:
                actions = ["echo 'Adding composer config:platform:php'",
                           "cd {0} && composer config platform.php {1}".format(self.builddir,
                                                                               self.typeVersion)]
                # now add the child commands
                actions += func(self)
                actions += ["echo 'Removing composer config:platform'",
                            "cd {0} && composer config --unset platform".format(self.builddir)]
            else:
                actions = func()

            return actions

        return wrapper
