from . import BaseProject


class RemoteProject(BaseProject):
    '''Base class synchronizing code with remote source tree, each
    subclass must contain aither `upstream_tag` or `upstream_branch`
    class attribute.
    '''

    @property
    def init(self):
        return super(RemoteProject, self).init + [
            'cd {0} && git remote add project {1}'.format(
                self.builddir, self.remote)
        ]

    @property
    def update(self):
        actions = [
            'cd {0} && git checkout master'.format(self.builddir),
            'cd {0} && git fetch --all --depth=2'.format(self.builddir),
            'cd {0} & git fetch --all --tags'.format(self.builddir),
        ]

        if hasattr(self, 'upstream_tag'):
            actions.append(
                'cd {0} && git merge --allow-unrelated-histories -X theirs --squash {1}'.format(
                    self.builddir, self.upstream_tag))
        elif hasattr(self, 'upstream_branch'):
            actions.append(
                'cd {0} && git merge --allow-unrelated-histories -X theirs --squash project/{1}'.format(
                    self.builddir, self.upstream_branch))
        else:
            raise AttributeError(
                'Each RemoteProject subclass must contain either a upstream_tag or upstream_branch class attribute.')
        actions.append('cd {0} & & composer update - -prefer-dist - -ignore-platform-reqs --no-interaction'.format(
            self.builddir)
        )
