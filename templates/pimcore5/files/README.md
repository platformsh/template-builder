# Pimcore 5 project template for Platform.sh

This project provides a starter kit for Pimcore 5 projects hosted on [Platform.sh](http://platform.sh).  There are only very minor changes from vanilla Pimcore 5.

## Starting a new project

To start a new Pimcore 5 project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start    new project from a template".  Then select Pimcore 5 as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository.

## Using as a reference

You can use this repository as a reference for your own Pimcore 5 projects, and
borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

Also see:

* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platform.php`.  That will load a PHP file rather than YAML file to specify Symfony configuration parameters.
* [`parameters_platform.php`](/app/config/parameters_platform.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters.  This file will be parsed on every page load.  By default it only maps a default database and rediscache connection parameters.  You can add to it as needed.
* [`installer.yml`](/app/config/installer.yml) - This file is added so the pimcore install process can retrieve the database connection parameters needed for the installation process.

Now that you have you pimcore base project loaded on platform, proceed with setting up your admin user and bootstraping pimcore5
- Update the database encoding, using our Platform CLI tool:
```
platform sql -p {PROJECT-ID} -e master "ALTER DATABASE  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```
- Install Pimcore:
Ssh to the container instance with Platform CLI tool:
```
platform ssh
```
Proceed with the installation procedure
```bash
export PIMCORE_INSTALL_ADMIN_USERNAME='admin'
export PIMCORE_INSTALL_ADMIN_PASSWORD='admin'
vendor/bin/pimcore-install --no-interaction --ignore-existing-config --no-debug
```

That's all you need to make a Pimcore 5 application run on Platform.sh!
