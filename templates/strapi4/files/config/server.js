module.exports = ({ env }) => ({
  // Basic server settings.
  //
  // See https://strapi.io/documentation/v3.x/getting-started/deployment.html#application-configuration
  host: env("HOST", "0.0.0.0"),
  port: env.int("PORT", 1337),

  // GraphQL endpoint configuration.
  //
  // See https://strapi.io/documentation/v3.x/plugins/graphql.html#usage
  graphql: {
    endpoint: "/graphql",
    shadowCRUD: true,
    playgroundAlways: false,
    depthLimit: 7,
    amountLimit: 100,
    apolloServer: {
      tracing: false,
    },
  },
});
