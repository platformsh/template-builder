<details>
<summary><strong>Rebuilding cache</strong></summary><br/>

You may run into a database error after installing Drupal on your production environment initially.
To fix, SSH into the application container (`platform ssh`) and rebuild the cache using Drush:

```bash
drush cache-rebuild
```

</details>
