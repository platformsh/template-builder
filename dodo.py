'''
DoIt (http://pydoit.org/) main Python module. Tasks are automatically generated for all projects from
project_list() list. Template directory is scanned for the templates. When adding new template, no
changes to this file are needed in case BaseProject implementations of all tasks are satisfying.
In case the actions of some tasks need to be customized, the new BaseProject subclass must be imported.
'''

from project.builder import project_list

DOIT_CONFIG = {
    "verbosity": 2,
}


def task_cleanup():
    """
    DoIt Task: Removes all generated files for a project.

    Usage: doit cleanup:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.cleanup,
        }


def task_init():
    """
    DoIt Task: Initializes a project directory so it can be built.

    Usage: doit init:<project>
    """
    for project in project_list():
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
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.update,
        }


def task_build():
    """
    DoIt Task: Runs any build steps required for the application

    Usage: doit build:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.build,
        }


def task_platformify():
    """
    DoIt Task: Applies necessary changes to a project,
    such as adding configuration files, applying patches, etc.

    Usage: doit platformify:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.platformify,
        }


def task_branch():
    """
    DoIt Task: Creates a new Git branch for pushing updates to the template repo.

    Usage: doit branch:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.branch,
        }


def task_push():
    """
    DoIt Task: Pushes a prepared branch to GitHub.

    Usage: doit push:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'actions': project.push,
        }


def task_rebuild():
    """
    DoIt Task: Aggregates the update, platformify, and branch tasks for one-stop shopping.

    Usage: doit rebuild:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'task_dep': ["{0}:{1}".format(action, project.name)
                         for action in ['update', 'build', 'platformify', 'branch']
                         ],
            'actions': [],
        }


def task_full():
    """
    DoIt Task: Aggregates the init, rebuild, and push tasks for one-stop shopping.

    Usage: doit full:<project>
    """
    for project in project_list():
        yield {
            'name': project.name,
            'task_dep': ["{0}:{1}".format(action, project.name)
                         for action in ['cleanup', 'init', 'update', 'platformify', 'branch', 'push']
                         ],
            'actions': [],
        }
