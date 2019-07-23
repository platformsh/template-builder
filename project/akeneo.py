from .remote import RemoteProject


class Akeneo(RemoteProject):
    major_version = 'v3'
    remote = 'https://github.com/akeneo/pim-community-standard.git'

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
<<<<<<< HEAD
                'cd {0} && composer require platformsh/config-reader --no-scripts --ignore-platform-reqs'.format(self.builddir),]
=======
                'cd {0} && composer require platformsh/config-reader --no-scripts --ignore-platform-reqs'.format(
                    self.builddir),]
>>>>>>> deecb37ad31d62c17cfa1b8d0a87054b3c7aed21
