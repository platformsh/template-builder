import json
from collections import OrderedDict

DOIT_CONFIG = {
    #"num_process": 16,
    #"par_type": "thread",
    "verbosity": 2,
}

UPSTREAM_VERSIONS = {
    'drupal7_vanilla': '7.61',
    'drupal8': '8.x',
    'laravel': 'v5.7.15',
    'magento2ce': '2.2',
    'symfony3': '3.4',
    'symfony4': '4.2',
    'wordpress': '5.0.1',
}

# @TODO Add _push to all of the top-level tasks for one-stop shopping.

ALL_PROJECTS = [
    'django1',
    'django2',
    'drupal7',
    'drupal7_vanilla',
    'drupal8',
    'flask',
    'golang',
    'laravel',
    'magento2ce',
    'php',
    'python2',
    'python3',
    'symfony3',
    'symfony4',
    'wordpress',
]

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

def task_all_cleanup():
    return {
        'task_dep': [s + '_cleanup' for s in ALL_PROJECTS],
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
            'git clone git@github.com:platformsh/template-drupal8.git drupal8/build',
            'cd drupal8/build && git remote add project https://github.com/drupal-composer/drupal-project.git'
        ]
    }

def task_drupal8_platformify():
    return {
        'actions': [
            'rsync -aP drupal8/files/ drupal8/build/'
        ]
    }

def task_drupal8_cleanup():
    return common_cleanup('drupal8')

def task_drupal8_update():
    return common_update('drupal8', branch=UPSTREAM_VERSIONS['drupal8'])

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
            'git clone git@github.com:platformsh/template-symfony3.git symfony3/build',
            'cd symfony3/build && git remote add project https://github.com/symfony/symfony-standard.git'
        ]
    }

def task_symfony3_platformify():
    return {
        'actions': [
            'rsync -aP symfony3/files/ symfony3/build/',
            'cd symfony3/build && patch -p1 < ../parameters.patch'
        ]
    }

def task_symfony3_cleanup():
    return common_cleanup('symfony3')

def task_symfony3_update():
    return common_update('symfony3', branch=UPSTREAM_VERSIONS['symfony3'])

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
            'git clone git@github.com:platformsh/template-symfony4.git symfony4/build',
            'cd symfony4/build && git remote add project https://github.com/symfony/skeleton.git'
        ]
    }

def task_symfony4_platformify():
    return {
        'actions': [
            'rsync -aP symfony4/files/ symfony4/build/',
            'cd symfony4/build && composer require platformsh/symfonyflex-bridge'
        ]
    }

def task_symfony4_cleanup():
    return common_cleanup('symfony4')

def task_symfony4_update():
    return common_update('symfony4', branch=UPSTREAM_VERSIONS['symfony4'])

def task_symfony4_branch():
    return common_branch('symfony4')

def task_symfony4_push():
    return common_push('symfony4')

### Magento 2 CE ###

def task_magento2ce():
    return {
        'task_dep': ['magento2ce_update', 'magento2ce_platformify', 'magento2ce_branch',],
        'actions': []
    }

def task_magento2ce_init():
    return {
        'task_dep': ['magento2ce_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-magento2ce.git magento2ce/build',
            'cd magento2ce/build && git remote add project https://github.com/magento/magento2.git'
        ]
    }

def task_magento2ce_platformify():
    return {
        'actions': [
            'rsync -aP magento2ce/files/ magento2ce/build/',
            'cd magento2ce/build && patch -p1 < ../platformsh.patch',
        ]
    }

def task_magento2ce_cleanup():
    return common_cleanup('magento2ce')

def task_magento2ce_update():
    return common_update('magento2ce', branch=UPSTREAM_VERSIONS['magento2ce'])

def task_magento2ce_branch():
    return common_branch('magento2ce')

def task_magento2ce_push():
    return common_push('magento2ce')

### Laravel ###

def task_laravel():
    return {
        'task_dep': ['laravel_update', 'laravel_platformify', 'laravel_branch',],
        'actions': []
    }

def task_laravel_init():
    return {
        'task_dep': ['laravel_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-laravel.git laravel/build',
            'cd laravel/build && git remote add project https://github.com/laravel/laravel.git'
        ]
    }

def task_laravel_platformify():
    return {
        'actions': [
            'rsync -aP laravel/files/ laravel/build/',
            'cd laravel/build && patch -p1 < ../phpredis.patch',
            'cd laravel/build && composer require platformsh/laravel-bridge'
        ]
    }

def task_laravel_cleanup():
    return common_cleanup('laravel')

def task_laravel_update():
    return common_update('laravel', tag=UPSTREAM_VERSIONS['laravel'])

def task_laravel_branch():
    return common_branch('laravel')

