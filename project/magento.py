from .composer import ComposerProject


class Magento2ce(ComposerProject):
    major_version = '2.3'
    remote = 'https://github.com/magento/magento2.git'

    @property
    @ComposerProject.composer_platformify
    def platformify(self):
        return super(Magento2ce, self).platformify
