from .remote import RemoteProject


class Sculpin(RemoteProject):
    major_version = '3'
    remote = 'https://github.com/sculpin/sculpin-blog-skeleton.git'

    @property
    def platformify(self):
        return super(Sculpin, self).platformify + [
            'cd {0} && composer config allow-plugins.sculpin/sculpin-theme-composer-plugin true --no-plugins '.format(self.builddir),
        ]
