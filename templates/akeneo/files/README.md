# Akeneo PIM Community Edition for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/akeneo/.platform.template.yaml&utm_content=akeneo&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds the Akeneo PIM system for Platform.sh.  By default it uses the "minimal" install profile.  It requires at least a Medium plan as it uses a Worker instance for queue processing.

Akeneo is a Product Information Management (PIM) tool, which acts as a central store for product information, catalog information, and inventory management.

## Services

* PHP 7.4
* MySQL 8.0
* Elasticsearch 7.7

## Post-install

1. The first time the site is deployed, Akeneo's command line installer will run and initialize the database.  It will not run again unless the `installer/.platform.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`admin`.  **You need to change this password immediately. Not doing so is a security risk**.

## Customizations

The following changes have been made relative to Akeneo as it is downloaded from Akeneo.com.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The [`.environment`](.environment) file maps the Platform.sh environment variables to those expected by Akeneo.  You can add additional environment setup there as needed but do not remove the lines that already exist.

## References

* [Akeneo](https://www.akeneo.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
