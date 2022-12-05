from .remote import RemoteProject


class Sylius(RemoteProject):
    major_version = 'v1.12'
    remote = 'https://github.com/Sylius/Sylius-Standard.git'

    def composer_defaults(self):
        # get the default list from parent
        composerDefaults = super(Sylius, self).composer_defaults()
        # remove the ignore platform php line
        composerDefaults = composerDefaults.replace(' --ignore-platform-req=php', '')

        return composerDefaults

    @property
    def platformify(self):
        return super(Sylius, self).platformify + [
            'cd {0} && cp README.md README_upstream.md'.format(self.builddir),
            'cd {0} && ls -a'.format(self.builddir),
            'cd {0} && rm -rf .github'.format(self.builddir),
            'cd {0} && [ ! -e "./config/packages/swiftmailer.yaml" ] || rm "./config/packages/swiftmailer.yaml"'.format(self.builddir),
            'cd {0} && composer config allow-plugins.symfony/flex true --no-plugins '.format(self.builddir),
            'cd {0} && composer config allow-plugins.dealerdirect/phpcodesniffer-composer-installer true --no-plugins '.format(
                self.builddir),
            'cd {0} && composer config allow-plugins.phpstan/extension-installer true --no-plugins '.format(
                self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge'.format(self.builddir) + self.composer_defaults(),
        ]
