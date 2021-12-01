from . import BaseProject
import json
import requests

class Mattermost(BaseProject):

    @property
    def platformify(self):

        major_version = "6.1"

        response = requests.get('https://api.github.com/repos/mattermost/mattermost-server/releases')

        tags = [release["tag_name"] for release in response.json() if release["tag_name"].startswith("v{}".format(major_version)) and 'beta' not in release["tag_name"] and 'alpha' not in release["tag_name"]]

        return super(Mattermost, self).platformify + [
            'cd {0} && echo {1} > mattermost_version'.format(self.builddir, tags[0]),
        ]
