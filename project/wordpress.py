import sys
import os
import os.path
from pprint import pprint
import json
from collections import OrderedDict
from . import BaseProject
from .remote import RemoteProject
from .composer import ComposerProject

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
            # Move Platform.sh files into `wordpress`.
            'cd {0} && mv wp-config.php {1} && mv wp-cli.yml {1}'.format(self.builddir, self.install_dir),
        ]


# @todo
class WordPressComposerBase(ComposerProject):

    # Run through our list of dependencies that should be unpinned as defined in @see unPinDependencies
    def wp_modify_composer(self, composer, dependencies=[]):
        composer = super(WordPressComposerBase, self).wp_modify_composer(dependencies)
        # All composer-based WordPress repositories will need wpackagist.org added
        composer['repositories'] = [
            {
                "type": "composer",
                "url": "https://wpackagist.org"
            }
        ]

        return composer

class Wordpress_bedrock(WordPressComposerBase):
    major_version = '1'
    remote = 'https://github.com/roots/bedrock.git'
    unPinDependencies = ['roots/wordpress']

    @property
    def _platformify(self):
        def wp_modify_composer(composer):
            return super(Wordpress_bedrock, self).wp_modify_composer(composer, self.unPinDependencies)

        return super(Wordpress_bedrock, self)._platformify + [
            (self.modify_composer, [wp_modify_composer]),
            'cd {0} && rm -rf .circleci && rm -rf .github'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader wp-cli/wp-cli-bundle psy/psysh'.format(
                self.builddir) + self.composer_defaults(),
            'cd {0} && composer update'.format(self.builddir) + self.composer_defaults(),
        ]


class Wordpress_woocommerce(WordPressComposerBase):
    unPinDependencies = [
        'roots/wordpress',
        'wpackagist-plugin/woocommerce',
        'wpackagist-plugin/jetpack'
    ]
    major_version = '1'
    remote = 'https://github.com/roots/bedrock.git'

    @property
    def _platformify(self):
        def wp_modify_composer(composer):
            return super(Wordpress_woocommerce, self).wp_modify_composer(composer, self.unPinDependencies)

        return super(Wordpress_woocommerce, self)._platformify + [
            (self.modify_composer, [wp_modify_composer]),
            'cd {0} && rm -rf .circleci && rm -rf .github'.format(self.builddir),
            'cd {0} && composer require wpackagist-plugin/woocommerce wpackagist-plugin/jetpack'.format(
                self.builddir) + self.composer_defaults(),
        ]


class Wordpress_composer(WordPressComposerBase):
    major_version = '5'
    remote = 'https://github.com/johnpbloch/wordpress.git'
    unPinDependencies = ['johnpbloch/wordpress-core']

    @property
    def _platformify(self):

        def require_default_wppackages():
            # WordPress comes with a few default themes and plugins. Those packages are not
            #   automatically added via Composer, so they aren't really packages like they should be.
            #   This becomes a problem when adding new themes/plugins, resulting in a nested wp-content dir.
            #   The upstream recommendation seems to be to add them explicitly via Composer.
            #
            #   Issue: https://github.com/platformsh-templates/wordpress-composer/issues/7
            #   Recommendation: https://github.com/johnpbloch/wordpress-core/issues/5
            root = 'wordpress/wp-content/'
            namespace = {
                "themes": "wpackagist-theme",
                "plugins": "wpackagist-plugin"
            }

            if os.path.exists(self.builddir + root):
                defaultPackages = []

                # Find default themes and plugins subdirectories.
                installerPaths = [x for x in os.listdir(self.builddir + root) if
                                  os.path.isdir(self.builddir + root + x)]
                for path in installerPaths:
                    installerPath = '{0}{1}{2}/'.format(self.builddir, root, path)
                    # For each subdirectory, require the package, adding the right namespace to it.
                    [defaultPackages.append('{0}/{1}'.format(namespace[path], x)) for x in os.listdir(installerPath) if
                     os.path.isdir(installerPath + x)]

                return ' '.join(defaultPackages)

        def wp_modify_composer(composer):
            composer = super(Wordpress_composer, self).wp_modify_composer(composer, self.unPinDependencies)
            # In order to both use the Wordpress default install location `wordpress` and
            # supply the Platform.sh-specific `wp-config.php` to that installation, a script is
            # added to the upstream composer.json to move that config file during composer install.
            composer['scripts'] = {
                'subdirComposer': [
                    "cp wp-config.php wordpress/ && rm -rf wordpress/wp-content/wp-content"
                ],
                'post-install-cmd': "@subdirComposer"
            }

            composer['extra'] = {
                'installer-paths': {
                    r'wordpress/wp-content/plugins/{$name}': ['type:wordpress-plugin'],
                    r'wordpress/wp-content/themes/{$name}': ['type:wordpress-theme'],
                    r'wordpress/wp-content/mu-plugins/{$name}': ['type:wordpress-muplugin'],
                }
            }

            return composer

        return super(Wordpress_composer, self)._platformify + [
            (self.modify_composer, [wp_modify_composer]),
            'cd {0} && composer update'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && composer require platformsh/config-reader wp-cli/wp-cli-bundle psy/psysh'.format(
                self.builddir) + self.composer_defaults(),
            'cd {0} && composer require {1}'.format(self.builddir,
                                                    require_default_wppackages()) + self.composer_defaults(),
        ]
