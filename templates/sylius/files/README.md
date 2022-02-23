<br />
<!-- Platform.sh logo left -->
<p align="left">
    <a href="https://platform.sh">
        <img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
    </a>
</p>
<br /><br />
<!-- Template logo -->
<p align="center">
    <a href="https://github.com/directus/directus">
        <img src="https://demo.sylius.com/assets/shop/img/logo.png" alt="Logo" width="300">
    </a>
</p>
<!-- Template title -->
<br/>
<h2 align="center">Deploy Sylius on Platform.sh</h2>

<!-- Deploy on Platform.sh button -->
<br />
<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/sylius/.platform.template.yaml&utm_content=sylius&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="175px" />
    </a>
</p>
<br/><br/>

This template builds a Sylius application for Platform.sh, which can be used as a starting point for developing complex e-commerce applications.

Sylius is a modern e-commerce solution for PHP, based on Symfony Framework.

## Features

- PHP 8.0
- MySQL 10.2
- Automatic TLS certificates
- composer-based build

## Post-install

By default, Sylius ignores the `composer.lock` file in Git. Once you have deployed the template, it is a good idea to remove `composer.lock` from `.gitignore` and commit it, so that you can benefit from repeatable builds on Platform.sh.

## Customization

The following changes have been made relative to a plain Sylius 1.11 project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Composer library, [`platformsh/symfonyflex-bridge`](https://github.com/platformsh/symfonyflex-bridge), has been added.  It automatically maps Platform.sh's environment variables to Symfony environment variables where possible.  It leverages the [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php) library.

## Resources

- [Sylius](https://sylius.com)
- [Sylius documentation](https://docs.sylius.com/en/latest/)
- [Platform.sh deployment docs](https://docs.sylius.com/en/latest/cookbook/deployment/platform-sh.html)
- [Sylius Plus installation guide](https://docs.sylius.com/en/latest/cookbook/deployment/platform-sh.html#how-to-deploy-sylius-plus-to-platform-sh)
- [Cron jos and additional tips](https://docs.sylius.com/en/latest/cookbook/deployment/platform-sh.html#dive-deeper)
- [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)

