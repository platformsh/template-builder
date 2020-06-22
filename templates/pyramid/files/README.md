# Pyramid for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/pyramid/.platform.template.yaml&utm_content=pyramid&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Pyramid on Platform.sh.  It includes a minimalist application skeleton that demonstrates how to connect to a MariaDB server for data storage and Redis for caching.  It is intended for you to use as a starting point and modify for your own needs.

Pyramid is a web framework written in Python.

## Features

* Python 3.8
* MariaDB 10.4
* Redis 5.0
* Automatic TLS certificates
* Pipfile-based build

## Post-installation

The `app.py` file includes example controllers that demonstrate accessing services within the application.  Feel free to replace them with your own code as appropriate.

## Customizations

The following changes have been made relative to Pyramid as it is downloaded from the Pyramid website.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.

## References

* [Pyramid](https://trypyramid.com/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
