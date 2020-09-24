# from . import BaseProject
from .remote import RemoteProject
# import json
# from collections import OrderedDict

class Gatsby(RemoteProject):
    upstream_branch = "master"
    remote = 'https://github.com/gatsbyjs/gatsby-starter-blog.git'
    updateCommands = {
        'yarn.lock': 'yarn upgrade'
    }