# Hugo template for Platform.sh

This project provides a starter kit for Hugo projects hosted on Platform.sh. It is primarily an example, although could be used as the starting point for a real project.

If you want to change the theme of the Hugo template, consult that theme's documentation and either add the theme as a git submodule:

```sh
git submodule add https://github.com/panr/hugo-theme-hello-friend.git themes/hello-friend
```

Or you can also the theme in your `themes` folder. To enable the theme and add its default configuration, modify `config.toml` to the settings as documented.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.
