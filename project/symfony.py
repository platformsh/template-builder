from .remote import RemoteProject


class Symfony4(RemoteProject):
    major_version = 'v4'
    remote = 'https://github.com/symfony/skeleton.git'

    @property
    def platformify(self):
        return super(Symfony4, self).platformify + [
            # Symfony Flex now pins the lock files to a specific PHP version, so we have to in the platform version
            # as well to avoid issues if the lock files are generated on a newer PHP version than the template uses.
            # Keep this in sync with the template's PHP verison.
            'cd {0} && composer config platform.php 7.4'.format(self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge ^2.7'.format(self.builddir) + self.composer_defaults(),
        ]

class Symfony5(RemoteProject):
    major_version = 'v5'
    remote = 'https://github.com/symfony/skeleton.git'

    @property
    def platformify(self):
        return super(Symfony5, self).platformify + [
            # Symfony Flex now pins the lock files to a specific PHP version, so we have to in the platform version
            # as well to avoid issues if the lock files are generated on a newer PHP version than the template uses.
            # Keep this in sync with the template's PHP verison.
            'cd {0} && composer config platform.php 7.4'.format(self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge ^2.7'.format(self.builddir) + self.composer_defaults(),
        ]
