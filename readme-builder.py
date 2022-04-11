import os
import sys
import json
import yaml 

############################################################################################################
# Helpers
############################################################################################################
templates=os.listdir("{}/templates".format(os.getcwd()))
templates.remove("__init__.py")
templates.remove(".DS_Store")
readme_file = "README.md"
header_file = "header.svg"

# Generic read file function.
def read_file(file_location):
    with open(file_location, "r") as data:
        content = data.read()
    return content

############################################################################################################
# Header image
############################################################################################################
# Create the header graphic so we can test template logos that show up in console.
def create_header_image(data, image_destination):
    image_height = 150
    translate_x = image_height/2
    translate_y = image_height/2
    banner_width = 1080
    banner_height = 250
    banner_fill = "#f4f2f3"

    header = """
<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}">
<rect x="0" y="0" width="{0}" height="{1}" fill="#f4f2f3"/>""".format(banner_width, banner_height, banner_fill)

    if len(data["logo"]["images"]) == 2:
        header += """
<image href="{0}" x="40%" y="50%" height="150" transform="translate({2},{3})"/>
<image href="{1}" x="60%" y="50%" height="150" transform="translate({2},{3})"/>
</svg>""".format(data["logo"]["images"][0], data["logo"]["images"][1], str(-1*translate_x), str(-1*translate_x))
    else:
        header += """
<image href="{0}" x="50%" y="50%" height="{1}" transform="translate({2}, {3})"/>
</svg>
""".format(data["logo"]["images"][0], str(image_height), str(-1*translate_x), str(-1*translate_x))

    with open(image_destination, "w") as header_img:
        header_img.write(header)
############################################################################################################
# Header
############################################################################################################
# Create the common header text, with title, CTAs, and badges. 
def create_header(data, template, header_file):
    body = """
<p align="right">
<a href="https://platform.sh">
<img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
</a>
</p>

<p align="center">
<a href="{0}">
<img src="{1}">
</a>
</p>

<h1 align="center">{2}</h1>

<p align="center">
<strong>Contribute, request a feature, or check out our resources</strong>
<br />
<br />
<a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{3}/issues/new?assignees=&labels=bug&template=bug_report.yml"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{3}/issues/new?assignees=&labels=feature+request&template=improvements.yml"><strong>Request a feature</strong></a>
<br /><br />
</p>

<p align="center">
<a href="https://github.com/platformsh-templates/{3}/issues">
<img src="https://img.shields.io/github/issues/platformsh-templates/{3}.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh-templates/{3}.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{3}/blob/master/{4}">
<img src="https://img.shields.io/static/v1?label=License&message={5}&style=for-the-badge&labelColor=f4f2f3&color=ffd9d9" alt="License" />
</a>&nbsp&nbsp
<br /><br />
<a href="https://console.platform.sh/projects/create-project/?template=https://raw.githubusercontent.com/platformsh-templates/{3}/updates/.platform.template.yaml&utm_campaign=deploy_on_platform?utm_medium=button&utm_source=affiliate_links&utm_content=https://raw.githubusercontent.com/platformsh-templates/{3}/updates/.platform.template.yaml" target="_blank" title="Deploy with Platform.sh"><img src="https://platform.sh/images/deploy/deploy-button-lg-blue.svg" width="175px"></a>
</p>
</p>

<hr>
""".format(data["logo"]["link"], header_file, data["title"], template, data["license"]["location"], data["license"]["type"])

    return body

# Table of contents.
def create_toc():
    content = """
<p align="center">
<strong>Contents</strong>
<br /><br />
<a href="#about"><strong>About</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#getting-started"><strong>Getting started</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#migrate"><strong>Migrate</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#learn"><strong>Learn</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contribute"><strong>Contribute</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<hr>
"""
    return content
############################################################################################################
# About
############################################################################################################
# About the template, its features, and a short about Platform.sh.
def create_about(data):

    description = "\n\n".join(data["description"])
    features = "- " + "\n- ".join(data["features"])

    content = """
## About

{0}

### Features

{1}

""".format(description, features)
    return content
############################################################################################################
# Getting started
############################################################################################################
# Quickstart instructions (DoP repeat).
def create_quickstart(template):
    content = """
The quickest way to deploy this template on Platform.sh is by clicking the button below. 
This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/{0}/.platform.template.yaml&utm_content={0}&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>
<br/>
""".format(template)
    return content
# Getting started: Alt deploy options.

def create_project_options(data):
    content = ""
    about_dev_flag = ""

    if "create-project" in data["sections"]:

        if "-s dev" in data["sections"]["create-project"]:
                about_dev_flag = """
> **Note:**    
>
> Platform.sh templates prioritize upstream release versions over our own. Despite this, we update template dependencies on a scheduled basis independent of those upstreams. Because of this, template repos do not contain releases. This may change in the future, but until then the `-s dev` flag is necessary to use `composer create-project`.
"""

        content = """
You can also quickly recreate this project locally with the following command:

```bash
{0}
```

{1}
""".format(data["sections"]["create-project"], about_dev_flag)
    return content

