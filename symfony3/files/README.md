# Symfony 3 project template for Platform.sh

This project provides a starter kit for Symfony 3 projects hosted on [Platform.sh](http://platform.sh).  There are only very minor changes from vanilla Symfony 3.

## Starting a new project

To start a new Symfony 3 project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start    new project from a template".  Then select Symfony 3 as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository.

## Using as a reference

You can use this repository as a reference for your own Symfony projects, and
borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

Also see:

* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platform.php`.  That will load a PHP file rather than YAML file to specify Symfony configuration parameters.  Also note toward the bottom that the Doctrine DBAL server version is specified explicitly.  That is required to work around an issue where Doctrine will try to connect to the database during the build process to determine the server version, even though it doesn't need it.
* [`parameters_platform.php`](/app/config/parameters_platform.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters.  This file will be parsed on every page load.  By default it only maps a default database connection to Container parameters expected by Doctrine.  You can add to it as needed.

That's all you need to make a Symfony 3 application run on Platform.sh!
