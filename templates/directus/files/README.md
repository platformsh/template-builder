# Directus for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/directus/.platform.template.yaml&utm_content=directus&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building Directus for Platform.sh. It includes a quickstart application configured to run with PostgreSQL. It is intended for you to use as a starting point and modify for your own needs.

Directus is an open-source platform that allows you to create and manage an API from data stored in a database.

## Features

* Node.js 14
* PostgreSQL 12
* Automatic TLS certificates
* npm-based build

## Post-install

This template does not require any additional configuration once deployed to start developing your Directus application. During the first deploy, however, an admin user was added to allow you to log in (see `.environment`). After you log in for the first time, be sure to update this password immediately. 

Although this project uses PostgreSQL as its primary database, Directus supports [a number of other options](https://docs.directus.io/guides/installation/cli.html#_1-confirm-minimum-requirements-are-met) that can be easily substituted using Platform.sh's managed services. 

- [MariaDB](https://docs.platform.sh/configuration/services/mysql.html)
- [Oracle MySQL](https://docs.platform.sh/configuration/services/mysql.html)
- [PostgreSQL](https://docs.platform.sh/configuration/services/postgresql.html)

## Customizations

The following files and additions make the framework work on Platform.sh on top of the basic quickstart project (`npx create-directus-project`). If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.environment` file provides Platform.sh-specific environment variable overrides from the generated default `.env` settings for Directus and PostgreSQL. It also sets an initial username and password for an admin user. 
* A `.gitignore` file has been added to prevent `node_modules` from being committed. 

## References

* [Directus Documentation](https://docs.directus.io/getting-started/introduction.html)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
