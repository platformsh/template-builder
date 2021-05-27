from . import BaseProject
import subprocess
import packaging.version

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

    def init(self):
        super(RemoteProject, self).init()
        subprocess.call(["git", "remote", "add", "project", self.remote], cwd=self.builddir)

    def update(self):
        subprocess.call(["git", "checkout", "master"], cwd=self.builddir)
        subprocess.call(["git", "fetch", "--all", "--depth=2"], cwd=self.builddir)
        subprocess.call(["git", "fetch", "--all", "--tags"], cwd=self.builddir)        
        if hasattr(self, 'major_version'):
            latest_tag = self.latest_tag()
            print("Merging from upstream tag: {0}".format(latest_tag))
            subprocess.call(["git", "merge", "--allow-unrelated-histories", "-X", "theirs", "--squash", latest_tag], cwd=self.builddir)
        elif hasattr(self, 'upstream_branch'):
            subprocess.call(["git", "merge", "--allow-unrelated-histories", "-X", "theirs", "--squash", f"project/{self.upstream_branch}"], cwd=self.builddir)
        else:
            raise AttributeError(
                'Each RemoteProject subclass must contain either a major_version or upstream_branch class attribute.')

        # Do this last so it picks up all changes from above.
        self.package_update()

    def latest_tag(self):
        """
        :return: string The version number of the most up to date tag matching the current major version.
        """
        all_tags = subprocess.check_output(["git", "tag"], cwd=self.builddir).decode(
            'utf-8').splitlines()

        tags = [tag for tag in all_tags if tag.startswith(self.major_version) and 'beta' not in tag and 'alpha' not in tag]
        # If there are no proper releases, search again but allow pre-release versions this time.
        # @todo If the project is hosted on GitHub, a better approach would be to check the GitHub API to see what
        # is marked as the latest release.
        if not tags:
            tags = [tag for tag in all_tags if tag.startswith(self.major_version)]

        tags.sort(key=lambda x: packaging.version.parse(x), reverse=True)

        tag = next(iter(tags), None)

        if tag == None:
            raise Exception('No upstream tag found to merge from.')

        return tag
