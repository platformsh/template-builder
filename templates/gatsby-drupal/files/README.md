# Gatsby Drupal multi-app for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/gatsby-drupal/.platform.template.yaml&utm_content=gatsby-drupal&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a multi-app project using Gatsby as its frontend and a Drupal backend to store content using Gatsby's Drupal source plugin.

Gatsby is a free and open source framework based on React that helps developers build statically-generated websites and apps, and Drupal is a flexible and extensible PHP-based CMS framework.

> **Note:** This project will require at least a Medium plan.

## Services

* Node.js 12
* PHP 7.3
* MariaDB 10.4
* Redis 5.0

## Post-install

1. When you initially deploy the template, you will receive a `403` error on the base route. There is not yet any content to build the Gatsby site, because Drupal has not yet been fully installed. Visit the `backend.<generated url>` subdomain, and run through the Drupal installer as normal. You will not be asked for database credentials as those are already provided.
2. Once you have completed the Drupal install, you will need to enable a few plugins in order to fully configure it to be used as a backend for the Gatsby site. From the admin page, install the following from **Extend**:

- Gatsby JSON:API Extras
- Gatsby JSON:API Instant Preview and Incremental Builds
- JSON API
- JSON API Extras
- Serialization
- Pathauto

3. Set up aliases for your articles. From **Configuration**, go to the subsection *Search and Metadata* and click on *URL aliases*. With Pathauto enabled, you should be able to click on a header called *Pattern*. Click *Add Pathauto pattern*, and set it with the following fields:
    - Pattern type: Content
    - Path pattern: `/articles/[node:title]`
    - Content type: Article
    - Label: `pathautho-article`
    - Enabled

  Save the pattern. Now *Articles*, which would typically be available at `/node/<NODE NUMBER>` will have an alias at `/articles/<slug-of-article-title>`, which will be replicated on the final Gatsby site.

4. Add *Articles* by clicking the **Content** tab. Make sure to include all of the required fields in *Articles* (title, summary, body, image, and alt text for the image).

> **Note:** If you plan on enabling Gatsby Live Preview on your development environments, make sure to add at least two Articles now (larger description in Live Preview section below).

5. With the above steps completed, redeploy the environment with `platform redeploy -p <PROJECT ID> -e master`. The environment will redploy, and the Gatsby site will pull data from the backend Drupal API.

### Enabling Gatsby Live Preview

> **Note:** Live Preview is not enabled by default on *Master* environments, but it can be set up manually on your development environments.
> **Note:** After Live Preview is enabled, you will be able to edit content within Drupal, which will cause that content to update on Gatsby automatically for changes to its title, summary and body. Make sure to have at least two articles in Drupal before attempting to update an article's image. Gatsby temporarily is not able to locate the article during the update, and the environment will have to be redeployed. As long as there is more than one article present, this problem will not be encountered.  

1. On the **Configuration** panel, click on *Gatsby Settings* in the **Web Services** section.
2. Update the following fields and save the new configuration:
  - Gatsby Preview Server URL: the root url for your environment (`https://master-<hash>-<projectId>.<region>.platformsh.site/`)
  - Incremental Build Server Callback Hook(s): `<root-url-above>/__refresh`
  - Entity types to send to Gatsby Preview and Build Server:
      - File
      - Content
      - URL alias
3. Update an Article. Go to one of your articles, and update any of the fields.

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* Additional Platform.sh configuration reader modules for both [PHP](https://github.com/platformsh/config-reader-php) and [Node.js](https://github.com/platformsh/config-reader-nodejs) have been added. They provide convenience wrappers for accessing the Platform.sh environment variables.
* `gatsby-config.js` has been modified to read the Wordpress backend url and assign it to the `baseUrl` attribute for the `gatsby-source-wordpress` plugin. Since routes are not available during the build hook, and since we want this value to be generated and unique on each environment, `gatsby build` runs and pulls in content from the Wordpress app during the `post_deploy` hook on the mounted `public` directory. `gatbsby-source-wordpress` can have additional parameters set to modify your configuration, so consult the [documentation](https://www.gatsbyjs.org/packages/gatsby-source-wordpress/#how-to-use).

## References

* [Gatsby](https://www.gatsbyjs.org/)
* [gatsby-source-drupal](https://www.gatsbyjs.org/packages/gatsby-source-drupal/)
* [Dedcoupled Drupal by Lullabot](https://www.google.com/search?client=safari&rls=en&q=gatsby+drupal&ie=UTF-8&oe=UTF-8)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
* [Drupal](https://drupal.org/)
* [Drupal on Platform.sh](https://docs.platform.sh/frameworks/drupal.html)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