def task_laravel_push():
    return common_push('laravel')


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
            'git clone git@github.com:platformsh/template-drupal7.git drupal7/build',
        ]
    }

def task_drupal7_platformify():
    return {
        'actions': [
            'rsync -aP drupal7/files/ drupal7/build/'
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
            'git clone git@github.com:platformsh/template-drupal7-vanilla.git drupal7_vanilla/build',
        ]
    }

def task_drupal7_vanilla_platformify():
    return {
        'actions': [
            'rsync -aP drupal7_vanilla/files/ drupal7_vanilla/build/',
        ]
    }

def task_drupal7_vanilla_update():
    return {
        'actions': [
            'cd drupal7_vanilla/build && git checkout master && git pull --prune',
            "wget -qO- https://ftp.drupal.org/files/projects/drupal-" + UPSTREAM_VERSIONS['drupal7_vanilla'] + ".tar.gz | tar xzv --transform 's/^drupal-" + UPSTREAM_VERSIONS['drupal7_vanilla'] + "/docroot/' -C drupal7_vanilla/build/"
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
            'git clone git@github.com:platformsh/template-wordpress.git wordpress/build',
            'cd wordpress/build && git remote add project https://github.com/johnpbloch/wordpress.git'
        ]
    }

def task_wordpress_platformify():

    def wp_add_installer_paths():
        with open('wordpress/build/composer.json', 'r') as f:
            composer = json.load(f, object_pairs_hook=OrderedDict)

        composer['extra'] = {
            'wordpress-install-dir': 'web/wp',
            'installer-paths': {
                r'web/wp-content/plugins/{$name}': ['type:wordpress-plugin'],
                r'web/wp-content/themes/{$name}': ['type:wordpress-theme'],
                r'web/wp-content/mu-plugins/{$name}': ['type:wordpress-muplugin'],
            }
        }

        with open('wordpress/build/composer.json', 'w') as out:
            json.dump(composer, out, indent=2)

    return {
        'actions': [
            # The initial composer update put files in the wrong place, so clean that up.
            'rm -rf wordpress/build/wordpress',
            'rsync -aP wordpress/files/ wordpress/build/',
            (wp_add_installer_paths, []),
            'cd wordpress/build && composer update',
        ]
    }

def task_wordpress_cleanup():
    return common_cleanup('wordpress')

def task_wordpress_update():
    return common_update('wordpress', tag=UPSTREAM_VERSIONS['wordpress'])

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
            'git clone git@github.com:platformsh/template-flask.git flask/build',
        ]
    }

def task_flask_platformify():
    return {
        'actions': [
            'rsync -aP flask/files/ flask/build/',
        ]
    }

def task_flask_cleanup():
    return common_cleanup('flask')

def task_flask_update():
    return {
        'actions': [
            'cd flask/build && git checkout master && git pull --prune'
        ]
    }

def task_flask_branch():
    return common_branch('flask')

def task_flask_push():
    return common_push('flask')


### Django 1 ###

def task_django1():
    return {
        'task_dep': ['django1_update', 'django1_platformify', 'django1_branch',],
        'actions': []
    }

def task_django1_init():
    return {
        'task_dep': ['django1_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-django1.git django1/build',
        ]
    }

def task_django1_platformify():
    return {
        'actions': [
            'rsync -aP django1/files/ django1/build/',
        ]
    }

def task_django1_cleanup():
    return common_cleanup('django1')

def task_django1_update():
    return {
        'actions': [
            'cd django1/build && git checkout master && git pull --prune'
        ]
    }

def task_django1_branch():
    return common_branch('django1')

def task_django1_push():
    return common_push('django1')


### Django 2 ###

def task_django2():
    return {
        'task_dep': ['django2_update', 'django2_platformify', 'django2_branch',],
        'actions': []
    }

def task_django2_init():
    return {
        'task_dep': ['django2_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-django2.git django2/build',
        ]
    }

def task_django2_platformify():
    return {
        'actions': [
            'rsync -aP django2/files/ django2/build/',
        ]
    }

def task_django2_cleanup():
    return common_cleanup('django2')

def task_django2_update():
    return {
        'actions': [
            'cd django2/build && git checkout master && git pull --prune'
        ]
    }

def task_django2_branch():
    return common_branch('django2')

def task_django2_push():
    return common_push('django2')


### Python 3 (UWSGI) ###

def task_python3_uwsgi():
    return {
        'task_dep': ['python3_uwsgi_update', 'python3_uwsgi_platformify', 'python3_uwsgi_branch',],
        'actions': []
    }

def task_python3_uwsgi_init():
    return {
        'task_dep': ['python3_uwsgi_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-python3-uwsgi.git python3_uwsgi/build',
        ]
    }

