import os
from wikiserverconfig import LocalConfig


class Config(LocalConfig):
    hostname = '127.0.0.1'
    port = int(os.environ['PORT'])
