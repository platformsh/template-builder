import os.path
import json
from collections import OrderedDict
from . import BaseProject
from .remote import RemoteProject


class Wordpress_vanilla(BaseProject):
    remote = 'https://wordpress.org/latest'
    install_dir = 'wordpress'

    @property
    def platformify(self):
        return super(Wordpress_vanilla, self).platformify + [
            # Install WordPress
            'cd {0} && curl {1} -o {2}.tar.gz'.format(self.builddir, self.remote, self.install_dir),
            # Release the tar and cleanup.
            'cd {0} && tar -xvf {1}.tar.gz && rm {1}.tar.gz'.format(self.builddir, self.install_dir),
        ]

class Wordpress_bedrock(RemoteProject):
    major_version = '1'
    remote = 'https://github.com/roots/bedrock.git'

    @property
    def platformify(self):
        return super(Wordpress_bedrock, self).platformify + [
            'cd {0} && rm -rf .circleci && rm -rf .github'.format(self.builddir),
            'cd {0} && composer update --ignore-platform-reqs'.format(self.builddir),
        ]

class Wordpress_woocommerce(RemoteProject):
    major_version = '1'
    remote = 'https://github.com/roots/bedrock.git'

    @property
    def platformify(self):
        return super(Wordpress_woocommerce, self).platformify + [
            'cd {0} && rm -rf .circleci && rm -rf .github'.format(self.builddir),
            'cd {0} && composer require wpackagist-plugin/woocommerce wpackagist-plugin/jetpack --ignore-platform-reqs'.format(self.builddir),
        ]

class Wordpress_composer(RemoteProject):
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

        return super(Wordpress_composer, self).platformify + [
            (self.modify_composer, [wp_modify_composer]),
            'cd {0} && composer update --ignore-platform-reqs'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader wp-cli/wp-cli-bundle psy/psysh --ignore-platform-reqs'.format(self.builddir),
        ]
