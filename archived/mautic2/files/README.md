# Mautic for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/mautic/.platform.template.yaml&utm_content=mautic&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides a basic Mautic installation.  It includes MariaDB for storage, which will be auto-selected during the installer.  It also includes a RabbitMQ queue server that may be enabled manually post-install.

Mautic is an Open Source marketing automation tool built on Symfony.

## Features

* PHP 7.2
* MariaDB 10.4
* RabbitMQ 3.7
* Automatic TLS certificates
* Composer-based build

## Post-install

Because Mautic uses the same `local.php` file for service connections and user configuration, it requires some special handling.  On first load the installer will appear as normal.  The database configuration step will be pre-filled with the correct values.  Accept them as is and then proceed with the rest of the installation.

This template ships with RabbitMQ, but Mautic will need to be configured to use it.  The [Mautic documentation](https://www.mautic.org/docs/en/queue/index.html) explains how to do so.  To get the correct values to use you will need to check the Platform.sh `RELATIONSHIPS` variable.  If you have the [Platform.sh CLI](https://docs.platform.sh/development/cli.html) installed, the easiest way to do that is with the following command:

`platform relationships -p XXXXX`

Where `XXXXX` is the ID of your project.  That will list two relationships, `database` and `rabbitmqqueue`.  Use the host, user, and password of the second to fill out the RabbitMQ form in Mautic.

## Customizations

The following changes have been made relative to a plain Mautic project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* [`local.php`](/app/config/local.php) - Normally this file is written by Mautic's installer.  However, the `/app/config` directory is read-only on Platform.sh.  Instead, during the build process that file is pre-created as a symbolic link to a file in the `/persistent` writeable mount directory, allowing it to be writeable.
* [`platformsh_local.php`](/platformsh_local.php) - This is the initial `local.php` file which is copied to `/persistent` on the first deploy.  It contains the appropriate code to provide default values to the Mautic installer for the database connection.  However, the installer will overwrite it with its own static version.
* `AppKernel.php` has been patched to use a RAM disk for the file cache.  That's because Doctrine's normal file cache behavior is [incompatible with encrypted disks](https://github.com/doctrine/cache/issues/176).
* The `.gitignore` file that comes with Mautic has been modified to not ignore files that begin with `.`.  (That would exclude the Platform.sh configuration files.)

## References

* [Mautic](https://www.mautic.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
