# Symfony 4 for Platform.sh

This template provides a basic Symfony 4 skeleton.  It is configured for Production mode by default so the usual Symfony "welcome" page will not appear.  That can be adjusted in `.platform.app.yaml`.

Symfony is a high-performance loosely-coupled PHP web development framework.

## Services

* PHP 7.3
* MariaDB 10.2

## Post-install

1. This is a bare, empty Symfony project.  That means there will be no installation page after the site is deployed.  If you wish to switch Symfony into development mode, edit your `.platform.app.yaml` file and change the `variables.env.APP_ENV` property to "dev".  (Be sure to change it back before you go live.)

2. This bare skeleton does not include an ORM or any other bundles.  You are free to install your own as you need.  Many of them will be automatically configured on Platform.sh via environment variables.  See the `platformsh-flex-env.php` file in the `platformsh/symfonyflex-bridge` library (installed via Composer), as some bundles may require additional manual configuration.

## Customizations

The following changes have been made relative to a plain Symfony 4 project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Composer library, [`platformsh/symfonyflex-bridge`](https://github.com/platformsh/symfonyflex-bridge), has been added.  It automatically maps Platform.sh's environment variables to Symfony environment variables where possible.  It leverages the [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php) library.

## References

* [Symfony](https://symfony.com/)
* [Symfony on Platform.sh](https://docs.platform.sh/frameworks/symfony.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
