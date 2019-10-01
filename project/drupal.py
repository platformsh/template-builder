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
            "rm {0}public || true".format(self.version),
            "mv {0}drupal-{1} {0}public".format(self.builddir, self.version),
        ]


class Drupal8(RemoteProject):
    upstream_branch = '8.x'
    remote = 'https://github.com/drupal-composer/drupal-project.git'

    @property
    def platformify(self):
        return super(Drupal8, self).platformify + [
            'cd {0} /build && composer require platformsh/config-reader drupal/redis --ignore-platform-reqs'.format(
                self.builddir)
        ]

class Drupal8_multisite(Drupal8):
    pass

class Drupal8_opigno(Drupal8):
    major_version = '2'
    remote = 'https://bitbucket.org/opigno/opigno-composer.git'


class Drupal8_govcms8(Drupal8):
    major_version = '8.x'
    remote = 'https://github.com/govCMS/govCMS8.git'


    @property
    def platformify(self):
        def govcms_remove_phing():
            """
            The default GovCMS8 composer.json file runs a phing task that copies the site
            within itself.  It's not clear why, but it's unnecessary. Skip that.
            """
            with open('{0}/composer.json'.format(self.builddir), 'r') as f:
                # The OrderedDict means that the property orders in composer.json will be preserved.
                composer = json.load(f, object_pairs_hook=OrderedDict)

            composer['scripts']['post-install-cmd'].remove('@composer push')
            composer['scripts']['post-update-cmd'].remove('@composer push')

            with open('{0}/composer.json'.format(self.builddir), 'w') as out:
                json.dump(composer, out, indent=2)

        return [(govcms_remove_phing, [])] + super(Drupal8, self).platformify
