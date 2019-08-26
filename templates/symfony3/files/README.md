# Symfony 3 for Platform.sh

This template provides a basic Symfony 3 skeleton.  It is configured for Production mode by default so the usual Symfony "welcome" page will not appear.

Symfony is a high-performance loosely-coupled PHP web development framework.  Version 3 is the legacy support version.

## Services

* PHP 7.3
* MariaDB 10.2

## Post-install

1. This is a bare, empty Symfony project.  That means there will be no installation page after the site is deployed.

## Customizations

The following changes have been made relative to a plain Symfony 3 project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platformsh.php`.  That will load a PHP file rather than YAML file to specify Symfony configuration parameters.
* [`parameters_platformsh.php`](/app/config/parameters_platformsh.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters. This file will be parsed on every page load. By default it only maps a default database and Elasticsearch connection parameters. You can add to it as needed.
* [`parameters.yml.dist`](/app/config/parameters.yml.dist) - This file is modified so the install process can retrieve the database connection parameters, SwiftMailer can connect to the correct host and the initial data set is set to `minimal`.
* Due to a bug in Doctrine, the database version must be specified explicitly in `parameters.yml` or this project will fail to deploy.  It is already set.  Remember to update this file if you change the database version used in `services.yaml`.

## References

* [Symfony](https://symfony.com/)
* [Symfony on Platform.sh](https://docs.platform.sh/frameworks/symfony.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
