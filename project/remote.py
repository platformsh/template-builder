import subprocess

import packaging.version

from . import BaseProject


class RemoteProject(BaseProject):
    """
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
    """

    readMeFileName = "README"
    readMeFileExt = "md"
    readMeUpstreamFile = "_UPSTREAM"
    readMePSHFile = "_PSH"

    @property
    def init(self):
        return super(RemoteProject, self).init + [
            'cd {0} && git remote add project {1}'.format(
                self.builddir, self.remote)
        ]

    @property
    def update(self):
        actions = [
            # If we have a readme file from the template repository, rename it so we can bring it back later
            'cd {0} && if [[ -f "{1}.{2}" ]]; then echo "Moving {1}.{2} to {1}{3}.{2}"; mv "{1}.{2}" "{1}{3}.{2}"; fi;'
            .format(self.builddir, self.readMeFileName, self.readMeFileExt, self.readMePSHFile),
            'cd {0} && git checkout {1}'.format(self.builddir, self.default_branch),
            'cd {0} && git fetch --all --depth=2'.format(self.builddir),
            'cd {0} && git fetch --all --tags'.format(self.builddir),
            # now we need to handle our .github directory and files
            'cd {0} && [ -d {1} ] && mv {1} {2}'.format(self.builddir,'.github','tmp.github')
            # Remove working directory files when updating from upstream, so that deletions get picked up.
            # Disabled, because it was breaking Magento updates. Even though it was added to avoid breaking Magento updates.
            # 'cd {0} &&  (find . -maxdepth 1 -not \( -path ./.git -o -path . \) -exec rm -rf {{}} \;)'.format(self.builddir),
        ]

        if hasattr(self, 'major_version'):
            def merge_from_upstream_tag():
                latest_tag = self.latest_tag()
                print("Merging from upstream tag: {0}".format(latest_tag))
                subprocess.check_output('cd {0} && git merge --allow-unrelated-histories -X theirs --squash {1}'.format(
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

        # now we need to deal with the upstream README
        actions.append(
            'cd {0} && if [[ -f "{1}.{2}" ]]; then echo "moving upstream {1}.{2} to {1}{3}.{2}";mv "{1}.{2}" "{1}'
            '{3}.{2}"; git add "{1}{3}.{2}";git commit -m "renamed {1} to {1}{3}";fi;'
            .format(self.builddir, self.readMeFileName, self.readMeFileExt, self.readMeUpstreamFile)
        )

        # and now our README
        actions.append(
            'cd {0} && if [[ -f "{1}{3}.{2}" ]]; then echo "Moving our {1}{3}.{2} back to {1}.{2}";mv "{1}{3}.{2}" "'
            '{1}.{2}";git add {1}.{2};git commit -m "Commiting our {1}.{2}";fi;'
            .format(self.builddir, self.readMeFileName, self.readMeFileExt, self.readMePSHFile)
        )

        # now if a .github directory was reintroduced from the upstream, delete it, and then if ours is present, rename
        # it back to .github
        actions.append(
            # remove a .github directory that might have been brought in from upstream
            # @todo should we loop through all possible directories/files that may need to be removed?
            'cd {0}; if [ -d {1} ]; then rm -rf {1};fi; if [ -d {2} ]; then mv {2} {1};fi;'.format(self.builddir, '.github', 'tmp'
                                                                                                              '.github')
        )
        # Do this last so it picks up all changes from above.
        actions.extend(self.package_update_actions())

        return actions

    def latest_tag(self):
        """
        :return: string The version number of the most up to date tag matching the current major version.
        """
        all_tags = subprocess.check_output('cd {0} && git tag'.format(self.builddir), shell=True).decode(
            'utf-8').splitlines()

        tags = [tag for tag in all_tags if
                tag.startswith(self.major_version) and 'beta' not in tag and 'alpha' not in tag]
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
