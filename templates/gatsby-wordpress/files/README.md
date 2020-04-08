# Gatsby Wordpress multi-app for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/gatsby-wordpress/.platform.template.yaml&utm_content=gatsby-wordpress&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a multi-app project using Gatsby as its frontend and a Wordpress backend to store content using Gatsby's Wordpress source plugin.

Gatsby is a free and open source framework based on React that helps developers build statically-generated websites and apps, and WordPress is a blogging and lightweight CMS written in PHP.

## Services

* Node.js 12
* PHP 7.3
* MariaDB 10.4

## Post-install

1. When you initially deploy the template, you will receive a `403` error on the base route. There is not yet any content to build the Gatsby site, because Wordpress has not yet been fully installed. Visit the `backend.<generated url>` subdomain, and run through the Wordpress installer as normal. You will not be asked for database credentials as those are already provided.
2. Once you have completed the Wordpress install, redeploy the environment with `platform redeploy -p <PROJECT ID> -e master`.

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* Additional Platform.sh configuration reader modules for both [PHP](https://github.com/platformsh/config-reader-php) and [Node.js](https://github.com/platformsh/config-reader-nodejs) have been added. They provide convenience wrappers for accessing the Platform.sh environment variables.
* `gatsby-config.js` has been modified to read the Wordpress backend url and assign it to the `baseUrl` attribute for the `gatsby-source-wordpress` plugin. Since routes are not available during the build hook, and since we want this value to be generated and unique on each environment, `gatsby build` runs and pulls in content from the Wordpress app during the `post_deploy` hook on the mounted `public` directory. `gatbsby-source-wordpress` can have additional parameters set to modify your configuration, so consult the [documentation](https://www.gatsbyjs.org/packages/gatsby-source-wordpress/#how-to-use).

## References

* [Gatsby](https://www.gatsbyjs.org/)
* [gatsby-source-wordpress](https://www.gatsbyjs.org/packages/gatsby-source-wordpress/)
* [WordPress Source Plugin Tutorial](https://www.gatsbyjs.org/tutorial/wordpress-source-plugin-tutorial/)
* [Node.js http](https://nodejs.org/api/http.html#http_http)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
* [WordPress](https://wordpress.org/)
* [WordPress on Platform.sh](https://docs.platform.sh/frameworks/wordpress.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
