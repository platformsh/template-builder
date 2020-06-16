# Common Lisp Example for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/lisp/.platform.template.yaml&utm_content=lisp&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides the most basic configuration for running a Lisp Huchentoot web server for Platform.sh.  It can be used to build a very rudimentary application but is intended primarily as a documentation reference.  It is meant to be a starting point and can be modified to fit your own needs.

This template builds a simple Lisp Hunchentoot web server for Platform.sh.  It includes a minimalist application  for demonstration, but you are free to alter it as needed.

Hunchentoot is a web server written in Common Lisp and at the same time a toolkit for building dynamic websites.

## Features

* Lisp 1.5
* Automatic TLS certificates

## Customizations

The following files and additions make the the example work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.


## References

* [Hunchentoot](https://edicl.github.io/hunchentoot/)
* [Lisp on Platform.sh](https://docs.platform.sh/languages/lisp.html)
