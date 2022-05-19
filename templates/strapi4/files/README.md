# Strapi v4 template for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/strapi4/.platform.template.yaml&utm_content=strapi4&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a Strapi backend for Platform.sh, which can be used to quickly create an API that can be served by itself or as a Headless CMS data source for another frontend application in the same project. This repository does not include a frontend application, but you can add one of your choice and access Strapi by defining it in a relationship in your frontend's `.platform.app.yaml file.`

Strapi is a Headless CMS framework written in Node.js.

## Features

- Strapi v4
- Node.js 12
- PostgreSQL 12, MySQL 8
- Automatic TLS certificates
- yarn-based build

## Post-install

1. The first time the site is deployed, Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before any API endpoints can be created. Once you have registered the admin user, you will have access to the **Admin Panel**.
2. After you have created and `admin` user, you will not be able to create Content Types on `master`, since the `master` environment will be running in production, where Content Types are not editable. Create a new development branch, and log back in with your `admin` credentials.
3. Now you can begin adding Content Types to build out the API. By default, no Content Types have been included in the installation _and_ any Content Types you add will have secured API endpoints that will make them publicly inaccessible by default. You will need to update the permissions for each Content Type from the _Users & Permissions_ section of the **Admin Panel** after you have created them. If you are unfamiliar with how to create Content Types or modify permissions with Strapi, visit the [Quick Start Guide](https://strapi.io/documentation/v3.x/getting-started/quick-start.html) for detailed instructions.
4. This template provides only the API for a full project, but you can modify the repository into a [multi-app project](https://docs.platform.sh/configuration/app/multi-app.html#multiple-applications) where Strapi acts as a separate backend application for the front end of your choice. You can view our [Gatsby with Strapi template](https://github.com/platformsh-templates/gatsby-strapi) as an example.

## Customizations

The following changes have been made relative to the [quickstart Strapi project](https://strapi.io/documentation/v3.x/getting-started/quick-start.html) to run on Platform.sh. If using this project as a reference for your own existing project, replicate the changes below to your project.

- The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh. You may customize them as you see fit.
- The `.platform.app.yaml` file has been configured to run your production Strapi server on all environments you create. While you will be able to add content to an existing Content Type on `master`, you will only be able to create new Content Types during local development.
- There are a few modules that have been added to support Strapi:
  - [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs): Provides convenience wrappers for accessing the Platform.sh environment variables.
  - `pg`: supports connection with PostgreSQL.
  - [`graphql`](https://strapi.io/documentation/v3.x/plugins/graphql.html): supports GraphQL queries.
  - [`documentation`](https://github.com/strapi/strapi/tree/master/packages/strapi-plugin-documentation): generates an OpenAPI specification and Swagger documentation from your models. You can view the documentation at `/docs`, and the final spec at `/docs/spec`.

## Local development

The `config/database.js` file is set up to detect whether Strapi is running on Platform.sh or not using `config-reader-nodejs`. If Platform.sh is not detected, Strapi will default to a local SQLite database in`.tmp`.

## Extending

You can add additional plugins for Strapi locally by adding them as dependencies using Yarn. In most cases, official Strapi modules can be added with `yarn strapi install <plugin-name>`.

Customizing modules will differ slightly for each plugin. The `strapi-plugin-documentation` plugin for example generates an OpenAPI specification from your API and public Swagger documentation at `<your-domain>/docs`. Overrides are applied to that process using the `extensions/documentation/config/settings.json` file in this repository. In other cases, there will be a specific `overrides` subdirectory within `extensions/<plugin-name>` you will need to use, so check that plugin's documentation for details. Be aware of whether the plugin needs write access at runtime, and be sure to define matching mounts in your `.platform.app.yaml` file if necessary.

## Switching Database

Strapi v4 currently has support for PostgreSQL and MySQL. This template is built with PostgreSQL by default but in the event where you need to use a MySQL database, you can switch to a MySQL database by following these steps:

- In the `services.yaml` file, replace the postgres database with mysql:

```yaml
# Uncomment the line below if you would like to use a mysql database
dbmysql:
  type: oracle-mysql:8.0
  disk: 256
```

- In the `.platform.app.yaml` file, replace the `postgresdatabase` relationship with the following:

```yaml
relationships:
  mysqldatabse: "dbmysql:mysql"
```

- In the `database.js` file, replace the content with the following:

```js
const path = require("path");
const config = require("platformsh-config").config();

let dbRelationship = "mysqldatabase";

// Strapi default sqlite settings.
let connection = {
  connection: {
    client: "sqlite",
    connection: {
      filename: path.join(
        __dirname,
        "..",
        process.env.DATABASE_FILENAME || ".tmp/data.db"
      ),
    },
    useNullAsDefault: true,
  },
};

if (config.isValidPlatform() && !config.inBuild()) {
  // Platform.sh database configuration.
  const credentials = config.credentials(dbRelationship);
  console.log(
    `Using Platform.sh configuration with relationship ${dbRelationship}.`
  );

  connection = {
    connection: {
      client: "mysql",
      connection: {
        host: credentials.ip,
        port: credentials.port,
        database: credentials.path,
        user: credentials.username,
        password: credentials.password,
        ssl: false,
      },
      debug: false,
    },
  };
} else {
  if (config.isValidPlatform()) {
    // Build hook configuration message.
    console.log(
      "Using default configuration during Platform.sh build hook until relationships are available."
    );
  } else {
    // Strapi default local configuration.
    console.log(
      "Not in a Platform.sh Environment. Using default local sqlite configuration."
    );
  }
}

console.log(connection);

// export strapi database connection
module.exports = ({ env }) => connection;
```
The difference between the above and the existing configuration is that, we have changed the database client to mysql and we removed postgres database connection settings that are not relevant to MYSQL.

- The last step is to commit these settings to your git repository and deploy on Platform.sh
## References

- [Strapi v4 Documentation](https://docs.strapi.io/developer-docs/latest/getting-started/introduction.html)

- [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
