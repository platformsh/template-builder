import json
import os.path
from collections import OrderedDict

IGNORED = ["__pycache__"]
ROOTDIR = os.path.dirname(os.path.abspath(__file__))

DOIT_CONFIG = {
    "verbosity": 2,
}


# @TODO Add _push to all of the top-level tasks for one-stop shopping.

ALL_PROJECTS = [f.name for f in os.scandir(ROOTDIR)
                if f.is_dir() and f.name not in IGNORED
                ]


class BaseProject(object):

    def __init__(self, name):
        self.name = name

    @property
    def cleanup(self):
        return ['rm -rf {0}/build'.format(self.name)]

    @property
    def init(self):
        return ['git clone git@github.com:platformsh/template-{0}.git {0}/build'.format(
            self.name)
        ]

    @property
    def platformify(self):
        return ['rm -rf {0}/build'.format(self.name)]

    @property
    def update(self):
        return ['cd {0}/build && git checkout master && git pull --prune'.format(
            self.name)
        ]

    @property
    def push(self):
        return ['cd {0}/build && git checkout update && git push --force -u origin update'.format(
            self.name)
        ]

    @property
    def branch(self):
        return [
            'cd {0}/build && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;'.format(
                self.name),
            'cd {0}/build && git checkout -b update'.format(self.name),
            'cd {0}/build && git add -A && git commit -m "Update to latest upstream"'.format(
                self.name),
        ],


def task_cleanup():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': name,
            'actions': project.cleanup,
        }


def task_init():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': name,
            'task_dep': ['cleanup:{0}'.format(name)],
            'actions': project.init,
        }


def task_platformify():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': name,
            'actions': project.platformify,
        }


def task_update():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': name,
            'actions': project.update,
        }


def task_branch():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': name,
            'actions': project.branch,
        }


def task_push():
    for name in ALL_PROJECTS:
        project_cls = BaseProject
        project = project_cls(name)
        yield {
            'name': project,
            'actions': project.push,
        }


def task_workflow():
    for name in ALL_PROJECTS:
        yield {
            'basename': name,
            'task_dep': ["{0}:{1}".format(action, name)
                         for action in ['update', 'platformify', 'branch']
                         ],
            'actions': [],
        }

# def common_update(root, tag='', branch=''):
#
#    actions = [
#        'cd %s/build && git checkout master' % root,
#        'cd %s/build && git fetch --all --depth=2' % root,
#        'cd %s/build && git fetch --all --tags' % root,
#    ]
#
#    if tag:
#        actions.append('cd %s/build && git merge --allow-unrelated-histories -X theirs --squash %s' % (root, tag))
#    elif branch:
#        actions.append('cd %s/build && git merge --allow-unrelated-histories -X theirs --squash project/%s' % (root, branch))
#    else:
#        raise Exception('Either a tag or branch must be specified.')
#
#    actions.append('cd %s/build && composer update --prefer-dist --ignore-platform-reqs --no-interaction' % root)
#
#    return {
#        'actions': actions
#    }
