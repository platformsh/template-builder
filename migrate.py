# test.py in template-builder root

import os
import json
import dodo
from datetime import datetime

def get_templates_list():

    templates_path = "{0}/templates".format(os.getcwd())
    with os.scandir(templates_path) as p:
        for entry in p:
            if entry.is_dir():
                yield entry.name

def document_migration_steps(template):

    mypath = "{0}/templates/{1}/files".format(os.getcwd(), template)
    template_link = 'https://raw.githubusercontent.com/platformsh/template-builder/master/'

    def get_files(path, depth):
        """Retrieve files added to upstream templates."""
        depth -= 1
        with os.scandir(path) as p:
            for entry in p:
                file_link = entry.path.replace("{0}/".format(mypath),template_link)
                yield file_link
                if entry.is_dir() and depth > 0:
                    yield from get_files(entry.path, depth)

    def get_commands(data):
        # data = dodo.project_factory(template).update
        commands = []
        for item in data:
            if isinstance(item, str):
                # if 'echo' not in item and 'git' not in item and 'rsync' not in item:
                    if "&&" in item:
                        if len(item.split(" && ")) == 2:
                            # new_item = item.split(" && ")[1]
                            commands.append(item.split(" && ")[1])
                            # print(new_item)
                            # if 'composer require' in new_item or 'composer update' in new_item:
                            #     commands.append(new_item.split(" --")[0])
                            # else:
                            #     commands.append(item.split(" && ")[1])
                    else:
                        commands.append(item)
        return commands

    'cleanup', 'init', 'update', 'platformify', 'branch', 'push'

    def get_cleanup_commands():
        return get_commands(dodo.project_factory(template).cleanup)

    def get_init_commands():
        return get_commands(dodo.project_factory(template).init)

    def get_update_commands():
        return get_commands(dodo.project_factory(template).update)

    def get_platformify_commands():
        return get_commands(dodo.project_factory(template).platformify)

    def get_branch_commands():
        return get_commands(dodo.project_factory(template).branch)

    def get_push_commands():
        return get_commands(dodo.project_factory(template).push)

    # Files.
    migrate_files = list(get_files(mypath, 10))

    # Commands.
    cleanup_commands = get_cleanup_commands()
    init_commands = get_init_commands()
    update_commands = get_update_commands()
    platformify_commands = get_platformify_commands()
    branch_commands = get_branch_commands()
    push_commands = get_push_commands()

    try:
        major_version = dodo.project_factory(template).major_version
    except:
        major_version = None
    try:
        remote = dodo.project_factory(template).remote
    except:
        remote = None
    try:
        imageType = dodo.project_factory(template).type
    except:
        imageType = None
    try:
        imageTypeVersion = dodo.project_factory(template).typeVersion
    except:
        imageTypeVersion = None

    data = {
        "template": template,
        "type": imageType,
        "type_version": imageTypeVersion,
        "remote": {
            "major_version": major_version,
            "repository": remote,    
        },
        "last_updated_on": datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),
        "migration": {
            "files": migrate_files,
            "commands": [
                *cleanup_commands, 
                *init_commands, 
                *update_commands, 
                *platformify_commands,
                *branch_commands,
                *push_commands
            ]
        }
    }

    json_data=json.dumps(data, indent = 4)
    projectType = "remote"
    if remote == None:
        projectType = "basic"
    with open("{0}/migrations/{1}/{2}.migrate.json".format(os.getcwd(), projectType, template), "w") as outfile:
        outfile.write(json_data)

def run():
    templates = list(get_templates_list())
    for template in templates:
        document_migration_steps(template)

    # default_attributes = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_platformify', 'branch', 'builddir', 'cleanup', 'commitMessage', 'composer_defaults', 'init', 'latest_tag', 'major_version', 'name', 'package_update_actions', 'platformify', 'push', 'remote', 'type', 'typeVersion', 'update', 'updateBranch', 'updateCommands']
    # l_func = lambda x, y: list((set(x)- set(y))) + list((set(y)- set(x))) 
    # non_match = l_func(default_attributes, dir(dodo.project_factory('wordpress-composer')))
    # print(non_match)
    # print(dodo.project_factory('wordpress-composer').wp_modify_composer)


if __name__ == "__main__":
    run()