# Basic Python 3 for Platform.sh

This template provides the most basic configuration for running a custom Python 3.7 project.  It launches a Python application directly rather than using a runner.

Python is a general purpose scripting language often used in web development.

## Services

* Python 3.7.

## Customizations

The following files are of particular importance.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.

## References

* [Python](https://www.python.org/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
