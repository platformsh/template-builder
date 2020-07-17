from .remote import RemoteProject


class PrestaShop(RemoteProject):
    major_version = '1.7'
    remote = 'https://github.com/PrestaShop/PrestaShop.git'

    @property
    def platformify(self):
        return super(PrestaShop, self).platformify + [
            'cd {0} && composer require platformsh/PrestaShop-bridge'.format(self.builddir),
        ]
