# Basic PHP for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/php/.platform.template.yaml&utm_content=php&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides the most basic configuration for running a custom PHP project built with Composer.  It includes but doesn't make use of the Platform.sh `config-reader` library.  It can be used to build a very rudimentary application but is intended primarily as a documentation reference.

PHP is a high-performance scripting language especially well suited to web development.

## Features

* PHP 7.4
* Automatic TLS certificates
* Composer-based build

## Customizations

The following files are of particular importance.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* A Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [PHP](https://php.net/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
