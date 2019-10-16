# Node.js for Platform.sh

This template builds a simple application using the Node.js built-in `http` web server. It includes a minimalist application skeleton for demonstration, but you are free to alter it as needed.

Node.js is an open-source JavaScript runtime built on Chrome's V8 JavaScript engine.

## Services

* Node.js 10
* MariaDB 10.4

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional module, [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Node.js http](https://nodejs.org/api/http.html#http_http)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)