<details>
<summary><strong>How Drupal multi-site works on Platform.sh</strong></summary><br/>

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

</details>