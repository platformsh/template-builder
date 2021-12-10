from .composer import ComposerProject


class Typo3(ComposerProject):
    major_version = 'v10'
    remote = 'https://github.com/TYPO3/TYPO3.CMS.BaseDistribution.git'

    @property
    @ComposerProject.composer_platformify
    def platformify(self):
        def typo3_modify_composer(composer):
            # The TYPO3 docs recommend this order, but upstream places them in the opposite order.
            # This change appears to fix the error that was occurring in template-builder during
            # typo3cms install:fixfolderstructure.
            # See: https://docs.typo3.org/p/helhum/typo3-console/master/en-us/CommandReference/InstallFixfolderstructure.html#install-fixfolderstructure
            composer['scripts'] = {
                'typo3-cms-scripts': [
                    "typo3cms install:generatepackagestates",
                    "typo3cms install:fixfolderstructure"
                ]
            }

            composer['config']['platform']['php'] = "7.4"
            return composer

        return super(Typo3, self).platformify + [
            (self.modify_composer, [typo3_modify_composer]),
            'cd {0} && composer config extra.typo3/cms.web-dir public'.format(self.builddir),
            'cd {0} && composer update --no-scripts'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && psr/cache:^1.0 typo3/cms-introduction:~4.3.2 platformsh/config-reader pixelant/pxa-lpeh'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && composer update'.format(self.builddir) + self.composer_defaults(),
        ]
