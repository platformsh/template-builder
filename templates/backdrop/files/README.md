# Backdrop for Platform.sh

This template builds a Backdrop site, with the entire site committed to Git.

Backdrop is a PHP-based CMS, originally forked from Drupal 7.

## Services

* PHP 7.3
* MariaDB 10.4

## Post-install

1. Run through the Backdrop installer as normal by visiting `<project url>/install.php`.  You will not be asked for database credentials as those are already provided.

2. Once Backdrop is fully installed, We strongly recommend switching to Redis-based caching.

## Customizations

The following changes have been made relative to Backdrop as it is downloaded from backdropcms.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `/web/settings.platformsh.php` file contains Platform.sh-specific code to map environment variables into Backdrop configuration. You can add to it as needed.
* The `/web/settings.php` file has been customized to include the Platform.sh settings file.  It also will check for a `settings.local.php` file only if it's not running on Platform.sh.
* A patch has been included to support setting configuration values from `settings.php`.  This patch is based on an [existing PR](https://github.com/backdrop/backdrop/pull/2964) that is expected to be merged into a future version of Backdrop.  Once that happens the patch will no longer be necessary.

## References

* [Backdrop](https://backdropcms.org/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
