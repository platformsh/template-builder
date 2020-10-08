from .remote import RemoteProject

class Gatsby(RemoteProject):
    upstream_branch = "master"
    remote = 'https://github.com/gatsbyjs/gatsby-starter-blog.git'
    updateCommands = {
        'package.json': 'yarn upgrade'
    }
    