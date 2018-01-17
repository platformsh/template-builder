# Drupal 7.x template for Platform.sh

This project provides a starter kit for Drupal 7 projects hosted on Platform.sh.

This example is based on using a vanilla install of Drupal 7 checked into Git directly.

## Starting a new project

To start a new Drupal 7 project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start new project from a template". Then select Drupal 7 as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository. This template includes examples of how to set up a Drupal 7 site using Drush.

## Using as a reference


You can also use this repository as a reference for your own Drupal projects, and
borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

Also see:

* [`settings.php`](/docroot/sites/default/settings.php) - The customized `settings.php` file works for both Platform.sh and local development, setting only those values that are needed in both.  You can add additional values as documented in `default.settings.php` as desired.
* [`settings.platformsh.php`](/docroot/sites/default/settings.platformsh.php) - This file contains Platform.sh-specific code to map environment variables into Drupal configuration.  You can add to it as needed. See [the documentation](https://docs.platform.sh/frameworks/drupal7.html) for more examples of common snippets to include here.

## Repository structure

The `docroot` directory contains a normal Drupal 7 site, as downloaded from Drupal.org.  Any add-on modules can be simply checked into Git as normal.  Drupal 7 assumes the entire code base is in the docroot so this repository does as well.
