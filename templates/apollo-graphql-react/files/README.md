# Apollo GraphQL Server and Client with React on Platforn.sh

<p align="center">
  <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/apollo-graphql-react/.platform.template.yaml&utm_content=express&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform"">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
  </a>
</p>

This template shows how to setup a multi-application project exposing a GraphQL API that aggregates external APIs and internal data stored in MongoDB using Apollo Server and a client application using React, consuming the API with Apollo Client.

Apollo Server is an open-source, spec-compliant GraphQL server that's compatible with any GraphQL client.<br />
Apollo Client is state management library for JavaScript that enables you to manage both local and remote data with GraphQL.

## Features

* Node.js 14
* MariaDB 10.4
* Automatic TLS certificates
* Websockets
* yarn-based build

## Getting started

This project uses the YouTube API. Follow [these steps](https://developers.google.com/youtube/v3/getting-started) to get an API key and [export it in an environment variable](https://docs.platform.sh/development/variables.html#environment-variables) called YOUTUBE_API_KEY.

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `./back/.platform.app.yaml`, `./front/.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional module, [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables. See how it is used in `./front/src/index.js` and `./back/src/index.js`.

## References

* [Apollo Server](https://www.apollographql.com/docs/apollo-server/)
* [Apollo Client](https://www.apollographql.com/docs/apollo-client/)
* [React](https://reactjs.org/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
