# Gatsby Strapi multi-app for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/gatsby-strapi/.platform.template.yaml&utm_content=gatsby-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a two application project to deploy the Headless CMS pattern using Gatsby as its frontend and Strapi for its backend. The `gatsby-source-strapi` source plugin is used to pull data from Strapi during the `post_deploy` hook into the Gatsby Data Layer and build the frontend site. Gatsby utilizes the Platform.sh Configuration Reader library for Node.js to define the backend data source in its configuration. It is intended for you to use as a starting point and modify for your own needs.

Note that there are several setup steps required after the first deploy to create your first content types and access permissions in Strapi. See the included README's post-install section for details.

Gatsby is a free and open source framework based on React that helps developers build blazing fast websites and apps, and Strapi is a Headless CMS framework written in Node.js.

## Features

* Node.js 14
* PostgreSQL 12
* Automatic TLS certificates
* yarn-based build
* Multi-app configuration
* Delayed SSG build (post deploy hook)

## Post-install

This template uses Strapi's [Starter Gatsby Blog](https://github.com/strapi/strapi-starter-gatsby-blog) to deploy a multi-app project on Platform.sh. After it has deployed however, you will still need to manually set up Strapi's Admin Panel and an initial piece of content so that the Gatsby frontend application can fully build.

### Create an admin user

Visit the `backend.<generated url>` subdomain. Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before any API endpoints can be created.

### Set up the API
Once you have registered the admin user, you will have access to the **Admin Panel**, and from there you can begin adding Content Types to build out the API.
The frontend Gatsby application will attempt to index two content types by default: Articles and Categories.

#### Articles

In the Admin Panel, create your first content/collection type (Display name: `article`) with four fields:

- **Text:**
  - Base Settings:
    - Name: `title`
    - Type: `Short text`
  - Advanced Settings: `Required field`
- **Rich Text**
  - Base Settings:
    - Name: `content`
  - Advanced Settings: `Required field`
- **Media**
  - Base Settings:
    - Name: `image`
    - Type: `Single media`
  - Advanced Settings: `Required field`
- **Date**
  - Base Settings:
    - Name: `published_at`
    - Type: `date`
  - Advanced Settings: `Required field`

Save those changes (the server will restart).

Then, visit the `Articles` Collection, and `Add a New Article` to test. Include the required `title`, `content`, and `image`, and select a date for the post. Save it.

#### Categories

Return to the Content-Types Builder, and `Create a new collection type` called (Display name) `category` with two  fields:

- **Text**
  - Base Settings:
    - Name: `name`
    - Type: `Short text`

Finish, and save those changes (the server will restart).

#### Back to Articles

Return to the Content-Types Builder, and add a new field to the `Articles` collection.

- **Relation**
  - On the right hand dropdown, select Category
  - Then select the "many-to-one" icon, which will read `Category has many Articles` when selected.

Visit the `Category` collection in the upper left section of the sidebar, and then click `Add New Category`. Name it whatever you'd like. On the right hand side in the `Articles` dropdown menu, select the article you created, then click Save.

#### Permissions

Visit `Roles & Permissions` in the sidebar, and select `Public` permissions. Then adjust the permissions for your two collections:

  - `Category`: select `find` and `findone`
  - `Article`: select `find` and `findone`

Save your changes.

After you have completed the above steps, you will be able to test their availability at `<backend-url>/articles`, `<backend-url>/articles/1`, `<backend-url>/categories`, and `<backend-url>/categories/1`.

To rebuild the Gatsby frontend with this new data, run the command `platform redeploy -p <PROJECT ID> -e master` to redeploy the environment.

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
* `frontend/gatsby-config.js` has been modified to read the Strapi backend url and assign it to the `apiURL` attribute for the `gatsby-source-strapi` plugin. Since routes are not available during the build hook, and since we want this value to be generated and unique on each environment, `gatsby build` runs and pulls in content from the Wordpress app during the `post_deploy` hook on the mounted `public` directory.
* For Strapi, the `start` command calls the script `backend/start.sh`, which is configured to run Strapi as a development environment, allowing you to create new Content Types once it is deployed, even on the master/production branch of your project. We recommend adjusting this command to run Strapi in `production` mode on the master branch (`start.sh` includes an example environment-specific start command that can be used to accomplish this).

## References

* [Gatsby](https://www.gatsbyjs.org/)
* [gatsby-source-strapi on GitHub](https://github.com/strapi/gatsby-source-strapi)
* [Building a Static Blog using Gatsby and Strapi](https://strapi.io/blog/build-a-static-blog-with-gatsby-and-strapi)
* [Gatsby CMS with Strapi](https://strapi.io/gatsby-cms)
* [Strapi](https://strapi.io/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
