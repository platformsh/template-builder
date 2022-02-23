from .remote import RemoteProject

class Sylius(RemoteProject):
    major_version = 'v1.11'
    remote = 'https://github.com/Sylius/Sylius-Standard.git'

    @property
    def platformify(self):
        return [
            'cd {0} && cp README.md README_upstream.md'.format(self.builddir),
            'cd {0} && ls -a'.format(self.builddir),
            'cd {0} && rm -rf .github'.format(self.builddir),
            'cd {0} && composer require platformsh/symfonyflex-bridge'.format(self.builddir) + self.composer_defaults(),
        ] + super(Sylius, self).platformify
