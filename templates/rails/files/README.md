# Ruby on Rails template for Platform.sh

This project provides a starter kit for Ruby on Rails projects hosted on Platform.sh.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.

Additionally, this repository includes a bridge gem that auto-populates the environment variables that Rails looks for in order to connect to the database and other services.  See the `Gemfile` for the `gem` line that includes `platform_sh_helper`.  More information can be found in that [project's repository](https://github.com/platformsh/platformsh-rails-helper).
