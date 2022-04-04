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
                if not entry.is_dir():
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

    # 'cleanup', 'init', 'update', 'platformify', 'branch', 'push'

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
    migrate_trimmed_files = []
    migrate_rel = []
    if len(migrate_files) > 0:
        migrate_trimmed_files = ["https://raw.githubusercontent.com/platformsh-templates/{0}/master/{1}".format(template, file.split("template-builder/master/")[1]) for file in migrate_files]
        migrate_rel = [file.split("template-builder/master/")[1] for file in migrate_files]

    # Commands.
    cleanup_commands = get_cleanup_commands()
    init_commands = get_init_commands()
    update_commands = get_update_commands()
    platformify_commands = get_platformify_commands()
    branch_commands = get_branch_commands()
    push_commands = get_push_commands()

    dependencies = [command.split(" --")[0] for command in [*platformify_commands] if "composer require" in command]

    try:
        major_version = dodo.project_factory(template).major_version
    except:
        major_version = dodo.project_factory(template).upstream_branch
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
            "files": {
                "rel_template": migrate_trimmed_files,
                "rel_tb": migrate_files,
                "rel_root": migrate_rel
            },
            "commands": {
                "cleanup": [*cleanup_commands],
                "init": [*init_commands],
                "update": [*update_commands],
                "platformify": [*platformify_commands],
                "branch": [*branch_commands],
                "push": [*push_commands]
            },
            "migrate": {
                "init": [
                    "mkdir {0} && cd {0}".format(template),
                    "git init",
                    "git remote add upstream {0}".format(dodo.project_factory(template).remote),
                    "git checkout main",
                    "git fetch --all --depth=2",
                    "git fetch --all --tags",
                    "git merge --allow-unrelated-histories -X theirs {0}".format(major_version)
                ],
                "deps": dependencies
            }
        }
    }

    json_data=json.dumps(data, indent = 4)
    projectType = "remote"
    if remote == None:
        projectType = "basic"
    with open("{0}/migrations/{1}.migrate.json".format(os.getcwd(), template), "w") as outfile:
        outfile.write(json_data)

def run():
    templates = list(get_templates_list())
    ignore_templates = ['wordpress-vanilla']
    for template in templates:
        try:
            remote = dodo.project_factory(template).remote
        except:
            remote = None
        if remote is not None:
            if template not in ignore_templates:
                document_migration_steps(template)

if __name__ == "__main__":
    run()
