# Shopware for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/shopware/.platform.template.yaml&utm_content=shopware&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Shopware on Platform.sh using Composer.

Shopware is a PHP-based ecommerce system.

## Services

* PHP 7.3
* MariaDB 10.4

## Post-install

1. The first time the site is deployed, Shopware's command line installer will run and initialize the database.  It will not run again unless the `installer/.platform.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`admin`.  **You need to change this password immediately. Not doing so is a security risk**.

## Customizations

This project is built on the [Shopware/Composer-Project](https://github.com/shopware/composer-project) package, which wraps Shopware and makes it usable with Composer.  All plugins MUST be installed through Composer.  The in-browser plugin manager will not work as the disk is read-only.

The following changes have been made relative to a plain Shopware Composer project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* The Shopware/Composer-Project's `composer.json` file includes scripts that run on install and update.  Those have been removed as they require a `.env` to exist, which is not possible on Platform.sh.
* The [`platformsh-env.php`](platformsh-env.php) file will map Platform.sh environment variables to the enviroment variables expected by Shopware/Composer-Project.  It is auto-included from `composer.json` as part of the autoload process.
* The [`platformsh-db-url.php`](platformsh-db-url.php) script is used only during the install process to provide the installer with database credentials.  It may be removed post-install if desired.
* The build hook calls the [`deploy/build.sh`](deploy/build.sh) script, as it is rather long.

## References

* [Shopware](https://www.shopware.com/en/)
* [Shopware Composer-Project](https://github.com/shopware/composer-project)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
