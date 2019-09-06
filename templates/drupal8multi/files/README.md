# Drupal 8 Multisite for Platform.sh

This template builds Drupal 8 in a multisite configuration using the [Drupal Composer project](https://github.com/drupal-composer/drupal-project) for better flexibility.  It also includes configuration to use Redis for caching, although that must be enabled post-install per-site.

Drupal is a flexible and extensible PHP-based CMS framework capable of hosting multiple sites on a single code base.

## Services

* PHP 7.3
* MariaDB 10.2
* Redis 5

## Post-install

Each subsite installs separately.  As configured, this project uses a subdomain for each subsite.  The setup process for each site is the same:

1. Run through the Drupal installer as normal.  You will not be asked for database credentials as those are already provided.

2. Once Drupal is fully installed, edit the `sites/<sitename>/site-definition.php` file and set `$platformsh_enable_redis` to `true.  That will enable Drupal's Redis cache integration.  (The Redis cache integration cannot be active during the installer.)

## Customizations

The following changes have been made relative to Drupal 8 as it is downloaded from Drupal.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* It uses the Drupal Composer project, which allow the site to be managed entirely with Composer. That also causes the `vendor` and `config` directories to be placed outside of the web root for added security.  See the [Drupal documentation](https://www.drupal.org/node/2404989) for tips on how best to leverage Composer with Drupal 8.
* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.  However, the multi-site logic will only work if the conventions documented below are retained.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* The `sites/sites.php` file has been modified to dynamically build a `$sites` index based on the available routes.  If you wish to alter the subsite logic you will need to change the contents of the `foreach()` loop in that file.
* The `sites/settings.platformsh.php` file contains Platform.sh-specific code to map environment variables into Drupal configuration. You can add to it as needed. See the documentation for more examples of common snippets to include here.  It uses the Config Reader library.
* The `settings.php` file has been heavily customized to only define those values needed for both Platform.sh and local development.  It calls out to `settings.platformsh.php` if available.  You can add additional values as documented in `default.settings.php` as desired.  It is also setup such that when you install Drupal on Platform.sh the installer will not ask for database credentials as they will already be defined.

Multisite on Platform.sh can be tricky.  Drupal multisite bases its logic off of the domain name of the incoming request.  However, the domain name of the request is by design highly variable on Platform.sh as every environment has a unique domain.  As a result, this template establishes a number of conventions and custom configuration to make multi-site work.

* Every subsite is a subdomain off of a common domain.  See `routes.yaml`.  The domain prefix is the "subsite ID".
* Every subsite has its own database and endpoint on a single MariaDB service instance.  The endpoint name is the same as the subsite ID.
* The `sites/sites.php` file includes code to build a `$sites` lookup list to map any incoming request, regardless of branch, to a settings directory named for the subsite ID.  It consists of two parts: The first block filters the routes list from the environment to just those that are relevant (that is, it excludes redirect routes or routes that point to a different application container).  The second parses those routes into a domain name -> directory list, where the directory is the site ID.  You will also most never want to modify the first part.  The second part you may want to modify if you are not using a subdomain model.
* The `.platform.app.yaml` file is essentially the same as for a single-site Drupal installation, but its relationships include every defined MariaDB endpoint.  The relationship is also named for the subsite ID.
* Every subsite ID's `settings.php` file is identical, and largely similar to the standard Platform.sh `settings.php` file.  You may customize it if needed.  However, it also sub-calls to a new file name `site-definition.php`.  That file defines two variables: One that sets the subsite ID, and one is a toggle to enable Redis for caching.  This value must be `false` for the install process.
* The `settings.php` files also include a shared `sites/settings.platformsh.php` file.  It is largely the same as in a single-site configuration but has been modified to leverage the subsite ID for:
** Selecting which database relationship to use
** Sncluding a cache prefix in Redis so that each site has its own effective cache pool.
** Setting the files and private files directories, which are subsite ID prefixes of top-level `files` and `private` directories rather than under each site directory.

## Adding a new subsite

Adding a new subsite requires the following steps.  For these steps, assume we're adding a subdomain named `stuff`.

1. Add a new route to `routes.yaml` with a new `stuff` domain prefix.  Copying and pasting an existing route is fine.
2. Copy the `sites/default` directory to `sites/stuff`.
3. Edit `sites/stuff/site-definition.php` and set `$platformsh_subsite_id` to `stuff`, then set `$platformsh_enable_redis` to false.
4. Edit `services.yaml` and add a new database and endpoint.  Copying and pasting an existing entry is fine.  The new relationship must be named `stuff`.
5. Edit `.platform.app.yaml` and add a new relationship: `stuff: db:stuff`.  (Where `db` is the name of the database service from `services.yaml`.)
6. Commit the above changes and push.
7. In your browser, go to the `stuff.example.com` domain (or equivalent on a dev environment) and run through the Drupal installer as usual.
8. Edit the `sites/stuff/site-definition.php` file again and enable Redis.
9. Commit and push that change.
10. Profit.

## References

* [Drupal](https://www.drupal.org/)
* [Drupal on Platform.sh](https://docs.platform.sh/frameworks/drupal8.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
