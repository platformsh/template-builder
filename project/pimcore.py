from .composer import ComposerProject


class Pimcore(ComposerProject):
    major_version = 'v2.7'
    remote = 'https://github.com/pimcore/skeleton.git'

    @property
    @ComposerProject.composer_platformify
    def platformify(self):
        """
        @todo why are we running composer update *again* at this stage? This makes the THIRD time we've run composer
        update during a doit full command: once during the `update` stage, once in the parent `platformify` stage
        and now once in this stage.
        :return:
        """
        return super(Pimcore, self).platformify + [
            'cd {0} && export COMPOSER_MEMORY_LIMIT=-1 && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm  '
            '--no-scripts'.format(self.builddir) + self.composer_defaults(),
        ]

    def composer_defaults(self):
        return super(ComposerProject, self).composer_defaults() + ' --no-scripts'

    def __init__(self, name):
        super(Pimcore, self).__init__(name)
        self.updateCommands['composer.json'] = self.updateCommands['composer.json'].replace('composer update','export COMPOSER_MEMORY_LIMIT=-1 && composer update')
