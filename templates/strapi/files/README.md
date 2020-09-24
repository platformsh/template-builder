# Strapi template for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/strapi/.platform.template.yaml&utm_content=strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a Strapi backend for Platform.sh, which can be used to quickly create an API that can be served by itself or as a Headless CMS data source for another frontend application in the same project. This repository not include a frontend application, but you can add one of your choice and access Strapi by defining it in a relationship in your frontend's `.platform.app.yaml` file.

Strapi is a Headless CMS framework written in Node.js.

## Features

* Node.js 12
* PostgreSQL 12
* Automatic TLS certificates
* npm-based build

## Post-install

1. The first time the site is deployed, Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before any API endpoints can be created. Once you have registered the admin user, you will have access to the **Admin Panel**.
2. After you have created and `admin` user, you will not be able to create Content Types on `master`, since the `master` environment will be running in production, where Content Types are not editable. Create a new development branch, and log back in with your `admin` credentials.
3. Now you can begin adding Content Types to build out the API. By default, no Content Types have been included in the installation *and* any Content Types you add will have secured API endpoints that will make them publicly inaccessible by default. You will need to update the permissions for each Content Type from the *Users & Permissions* section of the **Admin Panel** after you have created them. If you are unfamiliar with how to create Content Types or modify permissions with Strapi, visit the [Quick Start Guide](https://strapi.io/documentation/v3.x/getting-started/quick-start.html) for detailed instructions.
4. This template provides only the API for a full project, but you can modify the repository into a [multi-app project](https://docs.platform.sh/configuration/app/multi-app.html#multiple-applications) where Strapi acts as a separate backend application for the front end of your choice. For example, you can add a frontend ExpressJS application in another directory called `frontend` with its own `.platform.app.yaml` file.

  ```
  .
  ├── .git
  ├── .platform
  │   ├── routes.yaml
  │   └── services.yaml
  ├── backend
  │   ├── .platform.app.yaml
  │   ├── api
  │   ├── config
  │   ├── extensions
  │   ├── package.json
  │   ├── public
  │   └── yarn.lock
  └── frontend
      ├── .platform.app.yaml
      ├── index.js
      ├── package-lock.json
      └── package.json
  ```

## Customizations

The following changes have been made relative to the [quickstart Strapi project](https://strapi.io/documentation/v3.x/getting-started/quick-start.html) to run on Platform.sh.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional module, [config-reader-nodejs](https://github.com/platformsh/config-reader-nodejs), has been added. It provides convenience wrappers for accessing the Platform.sh environment variables.
* There are a few modules downloaded during the build hook to support Strapi:
    * `pg`: supports connection with PostgreSQL.
    * [`graphql`](https://strapi.io/documentation/v3.x/plugins/graphql.html): supports GraphQL queries.
    * [`documentation`](https://github.com/strapi/strapi/tree/master/packages/strapi-plugin-documentation): generates OpenAPI specification and Swagger documentation from models. You can view the documentation at `/docs`, and the final spec at `/docs/spec`. 
* A `platformsh/database.js` file has been addded, which uses `config-reader-nodejs` to retrieve PostgreSQL credentials and connect during the deploy hook. It overrides the quickstart's settings during the build hook.
* A `platformsh/server.js` file configures basic server settings, admin JWT authorization using the Platform.sh environment variable `PLATFORM_PROJECT_ENTROPY`, and GraphQL settings.
* A `platformsh/openapi.json` file overrides the default front matter information in the generated pubic API documentation. 

## References

* [Strapi.io](https://strapi.io/)
* [Strapi Documentation](https://strapi.io/documentation/v3.x)
* [Strapi Quick Start Guide](https://strapi.io/documentation/v3.x/getting-started/introduction.html)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
* [Multi-app on Platform.sh](https://docs.platform.sh/configuration/app/multi-app.html#multiple-applications)