from .remote import RemoteProject


class Pimcore(RemoteProject):
    major_version = 'v2.7'
    remote = 'https://github.com/pimcore/skeleton.git'

    @property
    def platformify(self):
        return super(Pimcore, self).platformify + [
            'cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm  --no-scripts'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && composer config allow-plugins.ocramius/package-versions true --no-plugins'.format(self.builddir),
        ]