def create_deploy_options():

    direct = read_file("{}/common/readme/deploy_direct.md".format(os.getcwd()))
    github = read_file("{}/common/readme/deploy_github.md".format(os.getcwd()))
    gitlab = read_file("{}/common/readme/deploy_gitlab.md".format(os.getcwd()))
    bitbucket = read_file("{}/common/readme/deploy_bitbucket.md".format(os.getcwd()))

    content = """
{0}
{1}
{2}
{3}
""".format(direct, github, gitlab, bitbucket)
    return content
# Getting started main.
def create_getting_started(template, data):
    quickstart = create_quickstart(template)
    deploy_options = create_deploy_options()
    createProject_options = create_project_options(data)

    content = """
## Getting started

### Deploy

#### Quickstart

{0}

{1}

#### Other deployment options

For all of the other options below, clone this repository first:

```bash
git clone https://github.com/platformsh-templates/{2}
```

If you're trying to deploy from GitHub, you can generate a copy of this repository first in your own namespace by clicking the [Use this template](https://github.com/platformsh-templates/{2}/generate) button at the top of this page. 

Then you can clone a copy of it locally with `git clone git@github.com:YOUR_NAMESPACE/{2}.git`.

{3}

""".format(quickstart, createProject_options, template, deploy_options)
    return content
# Getting started: post-install.
def create_post_install(data):
    defaultContent = ""
    if "postinstall" in data["sections"]:
        return read_file("{0}/{1}".format(os.getcwd(), data["sections"]["postinstall"]))
    return defaultContent
# Getting started: local dev.
def create_local_dev(template, data):
    defaultContent = ""
    if "local" in data["sections"]:

        local_options = ""
        config = data["sections"]["local"]
        for file in data["sections"]["local"]:
            local_options += read_file("{0}/{1}".format(os.getcwd(), file)) + "\n"

        content = """
### Local development

This section provides instructions for running the `{0}` template locally, connected to a live database instance on an active Platform.sh environment.

In all cases for developing with Platform.sh, it's important to develop on an isolated environment - do not connect to data on your production environment when developing locally. 
Each of the options below assume that you have already deployed this template to Platform.sh, as well as the following starting commands:

```bash
$ platform get PROJECT_ID
$ cd project-name
$ platform environment:branch updates
```

{1}

> **Note:**
>
> For many of the steps above, you may need to include the CLI flags `-p PROJECT_ID` and `-e ENVIRONMENT_ID` if you are not in the project directory or if the environment is associated with an existing pull request.

""".format(template, local_options)
        return content
    return defaultContent
# Create customizations.
def create_customizations():
    return """
### Customizations

A number of changes have been made to this repository from its source that you may already be familiar with. 
Configuration files have been added, and other small changes were necessary to deploy on Platform.sh

See [Migrate](#migrate) for more details.
"""
############################################################################################################
# Migrate
############################################################################################################
# Migration: Adding/updating files.
def create_migration_file_descriptions(template, data):

    ignore_files = ["README.md", "README_test.md", "header_test.svg", ".editorconfig"]

    with open("{0}/common/readme/file_ignore.json".format(os.getcwd(), template), 'r') as ignore_file:
        ignore_data=ignore_file.read()

    with open("{0}/migrations/{1}.migrate.json".format(os.getcwd(), template), 'r') as myfile:
        migrate_data=myfile.read()

    ignore_files = json.loads(ignore_data)
    migration_files = json.loads(migrate_data)

    migrate_content = """
|  File | Purpose    |
|:-----------|:--------|
"""

    for file in migration_files["migration"]["files"]["rel_root"]:
        if file not in ignore_files:
            if "migration" in data["sections"]:
                if file in data["sections"]["migration"]["files"]:
                    content = "| [`{0}`]({0}) |".format(file, file)
                    for entry in data["sections"]["migration"]["files"][file]:
                        if isinstance(entry, str):
                            content += " {0}".format(entry)
                        else: 
                            content += " {0}".format(read_file("{0}/{1}".format(os.getcwd(), entry["file"])))
                    migrate_content += content + " |\n"
                else:
                    migrate_content += "| [`{0}`]({0}) |    |\n".format(file)

    return """
{0}
""".format(migrate_content)
# Migrate: getting started.
def create_migration_getting_started(template, data):
    with open("{0}/migrations/{1}.migrate.json".format(os.getcwd(), template), 'r') as myfile:
        migrate_data=myfile.read()
    migration_files = json.loads(migrate_data)
    deps_content = ""
    for commands in migration_files["migration"]["migrate"]["init"]:
        deps_content += "$ {0}\n".format(commands)

    return """

```bash
{0}
```

""".format(deps_content)
# Migrate: dependencies.
def create_migration_dependencies(template, data):
    with open("{0}/migrations/{1}.migrate.json".format(os.getcwd(), template), 'r') as myfile:
        migrate_data=myfile.read()
    migration_files = json.loads(migrate_data)
    deps_content = ""
    for commands in migration_files["migration"]["migrate"]["deps"]:
        deps_content += "$ {0}\n".format(commands)

    return """

```bash
{0}
```

""".format(deps_content)

