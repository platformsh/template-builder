# Go template for Platform.sh

This project provides a template for a generic Go project on Platform.sh.  It is primarily an example, although could be used as the starting point for a real project.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Structure

This project relies on Go module support in Go 1.11 and later.  You should commit your `go.mod` and `go.sum` files to Git, but not the `vendor` directory.

Access to Platform.sh environment information (the port to use, database credentials, etc.) is provided via a a [helper library](https://github.com/platformsh/gohelper) provided by Platform.sh.

This example shows access to both the port on which to listen for incoming HTTP requests and to a MariaDB database.

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.  You will also need to install the Platform.sh bridge library, `github.com/platformsh/gohelper`.
