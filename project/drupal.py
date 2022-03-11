from . import BaseProject
from .remote import RemoteProject
import json
from collections import OrderedDict

class Drupal7_vanilla(BaseProject):
    version = '7.67'

    @property
    def update(self):
        return super(Drupal7_vanilla, self).update + [
            "wget https://ftp.drupal.org/files/projects/drupal-{0}.tar.gz && tar xzvf drupal-{0}.tar.gz -C {1}".format(self.version, self.builddir),
            "rm drupal-{0}.tar.gz".format(self.version),
            "rm -rf {0}public || true".format(self.builddir),
            "mv {0}drupal-{1} {0}public".format(self.builddir, self.version),
        ]


class Drupal8(RemoteProject):
    major_version = '8.9'
    remote = 'https://github.com/drupal/recommended-project.git'

    @property
    def platformify(self):
        return super(Drupal8, self).platformify + [
            # 'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults()
            'cd {0} && composer require platformsh/config-reader drush/drush:^10.6 drupal/console drupal/redis'.format(self.builddir)  + self.composer_defaults(),
            # 'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults()
        ]

class Drupal9(RemoteProject):
    # This can have a common base with Drupal 8 eventually, once modules are updated.
    major_version = "9.3"
    remote = 'https://github.com/drupal/recommended-project.git'

    @property
    def platformify(self):
        return super(Drupal9, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drush/drush drupal/redis'.format(self.builddir) + self.composer_defaults()
        ]

class Drupal8_multisite(Drupal8):
    pass

class Drupal8_opigno(Drupal8):
    major_version = '2'
    remote = 'https://bitbucket.org/opigno/opigno-composer.git'


class Drupal8_govcms8(RemoteProject):
    major_version = '1'
    remote = 'https://github.com/govCMS/govCMS8-project.git'

    @property
    def platformify(self):
       return super(Drupal8_govcms8, self).platformify + [
           # GovCMS comes with a pre-made lock file that pins symfony/filesystem at v4, but
           # drupal/console only works with the 3.x version, and therefore will fail.
           # It should work to remove the lock file first, but for some reason that is still failing.
           # For now, just skip installing console on GovCMS. I don't know if anyone uses it anyway.
           'cd {0} && composer require platformsh/config-reader drush/drush:^10.6 drupal/redis'.format(self.builddir) + self.composer_defaults(),
        ]
