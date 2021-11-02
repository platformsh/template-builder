from .remote import RemoteProject

import subprocess

class Laravel(RemoteProject):
    major_version = 'v8'
    remote = 'https://github.com/laravel/laravel.git'

    def platformify(self):
        super(Laravel, self).platformify()
        subprocess.call(["composer", "require", "platformsh/laravel-bridge"] + self.composer_defaults(), cwd=self.builddir)
