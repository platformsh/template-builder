# Drupal 8 Multisite for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal8-multisite/.platform.template.yaml&utm_content=drupal8-multisite&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Drupal 8 in a multisite configuration using the "Drupal Recommended" Composer project.  It also includes configuration to use Redis for caching, although that must be enabled post-install per-site.

Drupal is a flexible and extensible PHP-based CMS framework capable of hosting multiple sites on a single code base.

## Services

* PHP 7.4
* MariaDB 10.4
* Redis 5

## Post-install

Each subsite installs separately.  As configured, this project uses a subdomain for each subsite.  For each subsite, run through the Drupal installer as normal.  You will not be asked for database credentials as those are already provided.

## Customizations

The following changes have been made relative to Drupal 8 as it is downloaded from Drupal.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.  However, the multi-site logic will only work if the conventions documented below are retained.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* Drush and Drupal Console have been pre-included in `composer.json`.  You are free to remove one or both if you do not wish to use them.  (Note that the default cron and deploy hooks make use of Drush commands, however.)
* The build hook uses the included [`install-redis.sh`](install-redis.sh) script to custom compile the Redis extension at a specified version and enable it through a `php.ini` file.
* The Drupal Redis module comes pre-installed.  The placeholder module is not pre-installed, but it is enabled via `settings.platformsh.php` out of the box.
* The `sites/sites.php` file has been modified to dynamically build a `$sites` index based on the available routes.  If you wish to alter the subsite logic you will need to change the contents of the `foreach()` loop in that file.
* The `sites/settings.platformsh.php` file contains Platform.sh-specific code to map environment variables into Drupal configuration. You can add to it as needed. See the documentation for more examples of common snippets to include here.  It uses the Config Reader library.
* The `sites/default` site directory is unused.  It is retained as an example for copy-and-paste-ing only.
* The `settings.php` file has been heavily customized to only define those values needed for both Platform.sh and local development.  It calls out to `settings.platformsh.php` if available.  You can add additional values as documented in `default.settings.php` as desired.  It is also setup such that when you install Drupal on Platform.sh the installer will not ask for database credentials as they will already be defined.

Multisite on Platform.sh can be tricky.  Drupal multisite bases its logic off of the domain name of the incoming request.  However, the domain name of the request is by design highly variable on Platform.sh as every environment has a unique domain.  As a result, this template establishes a number of conventions and custom configuration to make multi-site work.

* Every subsite is a subdomain off of a common domain.  See `routes.yaml`.  The domain prefix is the "subsite ID".
* Every subsite has its own database and endpoint on a single MariaDB service instance.  The endpoint name is the same as the subsite ID.
* The `sites/sites.php` file includes code to build a `$sites` lookup list to map any incoming request, regardless of branch, to a settings directory named for the subsite ID.  It iterates over all routes that point to the Drupal application and parses those routes into a domain name -> directory list, where the directory is the site ID.  If you are not using a subdomain based multi-site you will likely need to modify the body of the `foreach()` loop.
* The `.platform.app.yaml` file is essentially the same as for a single-site Drupal installation, but its relationships include every defined MariaDB endpoint.  The relationship is also named for the subsite ID.
* Every subsite ID's `settings.php` file is identical, and largely similar to the standard Platform.sh `settings.php` file.  You may customize it if needed.  In particular, the `$platformsh_enable_redis` variable should be toggled to `true` for each site only after the install process is completed for that site, as Drupal cannot install with the redis module active.
* The `settings.php` files also include a shared `sites/settings.platformsh.php` file.  It is largely the same as in a single-site configuration but has been modified to leverage the subsite ID for:
  * Selecting which database relationship to use
  * Including a cache prefix in Redis so that each site has its own effective cache pool.
  * Setting the files and private files directories, which are subsite ID prefixes of top-level `files` and `private` directories rather than under each site directory.

## Adding a new subsite

Adding a new subsite requires the following steps.  For these steps, assume we're adding a subdomain named `stuff`.

1. Add a new route to `routes.yaml` with a new `stuff` domain prefix.  Copying and pasting an existing route is fine.
2. Copy the `sites/default` directory to `sites/stuff`.
3. Edit `services.yaml` and add a new database and endpoint.  Copying and pasting an existing entry is fine.  The new relationship must be named `stuff`.
4. Edit `.platform.app.yaml` and add a new relationship: `stuff: db:stuff`.  (Where `db` is the name of the database service from `services.yaml`.)
5. Commit the above changes and push.
6. In your browser, go to the `stuff.example.com` domain (or equivalent on a dev environment) and run through the Drupal installer as usual. Alternatively, you can use Drush as described bellow.
7. Edit the `sites/stuff/settings.php` file again and enable Redis by setting `$platformsh_enable_redis` to true.
8. Commit and push that change.
9. Profit.

Alternatively, a PHP shell script is provided that automates steps 1-4.  See [`psh-subsite-add.php`](psh-subsite-add.php).

## Using Drush in multi-site

In a Drupal multi-site setup, sites ID are defined in [web/sites/sites.php](https://github.com/platformsh-templates/drupal8-multisite/blob/master/web/sites/sites.php).  By default in this multi-site template, 2 subsites are defined in [routes.yaml](https://github.com/platformsh-templates/drupal8-multisite/blob/master/.platform/routes.yaml): `first` and `second`

Any Drush command can therefore be used on a specific subsite by using `--uri=`.  For example:
* `drush status --uri=first`
* `drush status --uri=second`

## References

* [Drupal](https://www.drupal.org/)
* [Drupal on Platform.sh](https://docs.platform.sh/frameworks/drupal8.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
