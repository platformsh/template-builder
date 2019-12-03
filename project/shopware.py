from .remote import RemoteProject


class Shopware(RemoteProject):
    major_version = 'v5'
    remote = 'https://github.com/shopware/shopware.git'

    @property
    def platformify(self):
        return super(Shopware, self).platformify + [
            'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader'.format(self.builddir),
        ]
