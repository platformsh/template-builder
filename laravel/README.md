# Laravel example for Platform.sh

This project provides a starter kit for Laravel projects hosted on Platform.sh. It is primarily an example, although could be used as the starting point for a real project.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!

## Using as a reference

You can use this repository as a reference for your own projects, and borrow whatever code is needed.  The most important parts are the [`.platform.app.yaml`](/.platform.app.yaml) file and the [`.platform`](/.platform) directory.

You also will need the [platformsh/laravel-bridge](https://github.com/platformsh/laravel-bridge) composer library.  It can be installed like any other composer library:

`composer require platformsh/laravel-bridge`

That's all you need to make a Laravel application run on Platform.sh!
