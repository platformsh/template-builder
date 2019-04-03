from . import BaseProject
import subprocess

class RemoteProject(BaseProject):
    '''
    Base class for projects that need to synchronize code with an upstream source.

    Projects that are based on a remote source that we then modify should use this
    base class instead.

    Projects extending this class MUST define the following class attributes:
    - `remote`, which is a Git URL to the upstream source.
    - `major_version`, which is the prefix of legal tags that can be merged from.
        So "5" will always to the most recent 5.y.z tag, "v3.4" will update to the latest
        "v.3.4.z" tag, etc.
    - OR `upstream_branch`, which specifies the tag or branch in the `remote` repository
        from which to pull. (If both are defined, `major_version` take precedence.)
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

        if hasattr(self, 'major_version'):
            def merge_from_upstream_tag():
                latest_tag = self.latest_tag()
                subprocess.check_output('cd {0} && git merge --allow-unrelated-histories -X theirs --squash {1}'.format(
                self.builddir, latest_tag), shell=True)
            actions.append(merge_from_upstream_tag)
        elif hasattr(self, 'upstream_branch'):
            actions.append(
                'cd {0} && git merge --allow-unrelated-histories -X theirs --squash project/{1}'.format(
                    self.builddir, self.upstream_branch))
        else:
            raise AttributeError(
                'Each RemoteProject subclass must contain either a major_version or upstream_branch class attribute.')

        # Do this last so it picks up all changes from above.
        actions.extend(self.packageUpdateActions())

        return actions

    def latest_tag(self):
        """
        :return: string The version number of the most up to date tag matching the current major version.
        """
        tags = subprocess.check_output('cd {0} && git tag'.format(self.builddir), shell=True).decode('utf-8').splitlines()
        tags = [tag for tag in tags if tag.startswith(self.major_version)]
        tags.sort(key=lambda s: [u for u in s.split('.')], reverse=True)

        tag = next(iter(tags), None)

        if tag == None:
            raise Exception('No upstream tag found to merge from')

        return tag
