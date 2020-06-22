# Gin for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/gin/.platform.template.yaml&utm_content=gin&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building the Gin framework for Platform.sh using Go modules.  It includes a minimalist application skeleton that demonstrates how to connect to a MariaDB server for data storage.  It is intended for you to use as a starting point and modify for your own needs.

Gin is a lightweight web framework written in Go that emphasizes performance.

## Features

* Go 1.14
* MariaDB 10.4
* Git module-based build

## Customizations

This project relies on Go module support in Go 1.11 and later.  You should commit your `go.mod` and `go.sum` files to Git, but not the `vendor` directory.

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Go module, [`platformsh/config-reader-go`](https://github.com/platformsh/config-reader-go), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Gin](https://gin-gonic.com/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
