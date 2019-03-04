from . import BaseProject
from .remote import RemoteProject


class Drupal7_vanilla(BaseProject):
    version = '7.61'

    @property
    def update(self):
        return super(Drupal7_vanilla, self).update + [
            "wget -qO- https://ftp.drupal.org/files/projects/drupal-{0}.tar.gz | tar xzv --transform 's/^drupal-{0}/docroot/' -C {1}".format(
                self.version, self.builddir),
        ]


class Drupal8(RemoteProject):
    upstream_branch = '8.x'
    remote = 'https://github.com/drupal-composer/drupal-project.git'

class Govcms8(RemoteProject):
    upstream_branch = '8.x'
    remote = 'https://github.com/drupal-composer/drupal-project.git'
