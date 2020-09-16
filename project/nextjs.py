from . import BaseProject
import os.path
from glob import glob
from . import TEMPLATEDIR

class Nextjs(BaseProject):
    updateCommands = {
        'yarn.lock': 'yarn upgrade'
    }
    