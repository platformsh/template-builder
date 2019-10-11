# TYPO3 for Platform.sh

This template builds the TYPO3 CMS for Platform.sh.

TYPO3 is a Content Management System (CMS) built in PHP.

## Services

* PHP 7.3
* MariaDB 10.4
* Redis 5.0

## Post-install

1. The first time the site is deployed, a custom installer will initialize the database and create an initial user.  It will not run again unless the `installer/.platform.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`password`.  **You need to change this password immediately. Not doing so is a security risk**.

## Customizations

The following changes have been made relative to TYPO3 as it is downloaded from typo3.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* At this time, the TYPO3 10 CLI installer is not yet compatible with Platform.sh.  Therefore this package includes a custom installer in `src/install.php` that is run from the deploy hook the first time the site is deployed.  It will non-interactively initialize the site's database and admin user.
* A `sites/main/config.yaml` file is provided that reads the base URL from an environment variable.
* A default `public/typo3conf/AdditionalConfiguration.php` file is provided that loads a `PlatformshConfiguration.php` file if found.  That file maps Platform.sh environment variables to the database, Redis, and base URL environment configuration needed by TYPO3.  You may modify both of these files as needed.
* Specifically, a relationship named `database` will automatically be wired to the TYPO3 primary database.  Additionally, if a relationship named `rediscache` is defined it will be used as the cache backend.  (It is included in this template.)

## References

* [TYPO3](https://typo3.org/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
