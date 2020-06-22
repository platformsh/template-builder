# Beego for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/beego/.platform.template.yaml&utm_content=beego&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>


This template demonstrates building the Beego framework for Platform.sh using Go modules.  It includes a minimalist application skeleton that demonstrates how to connect to a MariaDB server.  It is intended for you to use as a starting point and modify for your own needs.

Beego is a popular web framework written in Go.

## Features

* Go 1.14
* MariaDB 10.4
* Automatic TLS certificates
* Git module-based build

## Customizations

This project relies on Go module support in Go 1.11 and later.  You should commit your `go.mod` and `go.sum` files to Git, but not the `vendor` directory.

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Go module, [`platformsh/config-reader-go`](https://github.com/platformsh/config-reader-go), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* The `conf` directory shows one way of exposing the Config Reader to the application.  You are free to take some other approach if you prefer.

## References

* [Beego](https://beego.me/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
