from .remote import RemoteProject


class Typo3(RemoteProject):
    major_version = 'v1'
    remote = 'https://github.com/TYPO3/TYPO3.CMS.BaseDistribution.git'

    @property
    def platformify(self):
        return super(Typo3, self).platformify + [
            'cd {0} && composer update --no-scripts && composer require platformsh/config-reader'.format(self.builddir),
        ]
