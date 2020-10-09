from .remote import RemoteProject

class Gatsby(RemoteProject):
    upstream_branch = "master"
    remote = 'https://github.com/gatsbyjs/gatsby-starter-blog.git'

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }
    