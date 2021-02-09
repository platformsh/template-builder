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
            requirement set.  2.1.0 is the only version I could find that works on Composer 2 and PHP 7.4, but it needs
            7.4.7 specifically and a platform.php value of just 7.4 isn't enough.  This combination seems to work.
            Akeneo doesn't work with PHP 8 yet, because it depends on a version of Doctrine that is pinned to only
            support PHP 7, despite Doctrine and package-versions being written by the same person.
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
                'cd {0} && composer require platformsh/config-reader --no-scripts'.format(self.builddir) + self.composer_defaults(),]
