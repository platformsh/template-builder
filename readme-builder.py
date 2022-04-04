import os
import json
import yaml 

templates=os.listdir("{}/templates".format(os.getcwd()))
templates.remove("__init__.py")
templates.remove(".DS_Store")

readme_file = "README_test.md"
header_file = "header_test.svg"

# Generic read file function.
def read_file(file_location):
    with open(file_location, "r") as data:
        content = data.read()
    return content

# Create the header graphic so we can test template logos.
def create_header_image(data, destination):
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
<a href="https://github.com/platformsh-templates/{3}/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{3}/issues"><strong>Request a feature</strong></a>
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


# About
# Deploy
# Migrate
# Learn
    # Resources
    # About Platform.sh
# Contribute
# Contact


# Table of contents.
def create_toc():
    content = """
<p align="center">
<strong>Contents</strong>
<br /><br />
<a href="#about"><strong>About</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#getting-started"><strong>Getting started</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#migration"><strong>Migration</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contact"><strong>Contact</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#resources"><strong>Resources</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contributing"><strong>Contributing</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<hr>
"""
    return content

# About the template, its features, and a short about Platform.sh.
def create_about(data):

    description = "\n\n".join(data["description"])
    with open("{}/common/readme/platformsh_desc.md".format(os.getcwd()), "r") as about_psh:
        platform = about_psh.read()
    
    features = "- " + "\n- ".join(data["features"])


    content = """
## About

{0}

### Features

{1}

### Platform.sh

{2}

""".format(description, features, platform)
    return content

# Quickstart instructions (DoP repeat).
def create_quickstart(template):
    content = """
The quickest way to deploy this template on Platform.sh is by clicking the button below. This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/{0}/.platform.template.yaml&utm_content={0}&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>

> **Note:**
>
> If you do not already have a Platform.sh account, you will be asked to fill out some basic information, after which you will be given a 30-day free trial to experiment with our platform.
""".format(template)
    return content

# Getting started.
def create_getting_started(template):
    quickstart = create_quickstart(template)

    content = """
## Getting started

### Deploy

#### Quickstart

{0}
""".format(quickstart)
    return content

# Getting started: Alt deploy options.
def create_deploy_options(template):

    direct = read_file("{}/common/readme/deploy_direct.md".format(os.getcwd()))
    github = read_file("{}/common/readme/deploy_github.md".format(os.getcwd()))
    gitlab = read_file("{}/common/readme/deploy_gitlab.md".format(os.getcwd()))
    bitbucket = read_file("{}/common/readme/deploy_bitbucket.md".format(os.getcwd()))

    content = """
#### Other deployment options

<details>
<summary>Deploy directly to Platform.sh from the command line</summary><br />

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/{0}
   ```

{1}

</details>

<details>
<summary>Deploy from GitHub</summary><br />

If you would instead to deploy this template from your own repository on GitHub, you can do so through the following steps.

> **Note:**
>
> You can find the full [GitHub integration documentation here](https://docs.platform.sh/integrations/source/github.html).

1. Clone this repository:

   Click the [Use this template](https://github.com/platformsh-templates/{0}/generate) button at the top of this page to create a new repository in your namespace containing this demo. Then you can clone a copy of it locally with `git clone git@github.com:YOUR_NAMESPACE/{0}.git`.

{2}

</details>

<details>
<summary>Deploy from GitLab</summary><br />

If you would instead to deploy this template from your own repository on GitLab, you can do so through the following steps.

> **Note:**
>
> You can find the full [GitLab integration documentation here](https://docs.platform.sh/integrations/source/gitlab.html).

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/{0}
   ```

{3}

</details>

<details>
<summary>Deploy from Bitbucket</summary><br />

If you would instead to deploy this template from your own repository on Bitbucket, you can do so through the following steps.

> **Note:**
>
> You can find the full [Bitbucket integration documentation here](https://docs.platform.sh/integrations/source/bitbucket.html).

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/{0}
   ```

{4}

</details>

""".format(template, direct, github, gitlab, bitbucket)

    return content


def create_post_install(data):
    defaultContent = ""
    if "postinstall" in data["sections"]:
        return read_file("{0}/{1}".format(os.getcwd(), data["sections"]["postinstall"]))
    return defaultContent

