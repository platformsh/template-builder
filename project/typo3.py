from .remote import RemoteProject


class Typo3(RemoteProject):
    major_version = 'v10'
    remote = 'https://github.com/TYPO3/TYPO3.CMS.BaseDistribution.git'

    @property
    def platformify(self):
        return super(Typo3, self).platformify + [
            'cd {0} && composer config extra.typo3/cms.web-dir public && composer update --no-scripts && composer require typo3/cms-introduction platformsh/config-reader pixelant/pxa-lpeh'.format(self.builddir),
        ]
