# Sculpin for Platform.sh

This template provides a basic Sculpin skeleton.  All files are generated at build time, so at runtime only static files need to be served.

## Services

* PHP 7.3

## Customizations

The following changes have been made relative to a plain Symfony 3 project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
