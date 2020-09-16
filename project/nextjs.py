from . import BaseProject

class Nextjs(BaseProject):
    updateCommands = {
        'yarn.lock': 'yarn upgrade'
    }
