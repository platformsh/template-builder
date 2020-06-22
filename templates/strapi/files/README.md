# Strapi template for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/strapi/.platform.template.yaml&utm_content=strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a Strapi backend for Platform.sh, which can be used to quickly create an API that can be served by itself or as a Headless CMS data source for another frontend application in the same project. This repository not include a frontend application, but you can add one of your choice and access Strapi by defining it in a relationship in your frontend's `.platform.app.yaml` file.

Strapi is a Headless CMS framework written in Node.js.

## Features

* Node.js 14
* PostgreSQL 12
* Automatic TLS certificates
* npm-based build

## Post-install

1. The first time the site is deployed, Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before any API endpoints can be created.
2. Once you have registered the admin user, you will have access to the **Admin Panel**, and from there you can begin adding Content Types to build out the API. By default, no Content Types have been included in the installation *and* any Content Types you add will have secured API endpoints that will make them publicly inaccessible. You will need to update the permissions for each Content Type from the *Users & Permissions* section of the **Admin Panel** after you have created them. If you are unfamiliar with how to create Content Types or modify permissions with Strapi, visit the [Quick Start Guide](https://strapi.io/documentation/3.0.0-beta.x/getting-started/quick-start.html) for detailed instructions.
3. This template provides only the API for a full project, but you can modify the repository into a [multi-app project](https://docs.platform.sh/configuration/app/multi-app.html#multiple-applications) where Strapi acts as a separate backend application for the front end of your choice. For example, you can add a frontend ExpressJS application in another directory called `frontend` with its own `.platform.app.yaml` file.

  ```
  .
  ├── .git
  ├── .platform
  │   ├── routes.yaml
  │   └── services.yaml
  ├── backend
  │   ├── .platform.app.yaml
  │   ├── api
  │   ├── config
  │   ├── extensions
  │   ├── package.json
  │   ├── public
  │   └── yarn.lock
  └── frontend
      ├── .platform.app.yaml
      ├── index.js
      ├── package-lock.json
      └── package.json
  ```

## Customizations

The following changes have been made relative to the quickstart Strapi project to run on Platform.sh.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional module, [config-reader-nodejs](https://github.com/platformsh/config-reader-nodejs), has been added. It provides convenience wrappers for accessing the Platform.sh environment variables.
* The traditional `config/(development|production|staging)/database.json` file has been replaced with a `database.js` script. This change allows you to leverage `config-reader-nodejs` to dynamically read database (in this case, PostgreSQL) credentials on the fly from the `PLATFORM_RELATIONSHIPS` environment variable, rather than pre-specifying them.
* The `config/(development|production|staging)/server.json` has been modified to read the `port` configuration from the `PORT` Platform.sh environment variable.
* The `start` command calls the script `start.sh`, which is configured to run Strapi as a [`development` environment](https://strapi.io/documentation/3.0.0-beta.x/cli/CLI.html#strapi-develop-dev), allowing you to create new Content Types once it is deployed, even on the `master`/production branch of your project. We recommend adjusting this command to run Strapi in [`production`](https://strapi.io/documentation/3.0.0-beta.x/cli/CLI.html#strapi-start) mode on the master branch (`start.sh` includes an example environment-specific start command that can be used to accomplish this).

## References

* [Strapi.io](https://strapi.io/)
* [Strapi Documentation](https://strapi.io/documentation/3.0.0-beta.x/getting-started/introduction.html)
* [Strapi Quick Start Guide](https://strapi.io/documentation/3.0.0-beta.x/getting-started/quick-start.html)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
* [Multi-app on Platform.sh](https://docs.platform.sh/configuration/app/multi-app.html#multiple-applications)
