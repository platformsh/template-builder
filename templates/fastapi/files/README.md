# FastAPI for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/fastapi/.platform.template.yaml&utm_content=fastapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building the FastAPI framework for Platform.sh.  It includes a minimalist application skeleton that demonstrates how to connect to a MariaDB server for data storage and Redis for caching.  The application starts as a bare Python process with no separate runner.  It is intended for you to use as a starting point and modify for your own needs.

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features

* Python 3.11
* MariaDB 10.4
* Redis 5.0
* Automatic TLS certificates
* Pipfile-based build

## Customizations

The following files have been added to a basic FastAPI configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* A rudimentary application is included in `server.py` for demonstration purposes.  It shows the basic process of starting the server and connecting to the MariaDB database.  Modify and replace it as desired.

## References

* [FastAPI](https://fastapi.tiangolo.com/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
