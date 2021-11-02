# TYPO3 (v11) for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/typo3-v11/.platform.template.yaml&utm_content=typo3-v11&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds the TYPO3 (v11) CMS for Platform.sh.  It comes pre-configured with MariaDB for storage and Redis for caching.  A command line installer will automatically initialize the site on first deploy.

TYPO3 is a Content Management System (CMS) built in PHP.

## Features

* PHP 7.4
* MariaDB 10.4
* Redis 5.0
* Automatic TLS certificates
* Composer-based build

## Post-install

1. The first time the site is deployed, the TYPO3 console will initialize the database and create an initial user.  It will not run again unless the `var/platformsh.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`password`.  **You need to change this password immediately. Not doing so is a security risk**.

## Customizations

The following changes have been made relative to TYPO3 as it is downloaded from typo3.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A default `public/typo3conf/AdditionalConfiguration.php` file is provided that loads a `PlatformshConfiguration.php` file if found.  That file maps Platform.sh environment variables to the database, Redis, and base URL environment configuration needed by TYPO3.  You may modify both of these files as needed.
* The [`public/typo3conf/LocalConfiguration.php`](https://docs.typo3.org/m/typo3/reference-coreapi/master/en-us/ApiOverview/GlobalValues/Typo3ConfVars/Index.html#file-localconfiguration-php) file has been moved to `var/LocalConfiguration.php` as `public/typo3conf` is read only in the production environment. A symlink from `public/typo3/LocalConfiguration.php` to the new location is created during the build stage.
* During the first build, the [`ENABLE_INSTALL_TOOL`](https://docs.typo3.org/m/typo3/reference-coreapi/master/en-us/Security/GuidelinesIntegrators/InstallTool.html#install-tool) file is created in the `var/` directory, and a symlink created connecting it to `public/typo3conf`. Once you have finished installing TYPO3, you can remove the `TYPO3_ENABLE_INSTALL_TOOL: 'true'` from the `.platform.app.yaml` file in the `variables:env` section.
* Specifically, a relationship named `database` will automatically be wired to the TYPO3 primary database.  Additionally, if a relationship named `rediscache` is defined it will be used as the cache backend.  (It is included in this template.)

## References

* [TYPO3](https://typo3.org/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
