from .remote import RemoteProject
import json
from collections import OrderedDict

class Akeneo(RemoteProject):
    major_version = 'v3'
    remote = 'https://github.com/akeneo/pim-community-standard.git'

    @property
    def update(self):

        def akeneo_modify_composer():
            """
            akeneo/pim-community-standard requires PHP 7.2, but it's dependency ocramius/package-versions requires 7.3 with the previous
            default configuration (1.5.1). This resolves that problem.
            """
            with open('{0}/composer.json'.format(self.builddir), 'r') as f:
                # The OrderedDict means that the property orders in composer.json will be preserved.
                composer = json.load(f, object_pairs_hook=OrderedDict)

            composer['require']['ocramius/package-versions'] = ">=1.4.0 <1.5.0"

            with open('{0}/composer.json'.format(self.builddir), 'w') as out:
                json.dump(composer, out, indent=4)

        return super(Akeneo, self).update + [
            (akeneo_modify_composer, [])
        ]

    @property
    def platformify(self):

        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader --no-scripts --ignore-platform-reqs'.format(self.builddir),]
