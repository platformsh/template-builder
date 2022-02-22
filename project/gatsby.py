from .remote import RemoteProject

class Gatsby(RemoteProject):
    upstream_branch = "master"
    remote = 'https://github.com/gatsbyjs/gatsby-starter-blog.git'

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def platformify(self):

        return super(Gatsby, self).platformify + [
            # Add dependencies.
            'cd {0} && rm -rf package-lock.json'.format(self.builddir),
        ]