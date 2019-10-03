import json
from collections import OrderedDict

from .remote import RemoteProject


class Wordpress(RemoteProject):
    major_version = '5'
    remote = 'https://github.com/johnpbloch/wordpress.git'

    @property
    def platformify(self):
        return super(Wordpress, self).platformify + [
            'cd {0} && composer update --ignore-platform-reqs'.format(self.builddir),
        ]
