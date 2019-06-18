from .remote import RemoteProject


class OpenProject(RemoteProject):
    upstream_branch = 'stable/8'
    remote = 'https://github.com/opf/openproject-ce.git'
"""
    @property
    def platformify(self):
        return super(Laravel, self).platformify + [
            'cd {0} /build && composer require platformsh/laravel-bridge'.format(
                self.builddir)
        ]
"""
