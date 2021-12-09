from .remote import RemoteProject
from .composer import ComposerProject


class Pimcore(ComposerProject):
    major_version = 'v2.7'
    remote = 'https://github.com/pimcore/skeleton.git'

    @property
    @ComposerProject.composer_platformify()
    def platformify(self):
        return super(Pimcore, self).platformify + [
            'cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm  '
            '--no-scripts'.format(self.builddir) + self.composer_defaults(),
        ]
