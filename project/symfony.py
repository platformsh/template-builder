from .remote import RemoteProject


class Symfony3(RemoteProject):
    update_branch = '3.4'
    remote = 'https://github.com/symfony/symfony-standard.git'


class Symfony4(RemoteProject):
    update_branch = '4.2'
    remote = 'https://github.com/symfony/skeleton.git'

    @property
    def platformify(self):
        return super(Symfony4, self).platformify + [
            'cd {0} && composer require platformsh/symfonyflex-bridge'.format(
                self.builddir)
        ]
