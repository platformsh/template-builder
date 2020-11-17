import os
import requests
import meilisearch
from platformshconfig import Config

class MeilisearchTemplate:
    def __init__(self):
        self.default = {
            "host": "http://127.0.0.1",
            "key": None,
            "port": 7700
        }
        self.seed = {
            "indexName": "movies",
            "source": "https://raw.githubusercontent.com/meilisearch/MeiliSearch/master/datasets/movies/movies.json"
        }

    def getConnectionString(self):
        """
        Sets the Meilisearch host string, depending on the environment.

        Returns:
            string: Meilisearch host string.
        """
        if os.environ.get('PORT'):
            return "{}:{}".format(self.default["host"], os.environ['PORT'])
        else:
            return "{}:{}".format(self.default["host"], self.default["port"])

    def getMasterKey(self):
        config = Config()
        if config.is_valid_platform() and not os.environ.get('TEMPLATE_DEMO'):
            if config.branch == "master":
                return config.projectEntropy
            else:
                return config.branch
        elif os.environ.get("MEILI_MASTER_KEY"):
            return os.environ["MEILI_MASTER_KEY"]
        else:
            return self.default["key"]

    def getSeedData(self):
        return requests.get(self.seed["source"]).json()

    def update(self):
        # Create a Meilisearch client.
        client = meilisearch.Client(self.getConnectionString(), self.getMasterKey())
        # Seed with default dataset if file is present.
        if os.environ.get('TEMPLATE_DEMO'):
            # Local: delete the seed index if exists.
            if len(client.get_indexes()):
                client.get_index(self.seed["indexName"]).delete()
            # Create a new index.
            index = client.create_index(uid=self.seed["indexName"])
            # Add the seed dataset's documents to the index.
            index.add_documents(self.getSeedData())

if __name__ == "__main__":
    meili = MeilisearchTemplate()
    meili.update()
