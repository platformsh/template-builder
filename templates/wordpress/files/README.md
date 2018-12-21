# WordPress template for Platform.sh

This project provides a starter kit for WordPress projects hosted on Platform.sh. It is primarily an example, although could be used as the starting point for a real project.  It is built using Composer, via the popular <a href="https://github.com/johnpbloch/wordpress">johnpbloch/wordpress</a> script.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.

2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.

## Local settings

This example looks for an optional `wp-config-local.php` alongside your `wp-config.php` file that you can use to develop locally. This file is ignored in git.

Example `wp-config-local.php`:

```php
<?php

define('WP_HOME', "http://localhost");
define('WP_SITEURL',"http://localhost");
define('DB_NAME', "my_wordpress");
define('DB_USER', "user");
define('DB_PASSWORD', "a strong password");
define('DB_HOST', "127.0.0.1");
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

// These will be set automatically on Platform.sh to a different value, but that won't cause issues.
define('AUTH_KEY', 'SECURE_AUTH_KEY');
define('LOGGED_IN_KEY', 'LOGGED_IN_SALT');
define('NONCE_KEY', 'NONCE_SALT');
define('AUTH_SALT', 'SECURE_AUTH_SALT');
```
