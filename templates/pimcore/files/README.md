# Pimcore for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/pimcore/.platform.template.yaml&utm_content=pimcore&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Pimcore 5 on Platform.sh.  It comes pre-installed with a MariaDB database connecting through Doctrine and Redis for caching via a custom configuration file.  It will self-install on the first deploy.

Pimcore is a Symfony-based Digital Experience Platform.

## Features

* PHP 7.4
* MariaDB 10.4
* Redis 5
* Automatic TLS certificates
* Composer-based build

## Post-install

1. This template installs Pimcore with a default `admin` user with password `admin`.  **You must login and change this immediately.**

2. Once the site has been installed and the password changed, you may optionally modify the `deploy` hook in `.platform.app.yaml` and remove the install block.  It's the part wrapped in a bash `if` statement that includes the default user and password.

## Customizations

The following changes have been made relative to a vanilla Pimcore install.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* The Doctrine ORM has been included out of the box.
* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platformsh.php`.  That will load a PHP file rather than YAML file to specify Pimcore configuration parameters.  It also enables Doctrine and Redis caching.  Due to a bug in Doctrine, the database version must be specified explicitly in `config.yml` or this project will fail to deploy.  It is already set.  Remember to update this file if you change the database version used in `config.yaml`.
* [`parameters_platformsh.php`](/app/config/parameters_platformsh.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters. This file will be parsed on every page load. By default it only maps a default database and Redis connection parameters. You can add to it as needed.
* [`installer.yml`](/app/config/installer.yml) - This file is modified so the install process can retrieve the database connection parameters.

## References

* [Pimcore](https://pimcore.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
