import os.path
from glob import glob

ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATEDIR = os.path.join(ROOTDIR, 'templates')


class BaseProject(object):
    '''
    Base class storing task actions.

    Each @property method corresponds to a DoIt task of the same name.
    In practice, platformify is usually the only one that most projects will need
    to override.
    '''

    def __init__(self, name):
        self.name = name
        self.builddir = os.path.join(TEMPLATEDIR, self.name, 'build/')

    @property
    def cleanup(self):
        return ['rm -rf {0}'.format(self.builddir)]

    @property
    def init(self):
        if hasattr(self, 'github_name'):
            name = self.github_name
        else:
            name = self.name.replace('_', '-')
        return ['git clone git@github.com:platformsh/template-{0}.git {1}'.format(
            name, self.builddir)
        ]

    @property
    def update(self):
        return ['cd {0} && git checkout master && git pull --prune'.format(
            self.builddir)
        ]

    @property
    def platformify(self):
        """
        The default implementation of this method will
        1) Copy the contents of the files/ directory in the project over the
           application, replacing what's there.
        2) Apply any *.patch files found in the project directory, in alphabetical order.

        Individual projects may expand on these tasks as needed.
        """
        actions = ['rsync -aP {0} {1}'.format(
            os.path.join(TEMPLATEDIR, self.name, 'files/'),  self.builddir
        )]
        patches = glob(os.path.join(TEMPLATEDIR, self.name, "*.patch"))
        for patch in patches:
            actions.append('cd {0} && patch -p1 < {1}'.format(
                self.builddir, patch)
            )
        return actions

    @property
    def branch(self):
        return [
            'cd {0} && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;'.format(
                self.builddir),
            'cd {0} && git checkout -b update'.format(self.builddir),
            'cd {0} && git add -A && git commit -m "Update to latest upstream"'.format(
                self.builddir),
        ]

    @property
    def push(self):
        return ['cd {0} && git checkout update && git push --force -u origin update'.format(
            self.builddir)
        ]
