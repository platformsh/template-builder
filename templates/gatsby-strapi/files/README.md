# Gatsby Strapi multi-app for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/gatsby-strapi/.platform.template.yaml&utm_content=gatsby-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a multi-app project using Gatsby as its frontend and a Strapi backend to store content using the Gatsby source plugin for Strapi.

Gatsby is a free and open source framework based on React that helps developers build blazing fast websites and apps, and Strapi is a Headless CMS framework written in Node.js.

## Services

* Node.js 12
* PostgreSQL 12

## Post-install

1. When you initially deploy the template, you will receive a `403` error on the base route. There is not yet any content to build the Gatsby site, because Strapi does not yet have an API to serve. Visit the `backend.<generated url>` subdomain. Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before any API endpoints can be created.
2. Once you have registered the admin user, you will have access to the **Admin Panel**, and from there you can begin adding Content Types to build out the API.
The frontend Gatsby application will attempt to index two content types by default: Articles and Categories. You can view Strapi's tutorial for [setting up a Static blog using Gatsby and Strapi](https://strapi.io/blog/build-a-static-blog-with-gatsby-and-strapi), where it contains a detailed tutorial for creating these first two content types as well as your first post.

## Local development

`gatsby-config.js` has been modified to set the `gatsby-source-strapi` plugin's `apiURL` attribute automatically on a Platform.sh environment.

If developing your Gatsby app locally, this value will instead be sent to a url string set to the `API_URL` variable in your local `.env` file:

```bash
# .env

API_URL="https://www.backend.pr-1-djjnuwy-muwzogvpcpoe2.eu-3.platformsh.site"
```

> **Note:**
>
> The `apiURL` attribute will fail to retrieve posts if it contains a trailing slash, so be sure to exclude it when setting `API_URL`. 

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Platform.sh configuration reader module for [Node.js](https://github.com/platformsh/config-reader-nodejs) has been added. It provides convenience wrappers for accessing the Platform.sh environment variables.
* `gatsby-config.js` has been modified to read the Strapi backend url and assign it to the `apiURL` attribute for the `gatsby-source-strapi` plugin. Since routes are not available during the build hook, and since we want this value to be generated and unique on each environment, `gatsby build` runs and pulls in content from the Wordpress app during the `post_deploy` hook on the mounted `public` directory.

## References

* [Gatsby](https://www.gatsbyjs.org/)
* [gatsby-source-strapi](https://github.com/strapi/gatsby-source-strapi)
* [Building a Static Blog using Gatsby and Strapi](https://strapi.io/blog/build-a-static-blog-with-gatsby-and-strapi)
* [Gatsby CMS with Strapi](https://strapi.io/gatsby-cms)
* [Strapi](https://strapi.io/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
