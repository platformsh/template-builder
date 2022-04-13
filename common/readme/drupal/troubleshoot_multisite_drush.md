<details>
<summary><strong>Using Drush in multi-site</strong></summary><br/>

In a Drupal multi-site setup, sites ID are defined in [web/sites/sites.php](https://github.com/platformsh-templates/drupal8-multisite/blob/master/web/sites/sites.php).  By default in this multi-site template, 2 subsites are defined in [routes.yaml](https://github.com/platformsh-templates/drupal8-multisite/blob/master/.platform/routes.yaml): `first` and `second`

Any Drush command can therefore be used on a specific subsite by using `--uri=`.  For example:
* `drush status --uri=first`
* `drush status --uri=second`

</details>