from . import BaseProject
import subprocess
import packaging.version

class NoTagsException(Exception):
    pass

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
        if 'local' == self.location:
            return super(RemoteProject, self).init + [
                'cd {0} && git remote add project {1}'.format(
                    self.builddir, self.remote)
            ]
        else:
            super(RemoteProject, self).init()
            subprocess.call(["git", "remote", "add", "project", self.remote], cwd=self.builddir)

    @property
    def update(self):
        # @todo well, this is ugly as sin
        if 'remote' == self.location:
            subprocess.call(["git", "checkout", "master"], cwd=self.builddir)
            subprocess.call(["git", "fetch", "--all", "--depth=2"], cwd=self.builddir)
            subprocess.call(["git", "fetch", "--all", "--tags"], cwd=self.builddir)
            try:
                if hasattr(self, 'major_version'):
                    latest_tag = self.latest_tag()
                    print("Merging from upstream tag: {0}".format(latest_tag))
                    subprocess.call(
                        ["git", "merge", "--allow-unrelated-histories", "-X", "theirs", "--squash", latest_tag],
                        cwd=self.builddir)
                elif hasattr(self, 'upstream_branch'):
                    subprocess.call(["git", "merge", "--allow-unrelated-histories", "-X", "theirs", "--squash",
                                     "project/{0}".format(self.upstream_branch)], cwd=self.builddir)
                else:
                    raise AttributeError(
                        'Each RemoteProject subclass must contain either a major_version or upstream_branch class attribute.')
            except NoTagsException:
                pass  # do we care if there are no tags?

            # Do this last so it picks up all changes from above.
            self.package_update()
        else:
            actions = [
                'cd {0} && git checkout master'.format(self.builddir),
                'cd {0} && git fetch --all --depth=2'.format(self.builddir),
                'cd {0} && git fetch --all --tags'.format(self.builddir),
                # Remove working directory files when updating from upstream, so that deletions get picked up.
                # Disabled, because it was breaking Magento updates. Even though it was added to avoid breaking Magento updates.
                # 'cd {0} &&  (find . -maxdepth 1 -not \( -path ./.git -o -path . \) -exec rm -rf {{}} \;)'.format(self.builddir),
            ]

            if hasattr(self, 'major_version'):
                def merge_from_upstream_tag():
                    latest_tag = self.latest_tag()
                    print("Merging from upstream tag: {0}".format(latest_tag))
                    subprocess.check_output(
                        'cd {0} && git merge --allow-unrelated-histories -X theirs --squash {1}'.format(
                            self.builddir, latest_tag), shell=True)

                actions.append(merge_from_upstream_tag)
            elif hasattr(self, 'upstream_branch'):
                print("Merging from upstream branch: {0}".format(self.upstream_branch))
                actions.append(
                    'cd {0} && git merge --allow-unrelated-histories -X theirs --squash project/{1}'.format(
                        self.builddir, self.upstream_branch))
            else:
                raise AttributeError(
                    'Each RemoteProject subclass must contain either a major_version or upstream_branch class attribute.')

            # Do this last so it picks up all changes from above.
            actions.extend(self.package_update_actions())

            return actions

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
            raise NoTagsException('No upstream tag found to merge from.')

        return tag
