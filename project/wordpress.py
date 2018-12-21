import json
from collections import OrderedDict

from .remote import RemoteProject


class Wordpress(RemoteProject):
    tag = '5.0.1'
    remote = 'https://github.com/johnpbloch/wordpress.git'

    @property
    def platformify(self):
        def wp_add_installer_paths():
            with open('{0}/composer.json'.format(self.builddir), 'r') as f:
                composer = json.load(f, object_pairs_hook=OrderedDict)

            composer['extra'] = {
                'wordpress-install-dir': 'web/wp',
                'installer-paths': {
                    r'web/wp-content/plugins/{$name}': ['type:wordpress-plugin'],
                    r'web/wp-content/themes/{$name}': ['type:wordpress-theme'],
                    r'web/wp-content/mu-plugins/{$name}': ['type:wordpress-muplugin'],
                }
            }

            with open('{0}/composer.json'.format(self.builddir), 'w') as out:
                json.dump(composer, out, indent=2)

        return [  # The initial composer update put files in the wrong place, so clean that up.
            'rm -rf {0}/wordpress'.format(self.builddir)
        ] + super(Wordpress, self).platformify + [
            (wp_add_installer_paths, []),
            'cd {0} && composer update'.format(self.builddir),
        ]
