from project import RemoteProject


class Laravel(RemoteProject):
    major_version = 'v5'
    remote = 'https://github.com/laravel/laravel.git'

    @property
    def platformify(self):
        return super(Laravel, self).platformify + [
            'cd {0} && composer require platformsh/laravel-bridge'.format(self.builddir),
            'cd {0} && rm readme.md'.format(self.builddir),
        ]
