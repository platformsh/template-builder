module.exports = ({ env }) => ({
  // ...,
  graphql: {
    config: {
      endpoint: "/graphql",
      apolloServer: {
        introspection: true,
      },
    },
  },
});
