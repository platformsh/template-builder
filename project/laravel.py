from .remote import RemoteProject


class Laravel(RemoteProject):
    upstream_tag = 'v5.7.19'
    remote = 'https://github.com/laravel/laravel.git'

    @property
    def platformify(self):
        return super(Laravel, self).platformify + [
            'cd {0} /build && composer require platformsh/laravel-bridge'.format(
                self.builddir)
        ]
