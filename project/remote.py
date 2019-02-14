from . import BaseProject


class RemoteProject(BaseProject):
    '''
    Base class for projects that need to synchronize code with an upstream source.

    Projects that are based on a remote source that we then modify should use this
    base class instead.

    Projects extending this class MUST define the following class attributes:
    - `remote`, which is a Git URL to the upstream source.
    - either `upstream_tag` or `upstream_branch`, which specifies the tag or branch
        in the `remote` repository from which to pull. (If both are defined, `upstream_tag`
        take precedence.)

    Note that if using a tag, that means the project class will need to be updated
    every time there's a new upstream release.  C'est la vie.
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
            'cd {0} && git fetch --all --tags'.format(self.builddir),
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

        # Do this last so it picks up all changes from above.
        actions.extend(self.packageUpdateActions())

        return actions
