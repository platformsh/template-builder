# Platform.sh Python 3 minimal example

This project provides a starter kit for minimal Python 3 projects hosted on Platform.sh. Multiple Python 3 [versions](https://docs.platform.sh/languages/python.html#supported-versions) are supported. It is primarily an example, although could be used as the starting point for a real project.

Notice specifically the `server.py` where we read some of the environment variables and configure the App
to connect to the correct database and to a redis instance.

In this example we are not running any application server but the python script directly, you can check-out other examples to see it run with application servers such as Gunicorn.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.
