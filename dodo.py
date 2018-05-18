DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}

# @TODO Add _push to all of the top-level tasks for one-stop shopping.

ALL_PROJECTS = ['drupal8', 'drupal7', 'symfony3', 'drupal7_vanilla', 'symfony4', 'wordpress', 'flask']

def task_all():
    return {
        'task_dep': ALL_PROJECTS,
        'actions': []
    }

def task_all_init():

    return {
        'task_dep': [s + '_init' for s in ALL_PROJECTS],
        'actions': []
    }


### Drupal 8 ###

def task_drupal8():
    return {
        'task_dep': ['drupal8_update', 'drupal8_platformify', 'drupal8_branch',],
        'actions': []
    }

def task_drupal8_init():
    return {
        'task_dep': ['drupal8_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal8.git drupal8/template',
            'cd drupal8/template && git remote add project https://github.com/drupal-composer/drupal-project.git'
        ]
    }

def task_drupal8_platformify():
    return {
        'actions': [
            'rsync -aP drupal8/files/ drupal8/template/'
        ]
    }

def task_drupal8_cleanup():
    return common_cleanup('drupal8')

def task_drupal8_update():
    return common_update('drupal8', '8.x')

def task_drupal8_branch():
    return common_branch('drupal8')

def task_drupal8_push():
    return common_push('drupal8')


### Symfony 3 ###

def task_symfony3():
    return {
        'task_dep': ['symfony3_update', 'symfony3_platformify', 'symfony3_branch',],
        'actions': []
    }

def task_symfony3_init():
    return {
        'task_dep': ['symfony3_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-symfony3.git symfony3/template',
            'cd symfony3/template && git remote add project https://github.com/symfony/symfony-standard.git'
        ]
    }

def task_symfony3_platformify():
    return {
        'actions': [
            'rsync -aP symfony3/files/ symfony3/template/',
            'cd symfony3/template && patch -p1 < ../parameters.patch'
        ]
    }

def task_symfony3_cleanup():
    return common_cleanup('symfony3')

def task_symfony3_update():
    return common_update('symfony3', '3.4')

def task_symfony3_branch():
    return common_branch('symfony3')

def task_symfony3_push():
    return common_push('symfony3')

### Symfony 4 ###

def task_symfony4():
    return {
        'task_dep': ['symfony4_update', 'symfony4_platformify', 'symfony4_branch',],
        'actions': []
    }

def task_symfony4_init():
    return {
        'task_dep': ['symfony4_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-symfony4.git symfony4/template',
            'cd symfony4/template && git remote add project https://github.com/symfony/skeleton.git'
        ]
    }

def task_symfony4_platformify():
    return {
        'actions': [
            'rsync -aP symfony4/files/ symfony4/template/',
            'cd symfony4/template && composer require platformsh/symfonyflex-bridge'
        ]
    }

def task_symfony4_cleanup():
    return common_cleanup('symfony4')

def task_symfony4_update():
    return common_update('symfony4', '4.0')

def task_symfony4_branch():
    return common_branch('symfony4')

def task_symfony4_push():
    return common_push('symfony4')


### Drupal 7 (Drush Make) ###

def task_drupal7():
    return {
        'task_dep': ['drupal7_update', 'drupal7_platformify', 'drupal7_branch',],
        'actions': []
    }

def task_drupal7_init():
    return {
        'task_dep': ['drupal7_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal7.git drupal7/template',
        ]
    }

def task_drupal7_platformify():
    return {
        'actions': [
            'rsync -aP drupal7/files/ drupal7/template/'
        ]
    }

def task_drupal7_update():
    return {
        'actions': []
    }

def task_drupal7_cleanup():
    return common_cleanup('drupal7')

def task_drupal7_branch():
    return common_branch('drupal7')

def task_drupal7_push():
    return common_push('drupal7')


### Drupal 7 (Vanilla) ###

def task_drupal7_vanilla():
    return {
        'task_dep': ['drupal7_vanilla_update', 'drupal7_vanilla_platformify', 'drupal7_vanilla_branch',],
        'actions': []
    }

def task_drupal7_vanilla_init():
    return {
        'task_dep': ['drupal7_vanilla_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-drupal7-vanilla.git drupal7_vanilla/template',
        ]
    }

def task_drupal7_vanilla_platformify():
    return {
        'actions': [
            'rsync -aP drupal7_vanilla/files/ drupal7_vanilla/template/',
            'cd drupal7_vanilla/template && patch -p1 < ../allow-settings-files.patch',
        ]
    }

def task_drupal7_vanilla_update():
    return {
        'actions': [
            'cd drupal7_vanilla/template && git checkout master && git pull --prune',
            "wget -qO- https://ftp.drupal.org/files/projects/drupal-7.58.tar.gz | tar xzv --transform 's/^drupal-7.58/docroot/' -C drupal7_vanilla/template/"
        ]
    }

def task_drupal7_vanilla_cleanup():
    return common_cleanup('drupal7_vanilla')

def task_drupal7_vanilla_branch():
    return common_branch('drupal7_vanilla')

def task_drupal7_vanilla_push():
    return common_push('drupal7_vanilla')


### Wordpress (Composer) ###

def task_wordpress():
    return {
        'task_dep': ['wordpress_update', 'wordpress_platformify', 'wordpress_branch',],
        'actions': []
    }

def task_wordpress_init():
    return {
        'task_dep': ['wordpress_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-wordpress.git wordpress/template',
            'cd wordpress/template && git remote add project https://github.com/johnpbloch/wordpress.git'
        ]
    }

def task_wordpress_platformify():
    # @TODO Still need to port over more composer changes. What's the best way to modify composer.json
    # from here?
    return {
        'actions': [
            'rsync -aP wordpress/files/ wordpress/template/',
        ]
    }

def task_wordpress_cleanup():
    return common_cleanup('wordpress')

def task_wordpress_update():
    return common_update('wordpress', '4.9')

def task_wordpress_branch():
    return common_branch('wordpress')

def task_wordpress_push():
    return common_push('wordpress')


### Flask ###

def task_flask():
    return {
        'task_dep': ['flask_update', 'flask_platformify', 'flask_branch',],
        'actions': []
    }

def task_flask_init():
    return {
        'task_dep': ['flask_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-flask.git flask/template',
        ]
    }

def task_flask_platformify():
    return {
        'actions': [
            'rsync -aP flask/files/ flask/template/',
        ]
    }

def task_flask_cleanup():
    return common_cleanup('flask')

def task_flask_update():
    return {
        'actions': [
            'cd flask/template && git checkout master && git pull --prune'
        ]
    }

def task_flask_branch():
    return common_branch('flask')

def task_flask_push():
    return common_push('flask')



### Common command templates ###

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
            'cd %s/template && git checkout -B update && git push -u origin update' % root,
            'cd %s/template && hub pull-request -m "Update to latest upstream" -b platformsh:master -h update' % root
        ]
    }
