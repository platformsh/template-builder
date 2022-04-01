import os
import json
import yaml 

templates=os.listdir("{}/templates".format(os.getcwd()))
templates.remove("__init__.py")
templates.remove(".DS_Store")

readme_file = "README_test.md"
header_file = "header_test.svg"

def create_header_image(data, destination):
    image_height = 150
    translate_x = image_height/2
    translate_y = image_height/2
    banner_width = 1080
    banner_height = 250
    banner_fill = "#f4f2f3"

    # First create the header graphic.
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


def create_toc():
    content = """
<p align="center">
<strong>Contents</strong>
<br /><br />
<a href="#about"><strong>About</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#getting-started"><strong>Getting started</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#customizations"><strong>Customizations</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#migrating"><strong>Migrating</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contact"><strong>Contact</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#resources"><strong>Resources</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contributing"><strong>Contributing</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<hr>
"""
    return content

def create_about(data):

    description = "\n\n".join(data["description"])
    with open("{}/common/readme/platformsh_desc.md".format(os.getcwd()), "r") as about_psh:
        platform = about_psh.read()
    features = "\n\n-".join(data["features"])


    content = """
## About

{0}

### Features

{1}

### Platform.sh

{2}

""".format(description, features, platform)
    return content


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
                
                readme_destination = "{0}/templates/{1}/files/{2}".format(os.getcwd(), template, readme_file)
                with open(readme_destination, "w") as readme:
                    readme.write(body)




            except yaml.YAMLError as exc:
                print(exc)



