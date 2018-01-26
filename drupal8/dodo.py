

DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}

def task_drupal8():
    return {
        'file_dep': ['drupal8_cleanup', 'drupal8_init', 'drupal8_update', 'drupal8_platformify', 'drupal8_branch'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git template',
            'cd template && git remote add upstream https://github.com/drupal-composer/drupal-project.git'
        ]
    }

def task_drupal8_cleanup():
    return {
        'actions': [
            'rm -rf template'
        ]
    }

def task_drupal8_init():
    return {
        'file_dep': ['drupal8_clean'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git template',
            'cd template && git remote add upstream https://github.com/drupal-composer/drupal-project.git'
        ]
    }


def task_drupal8_update():
    return {
        'actions': [
            'cd template && git fetch --all --depth=2',
            'cd template && git merge --allow-unrelated-histories -X theirs --squash upstream/8.x',
            'cd template && composer install'
        ]
    }

def task_drupal8_platformify():
    return {
        'actions': [
            'rsync -aP files/ template/'
        ]
    }

def drupal8_branch():
    return {
        'actions': [
            'cd template && git checkout -b update',
            'cd template && git add -A && git commit -m "Update to latest upstream"'
        ]
    }

def drupal8_push():
    return {
        'actions': [
            'cd template && git checkout update && git push -u origin update',
            'cd template && hub pull-request -m "Update to latest upstream" -b master -h update'
        ]
    }
