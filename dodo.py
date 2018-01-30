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
    return common_cleanup('drupal8')

def task_drupal8_init():
    return {
        'task_dep': ['drupal8_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git drupal8/template',
            'cd drupal8/template && git remote add project https://github.com/drupal-composer/drupal-project.git'
        ]
    }


def task_drupal8_update():
    return common_update('drupal8', '8.x')

def task_drupal8_platformify():
    return {
        'actions': [
            'rsync -aP drupal8/files/ drupal8/template/'
        ]
    }

def task_drupal8_branch():
    return common_branch('drupal8')

def task_drupal8_push():
    return common_push('drupal8')


def task_symfony3():
    return {
        'task_dep': ['symfony3_update', 'symfony3_platformify', 'symfony3_branch',],
        'actions': []
    }

def task_symfony3_cleanup():
    return common_cleanup('symfony3')

def task_symfony3_init():
    return {
        'task_dep': ['symfony3_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-symfony3.git template',
            'cd symfony3/template && git remote add project https://github.com/symfony/symfony-standard.git'
        ]
    }

def task_symfony3_update():
    return common_update('symfony3', '3.4')

def task_symfony3_platformify():
    return {
        'actions': [
            'rsync -aP symfony3/files/ symfony3/template/',
            'cd symfony3/template && patch -p1 < ../parameters.patch'
        ]
    }

def task_symfony3_branch():
    return common_branch('symfony3')

def task_symfony3_push():
    return common_push('symfony3')



def common_cleanup(root):
    return {
        'actions': [
            'rm -rf %s/template' % root
        ]
    }

def common_update(root, branch):
    return {
        'actions': [
            'cd %s/template && git checkout master' % root,
            'cd %s/template && git fetch --all --depth=2' % root,
            'cd %s/template && git merge --allow-unrelated-histories -X theirs --squash project/%s' % (root, branch),
            'cd %s/template && composer install --no-interaction' % root
        ]
    }

def common_branch(root):
    return {
        'actions': [
            'cd %s/template && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;' % root,
            'cd %s/template && git checkout -b update' % root,
            'cd %s/template && git add -A && git commit -m "Update to latest upstream"' % root
        ]
    }

def common_push(root):
    return {
        'actions': [
            'cd %s/template && git checkout update && git push -u origin update' % root,
            'cd %s/template && hub pull-request -m "Update to latest upstream" -b platformsh:master -h update' % root
        ]
    }