def create_local_dev(template, data):
    defaultContent = ""
    if "local" in data["sections"]:

        local_options = ""
        config = data["sections"]["local"]
        for file in data["sections"]["local"]:
            local_options += read_file("{0}/{1}".format(os.getcwd(), file))


        content = """
### Local development

This section provides instructions for running the `{0}` template locally, connected to a live database instance on an active Platform.sh environment.

In all cases for developing with Platform.sh, it's important to develop on an isolated environment - do not connect to data on your production environment when developing locally. Each of the options below assume the following starting point:

```bash
platform get PROJECT_ID
cd project-name
platform environment:branch updates
```

> **Note:**
>
> For many of the steps below, you may need to include the CLI flags `-p PROJECT_ID` and `-e ENVIRONMENT_ID` if you are not in the project directory or if the environment is associated with an existing pull request.

{1}

""".format(template, local_options)
        return content
    return defaultContent

def create_migration_file_descriptions(template, data):

    ignore_files = ["README.md", "README_test.md", "header_test.svg", ".editorconfig"]

    with open("{0}/migrations/{1}.migrate.json".format(os.getcwd(), template), 'r') as myfile:
        migrate_data=myfile.read()

    migration_files = json.loads(migrate_data)

    migrate_content = """
| File          | Purpose    |
|:--------------|:-----------|
"""

    for file in migration_files["migration"]["files"]["rel_root"]:
        if file not in ignore_files:
            if "migration" in data["sections"]:
                if file in data["sections"]["migration"]:
                    content = "| **[`{0}`]({0}):** |".format(file, file)
                    for entry in data["sections"]["migration"][file]:
                        if isinstance(entry, str):
                            content += " {0}".format(entry)
                        else: 
                            content += " {0}".format(read_file("{0}/{1}".format(os.getcwd(), entry["file"])))
                    migrate_content += content + " |\n"
                else:
                    migrate_content += "| **[`{0}`]({0})** |   |\n".format(file)

    return """
{0}
""".format(migrate_content)

def create_migration(template, data):

    file_descriptions = create_migration_file_descriptions(template, data)

    return """
## Migration

If you would like to migrate your own project to Platform.sh, the following steps will help you to do so. 
For context, this template was generated from a central tool, most likely from an upstream open source project repository. 
Platform.sh uses this management tool to retrieve an upstream, after which a few modifications are made that allows it deploy successfully on our platform.

The steps below outline the important parts of this process - adding files and dependencies, for example.
Not every step will be applicable to each person's migration.
These steps actually assume the earliest starting point possible - that there is no code at all locally, and that this template repository will be built completely from scratch by you. 
If you already have code you'd like to migrate, feel free to focus on the steps most relevant to your application.

### Starting out

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor.

### Necessary files

A small number of files need to be added to or modified in your repository at this point. 
Some of them explicitly configure how the application is built and deployed on Platform.sh, while others simply modify files you may already have locally, in which case you will need to replicate those changes.

{0}

### Additional dependencies

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor.

""".format(file_descriptions)

# Resources
def create_resources(template, data):
    if "resources" in data["sections"]:  
        resource_links = ""
        for resource in data["sections"]["resources"]:
            resource_links += "- {0}\n".format(resource)
        content = """

## Resources

{0}

""".format(resource_links)
        return content
    return ""

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
<a href="https://github.com/platformsh-templates/{0}/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/{0}/issues"><strong>Submit a feature request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
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
for template in templates:
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

                # Then build the README.
                body = create_header(data, template, header_file)
                body += create_toc()
                body += create_about(data)
                body += create_getting_started(template)
                body += create_deploy_options(template)
                body += create_post_install(data)
                body += create_local_dev(template, data)
                body += create_migration(template, data)
                body += read_file("{0}/{1}".format(os.getcwd(), "common/readme/contact.md"))
                body += create_resources(template, data)
                body += create_contributing(template)
                
                readme_destination = "{0}/templates/{1}/files/{2}".format(os.getcwd(), template, readme_file)
                with open(readme_destination, "w") as readme:
                    readme.write(body)

            except yaml.YAMLError as exc:
                print(exc)
