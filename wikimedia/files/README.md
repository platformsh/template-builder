# WikiMedia project template for Platform.sh

This project provides a starter kit for WikiMedia instances hosted on [Platform.sh](http://platform.sh). 

## Starting a new project

To start a new WikiMedia instance on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "import your existing code"
2. Add Platform.sh as a git remote and push

Tada. You have a running wikimedia installation.

## Using as a reference

You can also use this repository as a reference for your own wikimedia based projects, and borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory as well as what we put in composer.local.json and LocalSettings.php

Also see:

* [`settings.php`](/web/sites/default/settings.php) - The customized `settings.php` file works for both Platform.sh and local development, setting only those values that are needed in both.  You can add additional values as documented in `default.settings.php` as desired.
* [`settings.platformsh.php`](/web/sites/default/settings.platformsh.php) - This file contains Platform.sh-specific code to map environment variables into Drupal configuration.  You can add to it as needed.  See [the documentation](https://docs.platform.sh/frameworks/drupal8.html) for more examples of common snippets to include here.
* [`scripts/platformsh`](/scripts/platformsh) - This directory contains our update script to keep this repository in sync with the Drupal Composer project.  It may be safely ignored or removed.
