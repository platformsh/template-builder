# Apollo Server for Platform.sh

This application demonstrates deploying a GraphQL API with Apollo Server. It provides an endpoint aggregating the YouTube API with local data stored in a MongoDB database.

Apollo Server is an open-source, spec-compliant GraphQL server that's compatible with any GraphQL client.

## Features

* Node.js 14
* MariaDB 10.4
* Automatic TLS certificates

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `/.platform/services.yaml`, and `/.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional module, [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Apollo Server](https://www.apollographql.com/docs/apollo-server/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
