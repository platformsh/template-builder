# Wagtail for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/wagtail/.platform.template.yaml&utm_content=wagtail&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds the Wagtail CMS on Platform.sh, using the gunicorn application runner.  It includes a PostgreSQL database that is configured automatically, and a basic demonstration app that shows how to use it.  It is intended for you to use as a starting point and modify for your own needs.  You will need to run the command line installation process by logging into the project over SSH after the first deploy.

Wagtail is a web CMS built using the Django framework for Python.

## Features

* Python 3.8
* PostgreSQL 12
* Automatic TLS certificates
* Pipfile-based build

## Post-installation

After installation, you will need to create the initial administrative user.

1. SSH into the project using `platform ssh` (if you have checked out a copy of the repository), or using the SSH login URL provided in the web console.

2. Run:

```python
python manage.py createsuperuser
```

That will create the initial user and provide you with the admin password.

3. Login to the Wagtail admin section at the `/cms` URL for your project.

## Customizations

The following files have been added to a basic Django configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Pip library, [`platformshconfig`](https://github.com/platformsh/config-reader-python), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A rudimentary `myapp` application is included for demonstration purposes.  In particular, the `settings.py` file is set up to configure Django to connect to the correct database, and run in Debug mode when not running the `master` branch.  You are free to change that configuration if you prefer.

## References

* [Wagtail](https://wagtail.io/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
