from .remote import RemoteProject

class Sylius(RemoteProject):
    major_version = 'v1.11'
    remote = 'https://github.com/Sylius/Sylius-Standard.git'

    @property
    def platformify(self):
        return super(Sylius, self).platformify + [
            'cd {0} && rm -rf .github',
        ]