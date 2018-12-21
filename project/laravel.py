from .remote import RemoteProject


class Laravel(RemoteProject):
    tag = 'v5.7.15'
    remote = 'https://github.com/laravel/laravel.git'

    @property
    def platformify(self):
        return super(Laravel, self).platformify + [
            'cd {0} /build && composer require platformsh/laravel-bridge'.format(
                self.builddir)
        ]
