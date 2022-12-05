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

## Deploy

The quickest way to deploy this template on Platform.sh is by clicking the button below. 
This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/akeneo/.platform.template.yaml&utm_content=akeneo&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>
<br/>

You can also quickly recreate this project locally with the following command:

```bash
composer create-project platformsh/pim-community-standard -s dev
```

> **Note:**    
>
> Platform.sh templates prioritize upstream release versions over our own. Despite this, we update template dependencies on a scheduled basis independent of those upstreams. Because of this, template repos do not contain releases. This may change in the future, but until then the `-s dev` flag is necessary to use `composer create-project`.

## Post-install

1. The first time the site is deployed, Akeneo's command line installer will run and initialize the database.  It will not run again unless the `installer/minimal.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`admin`.  **You need to change this password immediately. Not doing so is a security risk**.

3. After you have deployed, you can additionally view a built-in demo version of Akeneo, complete with default settings and an initial catalog of products. On a new environment (`platform environment:branch demo`), update the `variables.env` block of `.platform.app.yaml` to match the following:

```yaml
variables:
    env:
        APP_ENV: 'prod'
        APP_DEBUG: 0
        APP_DEFAULT_LOCALE: 'en_US'
        APP_PRODUCT_AND_PRODUCT_MODEL_INDEX_NAME: 'akeneo_pim_product_and_product_model'
        # AKENEO_STARTER: minimal
        AKENEO_STARTER: icecat_demo_dev
        # Update these for your desired Node version.
        NODE_VERSION: v14.19.0
```

`AKENEO_STARTER` will then be updated from the default `minimal` catalog to `icecat_demo_dev`. Like before, Akeneo will create an initial admin user (`admin/admin`), and you should update those credentials immediately. 

## Customizations

The following changes have been made relative to Akeneo as it is downloaded from Akeneo.com.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The [`.environment`](.environment) file maps the Platform.sh environment variables to those expected by Akeneo.  You can add additional environment setup there as needed but do not remove the lines that already exist.

## References

* [Akeneo](https://www.akeneo.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
