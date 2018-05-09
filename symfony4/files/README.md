# Symfony 4 Flex project template for Platform.sh

This project provides a starter kit for Symfony 4 projects hosted on [Platform.sh](http://platform.sh).  There are only very minor changes from vanilla Symfony 4.

## Starting a new project

To start a new Symfony 4 project on Platform.sh, you have 2 options:

1. Create a new project through the Platform.sh user interface and select "start new project from a template".  Then select Symfony 4 as the template. That will create a new project using this repository as a starting point.

2. Take an existing project, add the necessary Platform.sh files, and push it to a Platform.sh Git repository.

## Using as a reference

You can use this repository as a reference for your own Symfony projects, and
borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

You also will need the [platformsh/symfonyflex-bridge](https://github.com/platformsh/symfonyflex-bridge) composer library.  It can be installed like any other composer library:

`composer require platformsh/symfonyflex-bridge`

That's all you need to make a Symfony 4 application run on Platform.sh!
