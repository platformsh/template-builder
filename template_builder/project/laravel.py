from .remote import RemoteProject

import subprocess

class Laravel(RemoteProject):
    major_version = 'v8'
    remote = 'https://github.com/laravel/laravel.git'

    @property
    def platformify(self):
        if 'remote' == self.location:
            super(Laravel, self).platformify()
            subprocess.call(["composer", "require", "platformsh/laravel-bridge"] + self.composer_defaults(), cwd=self.builddir)
        else:
            return super(Laravel, self).platformify + [
                'cd {0} && composer require platformsh/laravel-bridge' + ' '.join(self.composer_defaults())
            ]
