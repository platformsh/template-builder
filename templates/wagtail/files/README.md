# Wagtail Django CMS template for Platform.sh

This project provides a starter kit for Wagtail projects hosted on Platform.sh. It is primarily an example, although could be used as the starting point for a real project.

Notice specifically the `settings.py` where we read some of the environment variables and configure Django
to connect to the correct database, and run in Debug mode when not running the `master` branch.

In this example we are running Wagtail with Gunicorn. You can check-out other examples to see it run with
other application servers.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it! You now have a working "hello world" level project you can build on.

You can create an admin user for the template after your first deployment with 

```python
python manage.py createsuperuser
```

and then log into the Wagtail admin section at

```bash
https://master-7rqtwti-<project id>.<region>.platformsh.site/cms
```

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.
