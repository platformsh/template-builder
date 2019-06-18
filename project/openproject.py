from .remote import RemoteProject


class Openproject(RemoteProject):
    upstream_branch = 'stable/8'
    remote = 'https://github.com/opf/openproject-ce.git'

    @property
    def platformify(self):
        return super(Openproject, self).platformify + [
            'cd {0}/build && bundle install --deployment --without mysql2 sqlite development test therubyracer docker'.format(
                self.builddir)
        ]
