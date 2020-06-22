# Sculpin for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/sculpin/.platform.template.yaml&utm_content=sculpin&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides a basic Sculpin skeleton.  All files are generated at build time, so at runtime only static files need to be served.

Sculpin is a static site generator written in PHP and using the Twig templating engine.

## Features

* PHP 7.4
* Automatic TLS certificates
* Composer-based build

## Customizations

The following changes have been made relative to a plain Sculpin project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.

## References

* [Sculpin](https://sculpin.io/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
