from . import BaseProject

class Gatsby(BaseProject):
    upstream_branch = "master"
    remote = 'https://github.com/gatsbyjs/gatsby-starter-blog.git'
    updateCommands = {
        'yarn.lock': 'yarn upgrade'
    }