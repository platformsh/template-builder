from . import BaseProject, TEMPLATEDIR
import os


class Phoenix_elixir(BaseProject):
    '''Phoenix_elixir object.

    This is necessary because elixir has some very specific naming conventions, that prevent the template from being called
    simply 'phoenix' (since it is trying to compile the phoenix Hex module), and the project cannot contain the '-' character,
    only underscore.

    This constructor sets the 'github_name' attribute to get around the naming convention checks in the BaseProject constructor.

    Here, it simply reuses 'name' to match the directory name exactly.
    '''
    def __init__(self, name):
        self.name = name
        self.github_name = name
        self.builddir = os.path.join(TEMPLATEDIR, self.name, 'build/')
