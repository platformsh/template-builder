import json
from collections import OrderedDict

from .remote import RemoteProject


class Wordpress(RemoteProject):
    major_version = '5'
    remote = 'https://github.com/johnpbloch/wordpress.git'

    @property
    def platformify(self):
        def wp_modify_composer(composer):
            # In order to both use the Wordpress default install location `wordpress` and
            # supply the Platform.sh-specific `wp-config.php` to that installation, a script is
            # added to the upstream composer.json to move that config file during composer install.
            composer['scripts'] = {
                'copywpconfig': [
                    "cp wp-config.php wordpress/"
                ],
                'post-install-cmd': "@copywpconfig"
            }

            composer['extra'] = {
                'installer-paths': {
                    r'wordpress/wp-content/plugins/{$name}': ['type:wordpress-plugin'],
                    r'wordpress/wp-content/themes/{$name}': ['type:wordpress-theme'],
                    r'wordpress/wp-content/mu-plugins/{$name}': ['type:wordpress-muplugin'],
                }
            }

            composer['repositories'] = [
                {
                    "type": "composer",
                    "url": "https://wpackagist.org"
                }
            ]
            return composer

        return super(Wordpress, self).platformify + [
            (self.modify_composer, [wp_modify_composer]),
            'cd {0} && composer update --ignore-platform-reqs'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader --ignore-platform-reqs'.format(self.builddir),
            # WP-CLI Composer recommendations (https://make.wordpress.org/cli/handbook/guides/installing/#installing-via-composer).
            'cd {0} && composer require wp-cli/wp-cli-bundle'.format(self.builddir),
            'cd {0} && composer require symfony/event-dispatcher'.format(self.builddir),
            'cd {0} && composer require symfony/lock'.format(self.builddir),
            'cd {0} && composer require illuminate/view'.format(self.builddir),
            'cd {0} && composer require symfony/yaml'.format(self.builddir),
            'cd {0} && composer require psy/psysh'.format(self.builddir),
            'cd {0} && composer require symfony/dependency-injection'.format(self.builddir),
            'cd {0} && composer require symfony/dependency-injection'.format(self.builddir),
            
        ]
