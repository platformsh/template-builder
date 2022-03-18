const forgotPasswordTemplate = {
  subject: "Strapi: Reset your password",
  html: `<p>We heard that you lost your password. Sorry about that!</p>
      <p>But don’t worry! You can use the following link to reset your password:</p>
      <p><a href="<%= url %>">Reset password</a></p>
      <p>Thanks!</p>`,
  text: `We heard that you lost your password. Sorry about that!
  But don’t worry! You can use the following link to reset your password:
  <%= url %>
  Thanks!`
}

module.exports = ({ env }) => ({

  // Basic server settings.
  // 
  // See https://strapi.io/documentation/v3.x/getting-started/deployment.html#application-configuration
  host: env('HOST', '0.0.0.0'),
  port: env.int('PORT', 1337),
  url: env('PUBLIC_URL'),

  // Admin user JWT configuration.
  // 
  // See https://strapi.io/documentation/v3.x/plugins/users-permissions.html#jwt-configuration
  admin: {
      auth: {
        secret: env('PLATFORM_PROJECT_ENTROPY', 'd30722761594d773930740e6a279889b'),
      },
      forgotPassword: {
        emailTemplate: forgotPasswordTemplate
    }
  },
  // GraphQL endpoint configuration.
  // 
  // See https://strapi.io/documentation/v3.x/plugins/graphql.html#usage
  graphql: {
      endpoint: '/graphql',
      shadowCRUD: true,
      playgroundAlways: false,
      depthLimit: 7,
      amountLimit: 100,
      apolloServer: {
          tracing: false,
      }
  },
});
