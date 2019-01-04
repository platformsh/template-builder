from . import BaseProject


class RemoteProject(BaseProject):
    '''Base class synchronizing code with remote source tree, each
    subclass must contain aither `tag` or `update_branch` class attribute.
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

        if hasattr(self, 'tag'):
            actions.append(
                'cd {0} && git merge --allow-unrelated-histories -X theirs --squash {1}'.format(
                    self.builddir, self.tag))
        elif hasattr(self, 'update_branch'):
            actions.append(
                'cd {0} && git merge --allow-unrelated-histories -X theirs --squash project/{1}'.format(
                    self.builddir, self.update_branch))
        else:
            raise AttributeError(
                'Each RemoteProject subclass must contain either a tag or update_branch class attribute.')
        actions.append('cd {0} & & composer update - -prefer-dist - -ignore-platform-reqs --no-interaction'.format(
            self.builddir)
        )
