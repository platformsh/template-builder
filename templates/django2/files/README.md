# Django 2 for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/django2/.platform.template.yaml&utm_content=django2&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template deploys the Django 2 application framework on Platform.sh, using the gunicorn application runner.  It also includes a PostgreSQL database connection pre-configured.

New projects should be built using Django 3, but this project is a reference for existing migrating sites.  Version 2 is in legacy support.

## Features

* Python 3.8
* PostgreSQL 12
* Automatic TLS certificates
* Pipfile-based build

## Customizations

The following files have been added to a basic Django configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Pip library, [`platformshconfig`](https://github.com/platformsh/config-reader-python), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A rudimentary `myapp` application is included for demonstration purposes.  In particular, the `settings.py` file is set up to configure Django to connect to the correct database, and run in Debug mode when not running the `master` branch.  You are free to change that configuration if you prefer.

## References

* [Django](https://www.djangoproject.com/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
