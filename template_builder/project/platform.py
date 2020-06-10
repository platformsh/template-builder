from . import BaseProject


class Platform(BaseProject):

    @property
    def update(self):
        return None

    @property
    def platformify(self):
        return None
