'''
DoIt (http://pydoit.org/) main Python module. Tasks are automatically generated for all projects from
ALL_PROJECTS list. Template directory is scanned for the templates. When adding new template, no
changes to this file are needed in case BaseProject implementations of all tasks are satisfying.
In case the actions of some tasks need to be customized, the new BaseProject subclass must be imported.
'''

import os

from project import BaseProject, TEMPLATEDIR
from project.akeneo import Akeneo
from project.backdrop import Backdrop
from project.drupal import Drupal7_vanilla, Drupal8, Drupal8_multisite, Drupal8_opigno, Drupal8_govcms8, Drupal9
from project.gatsby import Gatsby
from project.laravel import Laravel
from project.magento import Magento2ce
from project.pimcore import Pimcore
from project.laravel import Laravel
from project.magento import Magento2ce
from project.mautic import Mautic
from project.nextjs import Nextjs
from project.nuxtjs import Nuxtjs
from project.rails import Rails
from project.sculpin import Sculpin
from project.strapi import Strapi
from project.symfony import Symfony3, Symfony4, Symfony5
from project.typo3 import Typo3
from project.wordpress import Wordpress

DOIT_CONFIG = {
    "verbosity": 2,
}

# Blacklist of projects to ignore.
IGNORED = []

def project_factory(name):
    '''Instantiate a project object.  Class selection is based on the following naming convention:
    Project class matches template directory name with the first letter capitalized.
      laravel -> Laravel,
      drupal7_vanilla -> Drupal7_vanilla.

    The BaseProject class is used by default (class with the matching name is not imported)
    '''

    targetclass = name.capitalize().replace('-', '_')
    try:
        return globals()[targetclass](name)
    except KeyError:
        return BaseProject(name)

ALL_PROJECTS = [project_factory(f.name) for f in os.scandir(TEMPLATEDIR)
                if f.is_dir() and f.name not in IGNORED]

def task_cleanup():
    """
    DoIt Task: Removes all generated files for a project.

    Usage: doit cleanup:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.cleanup,
        }


def task_init():
    """
    DoIt Task: Initializes a project directory so it can be built.

    Usage: doit init:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'task_dep': ['cleanup:{0}'.format(project.name)],
            'actions': project.init,
        }


def task_update():
    """
    DoIt Task: Updates the build repository from upstream sources.

    Usage: doit update:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.update,
        }


def task_platformify():
    """
    DoIt Task: Applies necessary changes to a project,
    such as adding configuration files, applying patches, etc.

    Usage: doit platformify:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.platformify,
        }


def task_branch():
    """
    DoIt Task: Creates a new Git branch for pushing updates to the template repo.

    Usage: doit branch:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.branch,
        }


def task_push():
    """
    DoIt Task: Pushes a prepared branch to GitHub.

    Usage: doit push:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'actions': project.push,
        }


def task_rebuild():
    """
    DoIt Task: Aggregates the update, platformify, and branch tasks for one-stop shopping.

    Usage: doit rebuild:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'task_dep': ["{0}:{1}".format(action, project.name)
                         for action in ['update', 'platformify', 'branch']
                         ],
            'actions': [],
        }


def task_full():
    """
    DoIt Task: Aggregates the init, rebuild, and push tasks for one-stop shopping.

    Usage: doit full:<project>
    """
    for project in ALL_PROJECTS:
        yield {
            'name': project.name,
            'task_dep': ["{0}:{1}".format(action, project.name)
                         for action in ['cleanup', 'init', 'update', 'platformify', 'branch', 'push']
                         ],
            'actions': [],
        }
