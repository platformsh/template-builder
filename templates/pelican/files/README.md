# Pelican for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/pelican/.platform.template.yaml&utm_content=pelican&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides a basic Pelican skeleton.  Only content files need to be committed, as Pelican itself is downloaded at build time via the Pipfile.  All files are generated at build time, so at runtime only static files need to be served.

Pelican is a static site generator written in Python and using Jinja for templating.

## Features

* Python 3.8
* Automatic TLS certificates
* Pipfile-based build

## Customizations

The following changes have been made relative to a plain Pelican project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.

## References

* [Moin Moin](https://moinmo.in/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