# Migrate: data.
def create_migration_data(template, data):

    mounts = ""
    for mount in data["sections"]["migration"]["mounts"]:
        mounts += """
$ platform mount:upload -e main --mount {0} --source ./{0}""".format(mount)
    return """
If you are moving an existing site to Platform.sh, then in addition to code you also need to migrate your data. That means your database and your files.

<details>
<summary>Importing the database</summary><br/>

First, obtain a database dump from your current site and save your dump file as `database.sql`. Then, import the database into your Platform.sh site using the CLI:

```bash
platform sql -e main < database.sql
```

</details>
<details>
<summary>Importing files</summary><br/>

You first need to download your files from your current hosting environment. 
The easiest way is likely with rsync, but consult your old host's documentation. 

The `platform mount:upload` command provides a straightforward way to upload an entire directory to your site at once to a `mount` defined in a `.platform.app.yaml` file. 
Under the hood, it uses an SSH tunnel and rsync, so it is as efficient as possible. 
(There is also a `platform mount:download` command you can use to download files later.) 
Run the following from your local Git repository root (modifying the `--source` path if needed and setting `BRANCH_NAME` to the branch you are using).

A few examples are listed below, but repeat for all directories that contain data you would like to migrate.

```bash{0}
```

Note that `rsync` is picky about its trailing slashes, so be sure to include those.

</details>

""".format(mounts)
# Migrate: Main.
def create_migration(template, data):

    getting_started = create_migration_getting_started(template, data)
    file_descriptions = create_migration_file_descriptions(template, data)
    dependencies = create_migration_dependencies(template, data)
    deploy_options = create_deploy_options()
    data_migrate = create_migration_data(template, data)

    return """
## Migrate

The steps below outline the important steps for migrating your application to Platform.sh - adding the required configuration files and dependencies, for example.
Not every step will be applicable to each person's migration.
These steps actually assume the earliest starting point possible - that there is no code at all locally, and that this template repository will be rebuilt completely from scratch.

- [Getting started](#getting-started-1)
- [Adding and updating files](#adding-and-updating-files)
- [Dependencies](#dependencies)
- [Deploying to Platform.sh](#deploying-to-platformsh)
- [Migrating your data](#migrating-your-data)
- [Next steps](#next-steps)

If you already have code you'd like to migrate, feel free to focus on the steps most relevant to your application and skip the first section.

### Getting started

Assuming that your starting point is no local code, the steps below will setup a starting repository we can begin to make changes to to rebuild this template and migrate to Platform.sh. 
If you already have a codebase you are trying to migrate, move onto the next step - [Adding and updating files](#adding-and-updating-files) - and substitute any reference to the default branch `main` with some other branch name.

{0}

### Adding and updating files

A small number of files need to be added to or modified in your repository at this point. 
Some of them explicitly configure how the application is built and deployed on Platform.sh, while others simply modify files you may already have locally, in which case you will need to replicate those changes.

Open the dropdown below to view all of the **Added** and **Updated** files you'll need to reproduce in your migration.

<details>
<summary><strong>View files</strong></summary><br/>

{1}

</details>

### Dependencies and configuration

Sometimes it is necessary to install additional dependencies to and modify the configuration of an upstream project to deploy on Platform.sh. 
When it is, we do our best to keep these modifications to the minimum necessary. 
Run the commands below to reproduce the dependencies in this template. 

{2}

### Deploying to Platform.sh

Your repository now has all of the code it needs in order to deploy to Platform.sh. 

{3}

### Migrating your data

{4}

### Next steps

With your application now deployed on Platform.sh, things get more interesting. 
Run the command `platform environment:branch new-feature` for your project, or open a trivial pull request off of your current branch. 

The resulting environment is an *exact* copy of production.
It contains identical infrastructure to what's been defined in your configuration files, and even includes data copied from your production environment in its services. 
On this isolated environment, you're free to make any changes to your application you need to, and really test how they will behave on production. 

After that, here are a collection of additional resources you might find interesting as you continue with your migration to Platform.sh:

- [Local development](#local-development)
- [Troubleshooting](#troubleshooting)
- [Adding a domain and going live](https://docs.platform.sh/domains/steps.html)
- [(CDN) Content Delivery Networks](https://docs.platform.sh/domains/cdn.html)
- [Performance and observability with Blackfire.io](https://docs.platform.sh/integrations/observability/blackfire.html)
- [Pricing](https://docs.platform.sh/overview/pricing.html)
- [Security and compliance](https://docs.platform.sh/security.html)

""".format(getting_started, file_descriptions, dependencies, deploy_options, data_migrate)
############################################################################################################
# Learn
############################################################################################################
# Learn: Troubleshooting
def create_troubleshooting(data):

    troubleshoot_content = ""
    if "troubleshoot" in data["sections"]:
        for file in data["sections"]["troubleshoot"]:
            troubleshoot_content += """
{0}
""".format(read_file("{0}/{1}".format(os.getcwd(), file["file"])))

    return troubleshoot_content
