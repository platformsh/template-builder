from .remote import RemoteProject
import json
from collections import OrderedDict

class Akeneo(RemoteProject):
    major_version = 'v4'
    remote = 'https://github.com/akeneo/pim-community-standard.git'

    @property
    def update(self):

        def akeneo_modify_composer(composer):
            """
            akeneo/pim-community-standard requires PHP 7.4, but it's dependency ocramius/package-versions has a complex
            requirement set.  1.5.1 is the only version I could find that works on Composer 2 and PHP 7.4, but it needs
            to be faked out with a platform version of 7.3 despite working on 7.4.  This is what happens when packages
            are needlessly and pointlessly aggressive in dropping old version support.
            """

            composer['require']['ocramius/package-versions'] = "1.5.1"

            return composer

        return super(Akeneo, self).update + [
            'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            (self.modify_composer, [akeneo_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader --no-scripts'.format(self.builddir) + ' '.join(self.composer_defaults()),
                'cd {0} && composer update'.format(self.builddir) + ' '.join(self.composer_defaults()),
                'cd {0} && composer require --dev psr/cache ^1.0'.format(self.builddir) + ' '.join(self.composer_defaults()),
                ]
