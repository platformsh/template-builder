from .remote import RemoteProject
import json
from collections import OrderedDict

class Akeneo(RemoteProject):
    major_version = 'v5.0'
    remote = 'https://github.com/akeneo/pim-community-standard.git'

    @property
    def update(self):

        def akeneo_modify_composer(composer):
            """
            akeneo/pim-community-standard requires PHP 7.3, but it's dependency ocramius/package-versions requires 7.4
            in its latest version. This resolves that problem.
            """

            #composer['require']['ocramius/package-versions'] = "1.5.1"

            return composer

        return super(Akeneo, self).update + [
            'cd {0} && composer config platform.php 7.4'.format(self.builddir),
            (self.modify_composer, [akeneo_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader --no-scripts'.format(self.builddir) + self.composer_defaults(),]
