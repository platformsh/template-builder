from .remote import RemoteProject


class Mautic(RemoteProject):
    major_version = '2'
    remote = 'https://github.com/mautic/mautic.git'


    @property
    def update(self):
        actions = super(Mautic, self).update

        # composer update will pull in Twig 2 instead of Twig 1, which is declared
        # compatible according to the composer.json files but really isn't. It will crash
        # when compiling templates. So force Twig 1 here, before the first composer update
        # runs.
        actions.insert(4, 'cd {0} && composer require twig/twig ~1.42 --no-scripts --ignore-platform-reqs'.format(
            self.builddir))

        return actions
