from .remote import RemoteProject


class Typo3(RemoteProject):
    major_version = 'v10'
    remote = 'https://github.com/TYPO3/TYPO3.CMS.BaseDistribution.git'

    @property
    def platformify(self):
        return super(Typo3, self).platformify + [
            'cd {0} && composer config extra.typo3/cms.web-dir public'.format(self.builddir),
            'cd {0} && composer update --no-scripts'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && composer require typo3/cms-introduction platformsh/config-reader pixelant/pxa-lpeh'.format(self.builddir) + self.composer_defaults(),
        ]
