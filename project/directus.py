import os
from os import walk
from . import BaseProject

class Directus(BaseProject):

    @property
    def platformify(self):

        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TEMPLATEDIR = os.path.join(ROOTDIR, 'templates')
        extensions = "{}/directus/files/extensions/".format(TEMPLATEDIR)

        # Include .gitkeeps for extensions/uploads directories.
        gitkeeps = []
        for subdir in os.listdir(extensions):
            gitkeeps.append('touch {0}/directus/files/extensions/{1}/.gitkeep'.format(TEMPLATEDIR, subdir))
        gitkeeps.append('touch {0}/directus/files/uploads/.gitkeep'.format(TEMPLATEDIR))

        return gitkeeps + super(Directus, self).platformify
