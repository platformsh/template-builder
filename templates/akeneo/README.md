Akeneo PIM Community Standard Edition template for Platform.sh
=====================================

This project provides a starter kit for Akeneo projects hosted on [Platform.sh](http://platform.sh).  There are only very minor changes from vanilla Akeneo PIM Community Standard Edition.

## Starting a new project

To start a new Akeneo project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start new project from a template".  Then select Akeneo as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository.

## Using as a reference

You can use this repository as a reference for your own Akeneo projects, and borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.


Also see:

* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platform.php`.  That will load a PHP file rather than YAML file to specify Symfony configuration parameters.
* [`parameters_platform.php`](/app/config/parameters_platform.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters. This file will be parsed on every page load. By default it only maps a default database and elasticsearch connection parameters. You can add to it as needed.
* [`parameters.yml.dist`](/app/config/parameters.yml.dist) - This file is modified so the install process can retrieve the database connection parameters, SwiftMailer can connect to the correct host and the inital data set is set to `minimal`

The template is configured to install the data set automatically during the build hook. That means after the first build and deployment, you can login with user: `admin` / password: `admin`.

Please note, that this project uses a worker for the Akeneo `job-queue-consumer-daemon`. That means you need to run this on a Medium plan or higher.

That's all you need to make a Akeneo application run on Platform.sh!
