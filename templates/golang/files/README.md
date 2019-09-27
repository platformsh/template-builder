# Basic Go for Platform.sh

This template provides the most basic configuration for running a custom Go project.

Go is a statically typed, compiled language with an emphasis on easy concurrency and network services.

## Services

* Go 1.13
* MariaDB 10.2

## Customizations

This project relies on Go module support in Go 1.11 and later.  You should commit your `go.mod` and `go.sum` files to Git, but not the `vendor` directory.

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Go module, [`platformsh/config-reader-go`](https://github.com/platformsh/config-reader-go), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Go](https://golang.org/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