def task_python3_uwsgi_platformify():
    return {
        'actions': [
            'rsync -aP python3_uwsgi/files/ python3_uwsgi/build/',
        ]
    }

def task_python3_uwsgi_cleanup():
    return common_cleanup('python3_uwsgi')

def task_python3_uwsgi_update():
    return {
        'actions': [
            'cd python3_uwsgi/build && git checkout master && git pull --prune'
        ]
    }

def task_python3_uwsgi_branch():
    return common_branch('python3_uwsgi')

def task_python3_uwsgi_push():
    return common_push('python3_uwsgi')


### Python 3 ###

def task_python3():
    return {
        'task_dep': ['python3_update', 'python3_platformify', 'python3_branch',],
        'actions': []
    }

def task_python3_init():
    return {
        'task_dep': ['python3_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-python3.git python3/build',
        ]
    }

def task_python3_platformify():
    return {
        'actions': [
            'rsync -aP python3/files/ python3/build/',
        ]
    }

def task_python3_cleanup():
    return common_cleanup('python3')

def task_python3_update():
    return {
        'actions': [
            'cd python3/build && git checkout master && git pull --prune'
        ]
    }

def task_python3_branch():
    return common_branch('python3')

def task_python3_push():
    return common_push('python3')


### Python 2 ###

def task_python2():
    return {
        'task_dep': ['python2_update', 'python2_platformify', 'python2_branch',],
        'actions': []
    }

def task_python2_init():
    return {
        'task_dep': ['python2_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-python2.git python2/build',
        ]
    }

def task_python2_platformify():
    return {
        'actions': [
            'rsync -aP python2/files/ python2/build/',
        ]
    }

def task_python2_cleanup():
    return common_cleanup('python2')

def task_python2_update():
    return {
        'actions': [
            'cd python2/build && git checkout master && git pull --prune'
        ]
    }

def task_python2_branch():
    return common_branch('python2')

def task_python2_push():
    return common_push('python2')


### Golang ###

def task_golang():
    return {
        'task_dep': ['golang_update', 'golang_platformify', 'golang_branch',],
        'actions': []
    }

def task_golang_init():
    return {
        'task_dep': ['golang_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-golang.git golang/build',
        ]
    }

def task_golang_platformify():
    return {
        'actions': [
            'rsync -aP golang/files/ golang/build/',
        ]
    }

def task_golang_cleanup():
    return common_cleanup('golang')

def task_golang_update():
    return {
        'actions': [
            'cd golang/build && git checkout master && git pull --prune'
        ]
    }

def task_golang_branch():
    return common_branch('golang')

def task_golang_push():
    return common_push('golang')

### PHP (Generic) ###

def task_php():
    return {
        'task_dep': ['php_update', 'php_platformify', 'php_branch',],
        'actions': []
    }

def task_php_init():
    return {
        'task_dep': ['php_cleanup'],
        'actions': [
            'git clone git@github.com:platformsh/template-php.git php/build',
        ]
    }

def task_php_platformify():
    return {
        'actions': [
            'rsync -aP php/files/ php/build/',
        ]
    }

def task_php_cleanup():
    return common_cleanup('php')

def task_php_update():
    return {
        'actions': [
            'cd php/build && git checkout master && git pull --prune'
        ]
    }

def task_php_branch():
    return common_branch('php')

def task_php_push():
    return common_push('php')



### Common command templates ###

def common_cleanup(root):
    return {
        'actions': [
            'rm -rf %s/build' % root
        ]
    }

def common_update(root, tag='', branch=''):

    actions = [
        'cd %s/build && git checkout master' % root,
        'cd %s/build && git fetch --all --depth=2' % root,
        'cd %s/build && git fetch --all --tags' % root,
    ]

    if tag:
        actions.append('cd %s/build && git merge --allow-unrelated-histories -X theirs --squash %s' % (root, tag))
    elif branch:
        actions.append('cd %s/build && git merge --allow-unrelated-histories -X theirs --squash project/%s' % (root, branch))
    else:
        raise Exception('Either a tag or branch must be specified.')

    actions.append('cd %s/build && composer update --prefer-dist --ignore-platform-reqs --no-interaction' % root)

    return {
        'actions': actions
    }

def common_branch(root):
    return {
        'actions': [
            'cd %s/build && if git rev-parse --verify --quiet update; then git checkout master && git branch -D update; fi;' % root,
            'cd %s/build && git checkout -b update' % root,
            'cd %s/build && git add -A && git commit -m "Update to latest upstream"' % root
        ]
    }

def common_push(root):
    return {
        'actions': [
            'cd %s/build && git checkout update && git push --force -u origin update' % root,
        ]
    }
