from . import BaseProject
from .remote import RemoteProject
import json
from collections import OrderedDict


class Drupal7_vanilla(BaseProject):
    version = '7.65'

    @property
    def update(self):
        return super(Drupal7_vanilla, self).update + [
            "wget -qO- https://ftp.drupal.org/files/projects/drupal-{0}.tar.gz | tar xzv --transform 's/^drupal-{0}/docroot/' -C {1}".format(
                self.version, self.builddir),
        ]


class Drupal8(RemoteProject):
    upstream_branch = '8.x'
    remote = 'https://github.com/drupal-composer/drupal-project.git'

    @property
    def platformify(self):
        return super(Drupal8, self).platformify + [
            'cd {0} /build && composer require platformsh/config-reader drupal/redis'.format(
                self.builddir)
        ]

class Govcms8(RemoteProject):
    upstream_branch = '8.x'
    remote = 'https://github.com/drupal-composer/drupal-project.git'

    @property
    def platformify(self):

        def govcms8_add_installer_paths():
            """
            govcms9 requires more Composer modification than can be done
            with the Composer command line.  This function modifies the composer.json
            file as raw JSON instead.
            """
            with open('{0}/composer.json'.format(self.builddir), 'r') as f:
                # The OrderedDict means that the property orders in composer.json will be preserved.
                composer = json.load(f, object_pairs_hook=OrderedDict)

            composer['extra']['installer-types'] = ['bower-asset', 'npm-asset']
            composer['extra']['installer-paths']['web/libraries/{$name}'] = ['type:drupal-library', 'type:bower-asset', 'type:npm-asset']

            with open('{0}/composer.json'.format(self.builddir), 'w') as out:
                json.dump(composer, out, indent=2)

        return super(Govcms8, self).platformify + [
            (govcms8_add_installer_paths, []),
            'cd {0} && composer require govcms/govcms'.format(self.builddir)
        ]
