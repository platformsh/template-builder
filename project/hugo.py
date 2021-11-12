from . import BaseProject
import json
import requests

class Hugo(BaseProject):

    @property
    def platformify(self):

        response = requests.get('https://api.github.com/repos/gohugoio/hugo/releases')
        version = response.json()[0]["name"][1:]

        return super(Hugo, self).platformify + [
            'cd {0} && echo {1} > hugo_version'.format(self.builddir, version),
        ]
