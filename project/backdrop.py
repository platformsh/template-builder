from . import BaseProject
import os.path
from glob import glob
from . import TEMPLATEDIR

class Backdrop(BaseProject):
    version = '1.21.1'

    @property
    def update(self):
        return super(Backdrop, self).update + [
            "wget https://github.com/backdrop/backdrop/archive/{0}.tar.gz && tar xzvf {0}.tar.gz -C {1}".format(self.version, self.builddir),
            "rm {0}.tar.gz".format(self.version),
            "rm -rf {0}web || true".format(self.builddir),
            "mv {0}backdrop-{1} {0}web".format(self.builddir, self.version),
        ]

    @property
    def platformify(self):
        """
        This method needs to be overridden because the patch file for Backdrop is rolled against its app root; but the
        app root is the subdir `web` of the builddir, not the builddir.

        The only change here is the directory that patches are applied from.
        """
        actions = ['rsync -aP {0} {1}'.format(
            os.path.join(TEMPLATEDIR, self.name, 'files/'),  self.builddir
        )]
        patches = glob(os.path.join(TEMPLATEDIR, self.name, "*.patch"))
        for patch in patches:
            actions.append('cd {0}/web && patch -p1 < {1}'.format(
                self.builddir, patch)
            )

        # In some cases the package updater needs to be run after we've platform-ified the
        # template, so run it a second time. Worst case it's a bit slower to build but doesn't
        # hurt anything.
        actions.extend(self.package_update_actions())

        return actions
