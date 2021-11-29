from . import BaseProject
import json
import requests

class Mattermost(BaseProject):

    @property
    def platformify(self):

        response = requests.get('https://api.github.com/repos/mattermost/mattermost-server/releases')
        version = response.json()[0]["name"][1:]

        return super(Mattermost, self).platformify + [
            'cd {0} && echo {1} > mattermost_version'.format(self.builddir, version),
        ]
