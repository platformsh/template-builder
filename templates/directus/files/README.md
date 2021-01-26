# Directus for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/directus/.platform.template.yaml&utm_content=directus&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building Directus for Platform.sh. It includes a quickstart application configured to run with PostgreSQL. It is intended for you to use as a starting point and modify for your own needs.

Directus is an open-source platform that allows you to create and manage an API from data stored in a database.

## Features

* Node.js 12
* PostgreSQL 12
* Redis 6.0
* Automatic TLS certificates
* npm-based build

## Post-install

### Admin user

This template does not require any additional configuration once deployed to start developing your Directus application. During the first deploy, however, an admin user was added to allow you to log in. Those credentials are set (along with many other Platform.sh-specific settings) in the `.environment` file:

```txt
# Initial admin user on first deploy.
export INIT_ADMINUSER='admin@example.com'
export INIT_ADMINPW='password'
```

After you log in for the first time, be sure to update this password immediately. 

### Database

Although this project uses PostgreSQL as its primary database, Directus supports [a number of other options](https://docs.directus.io/guides/installation/cli.html#_1-confirm-minimum-requirements-are-met) that can be easily substituted using Platform.sh's managed services. 

- [MariaDB](https://docs.platform.sh/configuration/services/mysql.html)
- [Oracle MySQL](https://docs.platform.sh/configuration/services/mysql.html)
- [PostgreSQL](https://docs.platform.sh/configuration/services/postgresql.html)

### Logging

The Directus CLI is used to create both a role UUID for admin users, and to use that UUID to create the initial admin user. Currently, having a `LOG_LEVEL` for Directus other than `silent` causes the log message to be included in the following line from the `.platform.app.yaml` file's deploy hook, resulting in a syntax error when creating that first user:

```yaml
ROLE_UUID=$(npx directus roles create --name admin --admin)
```

This is only something to be aware of on the first install, or when using a similar method for creating new users using the CLI. After you have deployed Directus and created the first admin user, you will likely want to update the `.environment` file to set more reasonable environment-dependent log messages:

```txt
if [ "$PLATFORM_BRANCH" != "master" ] ; then
    export LOG_LEVEL="debug"
else
    export LOG_LEVEL="info"
fi
```

## Customizations

The following files and additions make the framework work on Platform.sh on top of the basic quickstart project (`npx create-directus-project`). If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.environment` file provides Platform.sh-specific environment variable overrides from the generated default `.env` settings for Directus and PostgreSQL. It also sets an initial username and password for an admin user. On Platform.sh, a `.env` file is required to configure Directus but is not committed (see below) in this project. Rather, at build time Directus's `example.env` file (`node_modules/directus/example.env`) is renamed in its place with a set of standard defaults which are then overridden by `.environment`. Consult this file locally, and then override with your own settings in `.environment` when appropriate. 
* A `.gitignore` file has been added to prevent `node_modules` and your `.env` generated for local development from being committed. 

## Local development

1. Add the database

    With this configuration, you will need to manually add Directus's database before running locally. For Postgresql:

    ```txt
    $ psql
    psql (12.4)
    Type "help" for help.

    me=# create database directus;
    CREATE DATABASE
    ```

2. Set up your database

    Run the commands below, and then follow the CLI prompts provided to configure Directus on your local database installation:

    ```bash
    $ npm install
    $ npx directus init
    ```

3. Run the server

    Run the Directus server locally with the command `npx directus start`.

## References

* [Directus Documentation](https://docs.directus.io/getting-started/introduction.html)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
