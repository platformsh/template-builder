# Pyramid for Platform.sh

This template builds Pyramid on Platform.sh.  It includes some basic example code to demonstrate how to connect to the database.

Pyramid is a web framework written in Python.

## Services

* Python 3.7
* MariaDB 10.2
* Redis 3.2

## Post-installation

The `app.py` file includes example controllers that demonstrate accessing services within the application.  Feel free to replace them with your own code as appropriate.

## Customizations

The following changes have been made relative to Pyramid as it is downloaded from the Pyramid website.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.

## References

* [Pyramid](https://trypyramid.com/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
