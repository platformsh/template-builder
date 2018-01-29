DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}

def task_symfony3():
    return {
        'task_dep': ['symfony3_update', 'symfony3_platformify', 'symfony3_branch',],
        'actions': []
    }

def task_symfony3_cleanup():
    return common_cleanup()

def task_symfony3_init():
    return {
        'task_dep': ['symfony3_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-symfony3.git template',
            'cd template && git remote add project https://github.com/symfony/symfony-standard.git'
        ]
    }


def task_symfony3_update():
    return {
        'actions': [
            'cd template && git checkout master',
            'cd template && git fetch --all --depth=2',
            'cd template && git merge --allow-unrelated-histories -X theirs --squash project/3.4',
            'cd template && composer install --no-interaction'
        ]
    }

def task_symfony3_platformify():
    return {
        'actions': [
            'rsync -aP files/ template/',
            'cd template && patch -p1 < ../parameters.patch'
        ]
    }

def task_symfony3_branch():
    return common_branch()

def task_symfony3_push():
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
