# Drupal 7.x template for Platform.sh

This project provides a starter kit for Drupal 7 projects hosted on Platform.sh.

This example is based on using the Drush Make build profile.

You can see there is not much in terms of files committed to this repository. You can learn (much) more on [Platform.sh Drupal Hosting Documentation](https://docs.platform.sh/frameworks/drupal7.html)


## Starting a new project

To start a new Drupal 7 project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start new project from a template". Then select Drupal 7 as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository. This template includes examples of how to set up a Drupal 7 site using Drush.

## Using as a reference


You can also use this repository as a reference for your own Drupal projects, and
borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

Also see:

* [`settings.php`](/settings.php) - The customized `settings.php` file works for both Platform.sh and local development, setting only those values that are needed in both.  You can add additional values as documented in `default.settings.php` as desired.
* [`settings.platformsh.php`](/settings.platformsh.php) - This file contains Platform.sh-specific code to map environment variables into Drupal configuration.  You can add to it as needed. See [the documentation](https://docs.platform.sh/frameworks/drupal7.html) for more examples of common snippets to include here.

## Repository structure

This is the whole layout of the repository (it will still make for a perfectly functional web site on [Platform.sh](http://platform.sh)!):

```
.platform/
        routes.yaml
        services.yaml
libraries/
        README.txt
modules/
        README.txt
themes/
        README.txt
.platform.app.yaml
project.make
```

The `.platform` directory and `.platform.app.yaml` file are the Platform.sh-specific configuration.  Please see the [documentation](https://docs.platform.sh/) for more information on those.

The `libraries`, `modules`, and `themes` directories are optional; they are where you would put any custom or forked libraries, modules, or themes that you want to include in your project when it gets built by Drush make.  Modules or themes from Drupal.org that you want to use unmodified should be specified in the `project.make` file instead.

The top-level `settings.php` and `settings.platformsh.php` files will be automatically moved to `public/sites/default` by the `drupal` build flavor, where Drupal can find them.
