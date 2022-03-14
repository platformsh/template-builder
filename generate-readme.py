# test.py in template-builder root

import os
import yaml
# import json
# import dodo
# from datetime import datetime

def get_templates_list():

    templates_path = "{0}/templates".format(os.getcwd())
    with os.scandir(templates_path) as p:
        for entry in p:
            if entry.is_dir():
                yield entry.name

def build_readme(template):

    with open("{0}/templates/{1}/meta.yaml".format(os.getcwd(), template), "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
        print(data['info']['title'])

    # Define the header
    #   Need: template repo, logo, logo link, title, LICENSE location
    body = """
<br />
<p align="left">
    <a href="https://platform.sh">
        <img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
    </a>
</p>
<br /><br />
<p align="center">
    <a href="{0}">
        <img src="{1}" width="300">
    </a>
</p>

<h1 align="center">{2}</h1>

<p align="center">
    <strong>Contribute to the Platform.sh knowledge base, or check out our resources</strong>
    <br />
    <br />
    <a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Request a feature</strong></a>
    <br /><br />
</p>

<p align="center">
    <a href="https://github.com/platformsh-templates/metabase/issues">
        <img src="https://img.shields.io/github/issues/platformsh-templates/nextjs-strapi.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/pulls">
        <img src="https://img.shields.io/github/issues-pr/platformsh-templates/nextjs-strapi.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/blob/master/LICENSE">
        <img src="https://img.shields.io/static/v1?label=License&message=MIT&style=flat-square&labelColor=f4f2f3&color=ffd9d9" alt="License" />
    </a>&nbsp&nbsp
    <br /><br /><br />
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextjs-strapi/.platform.template.yaml&utm_content=nextjs-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="175px" />
    </a>
</p>
</p>

<hr>
<br />
""".format(
    data['info']['logo']['link'],
    data['info']['logo']['src'],
    data['info']['title'],
)

    with open("{0}/templates/{1}/README.md".format(os.getcwd(), template), "w") as outfile:
        outfile.write(body)


def run():
    templates = list(get_templates_list())
    for template in templates:
        if template == 'wordpress-woocommerce':
            build_readme(template)
        # document_migration_steps(template)

    # default_attributes = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_platformify', 'branch', 'builddir', 'cleanup', 'commitMessage', 'composer_defaults', 'init', 'latest_tag', 'major_version', 'name', 'package_update_actions', 'platformify', 'push', 'remote', 'type', 'typeVersion', 'update', 'updateBranch', 'updateCommands']
    # l_func = lambda x, y: list((set(x)- set(y))) + list((set(y)- set(x))) 
    # non_match = l_func(default_attributes, dir(dodo.project_factory('wordpress-composer')))
    # print(non_match)
    # print(dodo.project_factory('wordpress-composer').wp_modify_composer)


if __name__ == "__main__":
    run()
