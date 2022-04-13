<details>
<summary><strong>Adding a new subsite</strong></summary><br/>

Adding a new subsite requires the following steps.  For these steps, assume we're adding a subdomain named `stuff`.

1. Add a new route to `routes.yaml` with a new `stuff` domain prefix.  Copying and pasting an existing route is fine.
2. Copy the `sites/default` directory to `sites/stuff`.
3. Edit `services.yaml` and add a new database and endpoint.  Copying and pasting an existing entry is fine.  The new relationship must be named `stuff`.
4. Edit `.platform.app.yaml` and add a new relationship: `stuff: db:stuff`.  (Where `db` is the name of the database service from `services.yaml`.)
5. Commit the above changes and push.
6. In your browser, go to the `stuff.example.com` domain (or equivalent on a dev environment) and run through the Drupal installer as usual. Alternatively, you can use Drush as described bellow.
7. Edit the `sites/stuff/settings.php` file again and enable Redis by setting `$platformsh_enable_redis` to true.
8. Commit and push that change.

Alternatively, a PHP shell script is provided that automates steps 1-4.  See [`psh-subsite-add.php`](psh-subsite-add.php).

</details>