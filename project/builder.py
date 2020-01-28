from os import scandir

from project.config import TEMPLATEDIR, IGNORED
from project import BaseProject


def project_factory(name):
    """Instantiate a project object.  Class selection is based on the following naming convention:
    Project class matches template directory name with the first letter capitalized.
      laravel -> Laravel,
      drupal7_vanilla -> Drupal7_vanilla.

    The BaseProject class is used by default (class with the matching name is not imported)

    :param name: name of the project
    :return: BaseProject
    """

    targetclass = name.capitalize().replace("-", "_")
    try:
        return globals()[targetclass](name)
    except KeyError:
        return BaseProject(name)


def project_list():
    """
    Return a list of project factories defining the available projects
    :return: list
    """
    return [
        project_factory(f.name)
        for f in scandir(TEMPLATEDIR)
        if f.is_dir() and f.name not in IGNORED
    ]