# Learn: Resources
def create_resources(template, data):
    if "resources" in data["sections"]:  
        resource_links = ""
        for resource in data["sections"]["resources"]:
            resource_links += "- {0}\n".format(resource)
        content = """
{0}
""".format(resource_links)
        return content
    return ""
# Learn: Contact
def create_contact():
    return read_file("{0}/{1}".format(os.getcwd(), "common/readme/contact.md"))
# Learn: About Platform.sh.
def create_about_platformsh():
    return read_file("{0}/{1}".format(os.getcwd(), "common/readme/platformsh_desc.md"))
def create_metrics(data):
    content = ""
    if "metrics" in data["sections"]:
        if data["sections"]["metrics"] == True:
            content = read_file("{0}/{1}".format(os.getcwd(), "common/readme/metrics.md"))
    return content

def create_blackfire(data):
    content = ""
    if "blackfire" in data["sections"]:
        if data["sections"]["blackfire"] == True:
            content = read_file("{0}/{1}".format(os.getcwd(), "common/readme/blackfire.md"))
    return content
def create_learn(template, data):
    troubleshooting = create_troubleshooting(data)
    metrics = create_metrics(data)
    blackfire = create_blackfire(data)
    resources = create_resources(template, data)
    contact = create_contact()
    about_platformsh = create_about_platformsh()
    return """
## Learn

### Troubleshooting

{0}

{1}

{2}

### Resources

{3}

### Contact

{4}

### About Platform.sh

{5}
""".format(troubleshooting, metrics, blackfire, resources, contact, about_platformsh)
############################################################################################################
# Contribute
############################################################################################################
# Contributing
def create_contributing(template):

    content = """

## Contributing

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<p align="center">
<strong>How to contribute</strong>
<br /><br />
<a href="https://github.com/platformsh-templates/{0}/issues/new?assignees=&labels=bug&template=bug_report.yml"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{0}/issues/new?assignees=&labels=feature+request&template=improvements.yml"><strong>Submit a feature request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{0}/pulls"><strong>Open a pull request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<p align="center">
<strong>Need help?</strong>
<br /><br />
<a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>
<br/>
<p align="center">
<a href="https://github.com/platformsh-templates/drupal9/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=platformsh-templates/drupal9" />
</a>
</p>

<p align="center">
<em>Made with <a href="https://contrib.rocks">contrib.rocks</a><em>
</p>

<br />
""".format(template)
    return content
############################################################################################################
# Main loop through all templates (if info.yaml file is present).
############################################################################################################
def generate_readme(template):
    info_file = "{0}/templates/{1}/info/info.yaml".format(os.getcwd(), template)
    if os.path.isfile(info_file):
        print("\n{0}".format(template))
        print("- Build readme")

        with open(info_file) as file:
            try:
                data = yaml.safe_load(file)

                # First create the header image.
                image_destination = "{0}/templates/{1}/files/{2}".format(os.getcwd(), template, header_file)
                create_header_image(data, image_destination)
                # Header.
                body = create_header(data, template, header_file)
                body += create_toc()
                # About.
                body += create_about(data)
                # Getting started.
                body += create_getting_started(template, data)
                body += create_post_install(data)
                body += create_local_dev(template, data)
                # Migrate.
                body += create_migration(template, data)
                # Learn.
                body += create_learn(template, data)
                # Contribute.
                body += create_contributing(template)
                
                readme_destination = "{0}/templates/{1}/files/{2}".format(os.getcwd(), template, readme_file)
                with open(readme_destination, "w") as readme:
                    readme.write(body)

            except yaml.YAMLError as exc:
                print(exc)
def run(args):
    if len(args) > 1:
        template = args[1]
        generate_readme(template)
    else:
        for template in templates:
            generate_readme(template)

if __name__ == "__main__":
    run(sys.argv)
