from .remote import RemoteProject


class Mautic(RemoteProject):
    major_version = '2'
    remote = 'https://github.com/mautic/mautic.git'

    @property
    def platformify(self):
        return super(Mautic, self).platformify + [
            'cd {0} && composer remove friendsofphp/php-cs-fixer --ignore-platform-reqs'.format(
                self.builddir)
        ]
