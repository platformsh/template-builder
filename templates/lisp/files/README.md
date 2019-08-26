# Common Lisp Example for Platform.sh

This template builds a simple Lisp Hunchentoot web server for Platform.sh.  It includes a minimalist application  for demonstration, but you are free to alter it as needed.

Hunchentoot is a web server written in Common Lisp and at the same time a toolkit for building dynamic websites.

## Services

* Lisp 1.5

## Customizations

The following files and additions make the the example work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.


## References

* [Hunchentoot](https://edicl.github.io/hunchentoot/)
* [Lisp on Platform.sh](https://docs.platform.sh/languages/lisp.html)
