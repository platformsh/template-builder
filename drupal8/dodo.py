

DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}


def task_drupal8():

    for task in common_tasks('drupal8'):
        yield task

    yield {
        'basename': 'drupal8:init',
        'file_dep': ['drupal8:clean'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git template',
            'cd template && git remote add upstream https://github.com/drupal-composer/drupal-project.git'
        ]
    }

    yield {
        'basename': 'drupal8:update',
        'actions': [
            'cd template && git fetch --all --depth=2',
            'cd template && git merge --allow-unrelated-histories -X theirs --squash upstream/8.x',
            'cd template && composer install'
        ]
    }

    yield {
        'basename': 'drupal8:platformify',
        'actions': [
            'rsync -aP files/ template/'
        ]
    }

def common_tasks(system):

    yield {
        'name': "%s:clean" % system,
        'actions': [
            'rm -rf template'
        ]
    }

"""
    return {
        'basename': 'Drupal8',
        'actions': [
            'echo hello',
            'echo world'
        ]
    }
"""
