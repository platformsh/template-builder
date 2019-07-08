# Django 1 LTS for Platform.sh

This template builds Django 1 on Platform.sh, using the gunicorn application runner.  New projects should be built using Django 2, but this project is a reference for existing migrating sites.

Django is a Python-based web application framework with a built-in ORM.  Version 1 is the legacy support version.

## Services

* Python 2.7
* PostgreSQL 10

## Customizations

The following files have been added to a basic Django configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Pip library, [`platformshconfig`](https://github.com/platformsh/config-reader-python), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A rudimentary `myapp` application is included for demonstration purposes.  In particular, the `settings.py` file is set up to configure Django to connect to the correct database, and run in Debug mode when not running the `master` branch.  You are free to change that configuration if you prefer.

## References

* [Django](https://www.djangoproject.com/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
