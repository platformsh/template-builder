<details>
<summary><strong>Default <code>hash_salt</code> behavior</strong></summary><br/>

Drupal's [default settings set](https://github.com/drupal/drupal/blob/9.3.x/core/assets/scaffold/files/default.settings.php#L252) `hash_salt` to an empty string:

```php
$settings['hash_salt'] = '';
```

In the past, Platform.sh templates have overridden this value:

```php
$settings['hash_salt'] = $settings['hash_salt'] ?? $platformsh->projectEntropy;
```

This setting was insufficient to cover some user configurations - such as those cases when an application depends on a `Null` value for `hash_salt`. 

Now, the setting looks like this in `settings.platformsh.php`:

```bash
$settings['hash_salt'] = empty($settings['hash_salt']) ? $platformsh->projectEntropy : $settings['hash_salt'];
```

This change sets `hash_salt` to the built-in environment variable `PLATFORM_PROJECT_ENTROPY` value if the project contains the default settings OR `Null`. 
If your application code *depends* on an empty value, feel free to comment out that line, or reset again later in that file.

Feel free to visit [`platformsh-templates/drupal9#73`](https://github.com/platformsh-templates/drupal9/pull/73) for more details on this discussion.

</details>