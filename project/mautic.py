import json
from collections import OrderedDict

from .remote import RemoteProject

class Mautic(RemoteProject):
    major_version = '2'
    remote = 'https://github.com/mautic/mautic.git'


    @property
    def update(self):
        actions = super(Mautic, self).update

        def mautic_fix_composer():
            """
            """
            with open('{0}/composer.json'.format(self.builddir), 'r') as f:
                # The OrderedDict means that the property orders in composer.json will be preserved.
                composer = json.load(f, object_pairs_hook=OrderedDict)

            # Remove the git hooks that Mautic wants to install for enforcing code style,
            # as those are useless during deployment.
            composer['scripts']['post-install-cmd'] = \
                [s for s in composer['scripts']['post-install-cmd'] if 'php -r' not in s]
            composer['scripts']['post-update-cmd'] = \
                [s for s in composer['scripts']['post-install-cmd'] if 'php -r' not in s]

            # composer update will pull in Twig 2 instead of Twig 1, which is declared
            # compatible according to the composer.json files but really isn't. It will crash
            # when compiling templates. So force Twig 1 here, before the first composer update
            # runs.  It also cannot use a require statement because this change must be made
            # before composer runs, even once, or it will still run with the scripts above
            # enabled.
            # The config reader is added here at the same time mainly for performance.
            composer['require']['twig/twig'] = "~1.42"
            composer['require']['platformsh/config-reader'] = "^2.3"

            composer['config']['platform']['php'] = '7.2.30'

            with open('{0}/composer.json'.format(self.builddir), 'w') as out:
                json.dump(composer, out, indent=2)

        actions.insert(4, (mautic_fix_composer, []))

        return actions
