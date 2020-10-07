const config = require("platformsh-config").config();

var backend_route = "";
if ( config.isValidPlatform() ) {
  require("dotenv").config({
    path: `.env.${process.env.NODE_ENV}`,
  })
    backend_route = `http://${config.credentials("drupal")["host"]}`;
} else {
  require("dotenv").config()
    backend_route = process.env.API_URL;
}

module.exports = {
  siteMetadata: {
    title: `Gatsby + Drupal on Platform.sh`,
    description: `This template builds a two application project to deploy the Headless CMS pattern using Gatsby as its frontend and Drupal for its backend.`,
    author: `@platformsh`,
  },
  plugins: [
    {
      resolve: `gatsby-source-drupal`,
      options: {
        baseUrl: backend_route
      },
    },
    `gatsby-plugin-react-helmet`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`,
      },
    },
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `gatsby-starter-default`,
        short_name: `starter`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
        icon: `src/images/gatsby-icon.png`, // This path is relative to the root of the site.
      },
    },
    // this (optional) plugin enables Progressive Web App + Offline functionality
    // To learn more, visit: https://gatsby.dev/offline
    // `gatsby-plugin-offline`,
  ],
}
