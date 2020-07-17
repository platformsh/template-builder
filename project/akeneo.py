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
            akeneo/pim-community-standard requires PHP 7.2, but it's dependency ocramius/package-versions requires 7.3
            with the previous default configuration (1.5.1). This resolves that problem.
            """

            composer['require']['ocramius/package-versions'] = ">=1.4.0 <1.5.0"

            return composer

        return super(Akeneo, self).update + [
            (self.modify_composer, [akeneo_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader --no-scripts --ignore-platform-reqs'.format(self.builddir),]
