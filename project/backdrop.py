from . import BaseProject

class Backdrop(BaseProject):
    version = '1.14.1'

    @property
    def update(self):
        return super(Backdrop, self).update + [
            "wget https://github.com/backdrop/backdrop/archive/{0}.tar.gz && tar xzvf {0}.tar.gz -C {"
            "1}".format(self.version, self.builddir),
            "rm {0}.tar.gz".format(self.version),
            "rm {0}web || true".format(self.version),
            "mv {0}backdrop-{1} {0}web".format(self.builddir, self.version),
        ]
