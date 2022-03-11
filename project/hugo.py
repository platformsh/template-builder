
from . import BaseProject
import os
import json
import requests

class Hugo(BaseProject):

    @property
    def platformify(self):

        headers = {'Authorization': "token {0}".format(os.environ.get("GITHUB_TOKEN"))}

        major_version = "0.91"

        response = requests.get('https://api.github.com/repos/gohugoio/hugo/releases', headers=headers)

        tags = [release["tag_name"] for release in response.json() if release["tag_name"].startswith("v{}".format(major_version)) and 'beta' not in release["tag_name"] and 'alpha' not in release["tag_name"]]

        return super(Hugo, self).platformify + [
            'cd {0} && echo {1} > hugo_version'.format(self.builddir, tags[0][1:]),
        ]
