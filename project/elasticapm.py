from . import BaseProject
import os
import json
import requests

class Elastic_apm(BaseProject):

    @property
    def platformify(self):

        if os.environ.get("GITHUB_TOKEN"):
            headers = {"Authorization": "token {0}".format(os.environ.get("GITHUB_TOKEN"))}
            responseKibana = requests.get('https://api.github.com/repos/elastic/kibana/releases', headers=headers)
            responseAPM = requests.get('https://api.github.com/repos/elastic/apm-server/releases', headers=headers)
        else:
            responseKibana = requests.get('https://api.github.com/repos/elastic/kibana/releases')
            responseAPM = requests.get('https://api.github.com/repos/elastic/apm-server/releases')

        kibana_version = responseKibana.json()[0]["tag_name"][1:]
        apm_version = responseAPM.json()[0]["tag_name"][1:]

        return super(Elastic_apm, self).platformify + [
            'cd {0}/kibana && echo {1} > kibana_version'.format(self.builddir, kibana_version),
            'cd {0}/apm  && echo {1} > apm_version'.format(self.builddir, apm_version),
        ]
