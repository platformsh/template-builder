from . import BaseProject
from .remote import RemoteProject


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
        composerDefaults = super(WordPressComposerBase, self).composer_defaults()
        # remove the ignore platform php line
        composerDefaults = composerDefaults.replace(' --ignore-platform-req=php', '')

        return composerDefaults

    def unpin_dependencies(self,composer,dependencies=[]):
        for dependency in dependencies:
            if dependency in composer['require']:
                composer['require'][dependency] = self.unlock_version(composer['require'][dependency])

        return composer

    def _modify_composer(self, composer, dependencies=[]):
        dependencies = self.unPinDependencies + dependencies
        composer = self.unpin_dependencies(composer, dependencies)
        return composer


    @property
    def platformify(self):
        # get the versions
        actions = super(WordPressComposerBase, self).platformify
        if hasattr(self, 'type') and hasattr(self, 'typeVersion') and 'php' == self.type:
            actions = ["echo 'Adding composer config:platform:php'",
                       "cd {0} && composer config platform.php {1}".format(self.builddir, self.typeVersion)] + actions
            # now add the child commands
            actions = actions + self._platformify
            actions = actions + ["echo 'Removing composer config:platform'",
                                 "cd {0} && composer config --unset platform".format(self.builddir)]
            # print("Our complete list of actions")
            # pprint(actions)
        else:
            actions = actions + self._platformify

        return actions

    @property
    def _platformify(self):
        return []
