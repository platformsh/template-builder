from .remote import RemoteProject


class Akeneo(RemoteProject):
    major_version = 'v1'
    remote = 'https://github.com/akeneo/pim-community-standard.git'

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader --no-scripts'.format(self.builddir),]
