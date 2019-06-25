from .remote import RemoteProject


class Pimcore5(RemoteProject):
    major_version = 'v1'
    remote = 'https://github.com/pimcore/skeleton.git'

    @property
    def platformify(self):
        return super(Pimcore5, self).platformify + [
            'cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm  --no-scripts'.format(self.builddir), ]
