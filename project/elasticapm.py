from . import BaseProject
import json
import requests

class Elastic_apm(BaseProject):

    @property
    def platformify(self):

        # Kibana
        response = requests.get('https://api.github.com/repos/elastic/kibana/releases')
        kibana_version = response.json()[0]["tag_name"][1:]

        # APM
        response = requests.get('https://api.github.com/repos/elastic/apm-server/releases')
        apm_version = response.json()[0]["tag_name"][1:]

        return super(Elastic_apm, self).platformify + [
            'cd {0}/kibana && echo {1} > kibana_version'.format(self.builddir, kibana_version),
            'cd {0}/apm  && echo {1} > apm_version'.format(self.builddir, apm_version),
        ]
