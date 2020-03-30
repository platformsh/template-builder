from .remote import RemoteProject


class Symfony3(RemoteProject):
    major_version = 'v3.4'
    remote = 'https://github.com/symfony/symfony-standard.git'

    @property
    def platformify(self):
        return super(Symfony3, self).platformify + [
            # Symfony 3 ships with a composer.json file that specifies a platform target
            # Of PHP 5.6, for no good reason, even though it depends on Doctrine, which
            # requires PHP 7.1.  Since we're guaranteeing a PHP 7.4 environment, just
            # change that requirement to 7.4 and be done with it.
            'cd {0} && composer config platform.php 7.4'.format(
                self.builddir),
            # Monolog-Bundle allows for Monolog 1.x or 2.x, but nothing else forces Monolog 1.x, so by default
            # 2.x gets installed.  That's explicitly not compatible with Symfony < 5, however.  Instead, force
            # an extra dependency on Monolog 1 to sidestep that issue.  It has to be done in a single install
            # step to avoid issues with Symfony's install script failing if either of these packages are missing.
            'cd {0} && composer require platformsh/config-reader monolog/monolog ~1.22 --ignore-platform-reqs'.format(
                self.builddir),
        ]


class Symfony4(RemoteProject):
    major_version = 'v4'
    remote = 'https://github.com/symfony/skeleton.git'

    @property
    def platformify(self):
        return super(Symfony4, self).platformify + [
            # Symfony Flex now pins the lock files to a specific PHP version, so we have to in the platform version
            # as well to avoid issues if the lock files are generated on a newer PHP version than the template uses.
            # Keep this in sync with the template's PHP verison.
            'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge ^2.2 --ignore-platform-reqs'.format(self.builddir),
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
            'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge ^2.2 --ignore-platform-reqs'.format(self.builddir),
        ]
