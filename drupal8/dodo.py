DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}

def task_drupal8():
    return {
        'task_dep': ['drupal8_update', 'drupal8_platformify', 'drupal8_branch',],
        'actions': []
    }

def task_drupal8_cleanup():
    return common_cleanup()

def task_drupal8_init():
    return {
        'task_dep': ['drupal8_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git template',
            'cd template && git remote add project https://github.com/drupal-composer/drupal-project.git'
        ]
    }


def task_drupal8_update():
    return {
        'actions': [
            'cd template && git checkout master',
            'cd template && git fetch --all --depth=2',
            'cd template && git merge --allow-unrelated-histories -X theirs --squash project/8.x',
            'cd template && composer install'
        ]
    }

def task_drupal8_platformify():
    return {
        'actions': [
            'rsync -aP files/ template/'
        ]
    }

def task_drupal8_branch():
    return common_branch()

def task_drupal8_push():
    return common_push()


def common_cleanup():
    return {
        'actions': [
            'rm -rf template'
        ]
    }

def common_branch():
    return {
        'actions': [
            'cd template && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;',
            'cd template && git checkout -b update',
            'cd template && git add -A && git commit -m "Update to latest upstream"'
        ]
    }

def common_push():
    return {
        'actions': [
            'cd template && git checkout update && git push -u origin update',
            'cd template && hub pull-request -m "Update to latest upstream" -b platformsh:master -h update'
        ]
    }
