'''
DoIt (http://pydoit.org/) main Python module. Tasks are automatically generated for all projects from
ALL_PROJECTS list. Template directory is scanned for the templates. When adding new template, no
changes to this file are needed in case BaseProject implementations of all tasks are satisfying.
In case the actions of some tasks need to be customized, the new BaseProject subclass must be imported.
'''

import os

from project import BaseProject, TEMPLATEDIR
from project.drupal import Drupal7_vanilla, Drupal8
from project.laravel import Laravel
from project.magento import Magento2ce
from project.symfony import Symfony3, Symfony4
from project.wordpress import Wordpress

DOIT_CONFIG = {
    "verbosity": 2,
}


def project_factory(name):
    '''Instantiate a project object, class selection is based on the following naming convention:
    Project class matches template directory name with the first letter capitalized.
      laravel -> Laravel,
      drupal7_vanilla -> Drupal7_vanilla.

    Base project class is used by default (class with the matching name is not imported)
    '''

    targetclass = name.capitalize()
    try:
        return globals()[targetclass](name)
    except KeyError:
        return BaseProject(name)


IGNORED = []
ALL_PROJECTS = [project_factory(f.name) for f in os.scandir(TEMPLATEDIR)
                if f.is_dir() and f.name not in IGNORED]

# @TODO Add _push to all of the top-level tasks for one-stop shopping.


def task_cleanup():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.cleanup,
        }


def task_init():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'task_dep': ['cleanup:{0}'.format(project.name)],
            'actions': project.init,
        }


def task_platformify():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.platformify,
        }


def task_update():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.update,
        }


def task_branch():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.branch,
        }


def task_push():
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.push,
        }


def task_workflow():
    for project in ALL_PROJECTS:
        yield {
            'basename': project.name,
            'task_dep': ["{0}:{1}".format(action, project.name)
                         for action in ['update', 'platformify', 'branch']
                         ],
            'actions': [],
        }
