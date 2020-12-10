# WordPress WooCommerce (Bedrock) for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/wordpress-woocommerce/.platform.template.yaml&utm_content=wordpress-woocommerce&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds WordPress on Platform.sh using the Bedrock boilerplate by Roots with Composer. It includes WooCommerce and JetPack as dependencies, which when enabled will quickly allow you to create a store on WordPress.

Plugins and themes should be managed with Composer exclusively. The only modifications made to the standard Bedrock boilerplate have been providing database credentials and main site url parameters via environment variables. With this configuration, the database is automatically configured such that the installer will not ask you for database credentials. While Bedrock provides support to replicate this configuration in a `.env` file for local development, an example Lando configuration file is included as the recommendated method to do so. 

WordPress is a blogging and lightweight CMS written in PHP, and Bedrock is a Composer-based WordPress boilerplate project with a slightly modified project structure and configuration protocol. WooCommerce is an open-source eCommerce platform and plugin for WordPress.

## Features

* PHP 7.4
* MariaDB 10.4
* Automatic TLS certificates
* Composer-based build

## Post-install

Run through the WordPress installer as normal. You will not be asked for database credentials as those are already provided. Once you have finished the installation and have logged into the site, go to the Plugins section of the sidebar and 'Activate' WooCommerce. Follow the instructions to finish setting up your store.

## Customizations

The following changes have been made relative to Bedrock's project creation command `composer create-project roots/bedrock`. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* A `.environment` file has been included which sets Bedrock's configuration on Platform.sh. It defines the connection to the MariaDB database, the primary site URL, and security keys and salts. 
* A base [Landofile](https://docs.lando.dev/config/lando.html#base-file) provides configuration to use this template locally using [Lando](https://docs.lando.dev).
* `woocommerce` and `jetpack` have been added as dependencies from the regular [`wordpress-bedrock`](https://github.com/platformsh-templates/wordpress-bedrock) template to support running a store with WordPress.

## Local development

This template has been configured for use with [Lando](https://docs.lando.dev).  Lando is Platform.sh's recommended local development tool.  It is capable of reading your Platform.sh configuration files and standing up an environment that is _very similar_ to your Platform.sh project.  Additionally, Lando can easily pull down databases and file mounts from your Platform.sh project.

To get started using Lando with your Platform.sh project check out the [Quick Start](https://docs.platform.sh/development/local/lando.html) or the [official Lando Platform.sh documentation](https://docs.lando.dev/config/platformsh.html).

## References

* [Bedrock at Roots](https://roots.io/bedrock/)
* [Bedrock documentation](https://roots.io/docs/bedrock/master/installation/)
* [Bedrock on GitHub](https://github.com/roots/bedrock)
* [WooCommerce](https://woocommerce.com/)
* [WordPress](https://wordpress.org/)
* [WordPress on Platform.sh](https://docs.platform.sh/frameworks/wordpress.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
* [How to install Wordpress plugins and themes with Composer](https://community.platform.sh/t/how-to-install-wordpress-plugins-and-themes-with-composer/507)
* [How to install custom/private Wordpress plugins and themes with Composer](https://community.platform.sh/t/how-to-install-custom-private-wordpress-plugins-and-themes-with-composer/622)
