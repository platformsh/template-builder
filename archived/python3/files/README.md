# Basic Python 3 for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/python3/.platform.template.yaml&utm_content=python3&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides the most basic configuration for running a custom Python 3.7 project.  It includes the `platformshconfig` package and demonstrates using it to connect to MariaDB and Redis.  It can be used to build a very rudimentary application but is intended primarily as a documentation reference.  The application starts as a bare Python process with no separate runner.

Python is a general purpose scripting language often used in web development.

## Features

* Python 3.8
* MariaDB 10.4
* Redis 5.0
* Automatic TLS certificates
* Pipfile-based build

## Customizations

The following files are of particular importance.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.

## References

* [Python](https://www.python.org/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
