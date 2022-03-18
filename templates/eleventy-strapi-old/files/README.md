# Eleventy Strapi multi-app for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/eleventy-strapi/.platform.template.yaml&utm_content=eleventy-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template deploys a two application project on Platform.sh: one for a frontend static site generator, Eleventy, and the other for a backend headless CMS, Strapi. Like our other "decoupled" templates, Eleventy's build is delayed until the `post_deploy` hook, at which point the backend Strapi content data becomes available to query using GraphQL. That data then is reformatted into "Blogs" on the frontend. Both applications utilize the Platform.sh Configuration Reader library for Node.js. It is intended for you to use as a starting point and modify for your own needs.

Note that there are several setup steps required after the first deploy. An `article` content type has already been committed, but you will still need to follow the post deploy instructions to add content and define permissions for Eleventy to consume it. 

Eleventy is a static site generator written in Node.js, and Strapi is a headless CMS framework also written in Node.js.

## Features

* Node.js 12 & 14
* PostgreSQL 12
* Automatic TLS certificates
* yarn-based build
* Multi-app configuration
* Delayed SSG build (post deploy hook)

## Post-install

On initial deploy, Eleventy will fail since Strapi is not yet serving data that it can consume. There are only a few post deploy steps you will need to perform to get the fully running project. 

### 1. Create an admin user

Visit the `backend.<generated url>` subdomain. Strapi will direct you to visit the `/admin` path to register an administrative user. You will need to register an admin user before you can create any content.

### 2. Write some content

Once you have registered the admin user, you will have access to the **Admin Panel**. Typically collections cannot be added in production, and on your Master environment Strapi will be running in production mode. Because of this, the repository already includes the necessary collection Eleventy expects called `Article`, which you can find in `strapi/api/article/`. It includes the following fields:

* `title`
* `content`
* `author`
* `slug`

Add a few posts, filling out each field for each post. When you're finished with a post, make sure to click "Save" and then "Publish". 

### 3. Set public permissions

Now that you have a collection and some data associated with it, you still need to make that data accessible to the outside world - and more importantly, to Eleventy. 

Go to "Settings" on the sidebar and select "Roles" under the "Users & Permissions Plugin" section. Go to the "Public" role, and you will see the permission settings for the "Articles" collection. Select `find` and `findone`, then save your changes. 

You should now be able to run the command locally and get your articles:

```bash
$ curl https://www.backend.master-<generated_url>/articles | jq
[
  {
    "id": 1,
    "title": "The Boy Who Cried Wolf",
    "content": "\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sodales lacus in vehicula varius. Mauris accumsan congue elit in imperdiet.",
    "author": "Daniel Phiri",
    "slug": "the-boy-who-cried-wolf",
    "published_at": "2021-02-11T17:01:32.440Z",
    "created_at": "2021-02-11T17:01:28.534Z",
    "updated_at": "2021-02-11T17:01:32.455Z"
  }
]
```

### 4. Redeploy

Now that the Strapi data is accessible, redeploy the environment, which will allow Eleventy to rebuild itself now using that data:

```bash
platform redeploy <PROJECT_ID> -e master
```

## Local development

Data is pulled into Eleventy from Strapi within the `eleventy/_data/blogposts.js` file. The script detects whether Eleventy's build is occuring on a Platform.sh environment, at which point it uses the `strapi` relationship defined in `eleventy/.platform.app.yaml` to make an internal request to that container. 

When developing locally, `blogposts.js` contains two other assumed modes. In the first, Eleventy assumes that there is a local Strapi server running at its default address of `http://localhost:1337`. In the second, the script detects a `API_URL` environment variable (which can be set in a `.env` file and read with `dotenv`) and uses that as the data source. 

### Local Strapi server

> **Requirements:**
>
> - yarn 
> - `git clone https://github.com/platformsh-templates/eleventy-strapi`

`strapi/config/server.js` is written to use a local, un-committed SQLite database (`.tmp/data.db`) by default. Run:

```bash
$ cd strapi
$ yarn --frozen-lockfile 
$ yarn develop
```

If setting up for the first time, follow the [post install instructions](#post-install) above to set up an admin user and prepare content. Once you have done so, run the Eleventy development server in another terminal:

```bash
$ cd eleventy
$ yarn --frozen-lockfile 
$ yarn serve
```

### Remote Strapi server on Platform.sh

> **Requirements:**
>
> - yarn 
> - [Platform.sh CLI installed](https://docs.platform.sh/development/cli.html#installation)
> - The project cloned locally, either by using the "Git" dropdown in the management console or using the CLI command `platform get`.

This case assumes that you have already deployed this template to a Platform.sh project and followed the [post install instructions](#post-install) above. 

Use the CLI to get the Strapi backend URL from the environment on Platform.sh, and write to a `.env` file:

```bash
$ cd eleventy
$ echo API_URL=https://backend.$(platform environment:info edge_hostname) >> .env
```

Then run the server:

```bash
$ yarn --frozen-lockfile 
$ yarn serve
```

### Developing with Strapi and Platform.sh

In this template, the Strapi admin panel has been configured to run on a development server on non-production environments. This difference from production allows you to define new collections at runtime on Platform.sh as an admin. In order to accomplish this on Platform.sh, where deployed environments are read-only filesystems, the `api` subdirectory where a new collections are defined (i.e., `api/articles` as in this template) is defined as a [mount](https://docs.platform.sh/configuration/app/storage.html#mounts). 

There are a few caveats to this decision you should keep in mind when developing new collections with Strapi on Platform.sh.

First, if you create new collections at runtime, and then merge that environment into production, that new collection *will not* appear on your production Strapi instance. On Platform.sh, code and data are treated as wholly distinct, and it is expected that your environments exist on a read-only filesystem by default. That is to say that code can travel up into parent branches, but data only flows downwards to child branches. 

You can still develop new collections on your non-production Platform.sh environment, but in order for them to end up in production, you will need to download the contents of that mount and commit those changes to your repository:

```bash
$ platform mount:download -p <PROJECT_ID> -e <DEV_ENVIRONMENT> --app strapi -m api --target api
$ git add api && git commit -m "Get upstream Strapi API changes."
```

For this reason, it is recommended that you develop new collections locally to begin with, and then push to Platform.sh to avoid forgetting this step. 

Second, when the deploy phase begins, *anything existing in a subdirectory that has been defined as a mount will be overwritten on Platform.sh*. What this *should* mean is that any new collections you have committed to `api`, such as `api/articles`, would be overwritten during deployment. To keep this from happening, the `scripts/handle_mounts.sh` script has been included. It runs at build time to stage committed collections in a temporary directory, and then again at deploy time to restore those files to the mounted directory. The script detects which directories to perform this action on from the `mounts` key of your `.platform.app.yaml` file, through the `PLATFORM_APPLICATION` environment variable. 

You can keep or modify this script for your needs, but keep in mind that if removed anything you have committed to subdirectories that have also been defined as `mounts` will be overwritten at deploy time.

## Customizations

Much of this template has been inspired by the [Building a Blog with 11ty and Strapi](https://strapi.io/blog/building-a-blog-with-11ty-and-strapi) post written by Daniel Madalitso Phiri from Strapi's blog. Major credit goes to Daniel for this template existing in the first place.

That being said, there have been some slight modifications to the [final repository](https://github.com/malgamves/11ty-x-strapi) linked in that post. Most of those changes are specific to pulling information from Platform.sh environments, while others simply add more places Strapi data is present that were not in the original article (the sitemap, for example).

For that reason, many of the customizations listed below include files covered in the original post, and that post's final repository is not considered the starting point in those descriptions. 

Instead we use the following starting point, which duplicates some of the steps in that post: this template uses Strapi's quickstart (`yarn create strapi-app backend --quickstart`) as an initial skeleton for the backend application, and the [base blog repository](https://github.com/11ty/eleventy-base-blog) for the Eleventy frontend. The following files and additions make the template work on Platform.sh.  If using this project as a reference for your own existing project, replicate the changes below to your project.

### Project

* The `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh. In this project, it contains PostgreSQL configuration, which Strapi uses as its database. You may customize them as you see fit.

### Eleventy (`eleventy`)

* A `.platform.app.yaml` file has been added. All application containers require this file on Platform.sh. It defines how Eleventy is built and deployed, which directories need write access at runtime, and over which relationship Eleventy can retrieve data from the Strapi backend (`strapi`).
* A `.environment` file has been added. This file provides a way to commit environment variables to a repository, including those that use information about the Platform.sh environment to set them. It is sourced during the start command onwards and when you SSH into the container. It retrieves the current URL for the application, which is used for setting metadata configuration. 
* The `dotenv` package has been added to facilitate the [local development](#local-development) variations for building Eleventy. 
* The packages `node-fetch` and the Platform.sh Configuration Reader library for Node.js have been added to use the current Platform.sh environment to pull data from the backend Strapi container. 
* A `comment` `pairedShortcode` has been added to `.eleventy.js` because it was missing from the upstream.
* A `css/platformsh.css` stylesheet has been added for minor style changes, and to support the `comment` shortcode. It is also imported into the base template, `_includes/layouts/base.njk`. 
* The `feed/feed.njk` and `feed/json.njk` have been modified to include the Strapi article data in its sitemaps. 
* A subdirctory for presenting Strapi content called `blogs` has been added, which includes a list template (`blogs/list.njk`) and a single template (`blogs/single.njk`). Both utilize the `blogposts` data object defined in `_data/blogposts.js` These files have been copied from [Daniel Madalitso Phiri's original article](https://strapi.io/blog/building-a-blog-with-11ty-and-strapi).
* A `_data/blogposts.js` file has been added. This file is the primary place where data from a Strapi source is retrieved and made available to Eleventy. If on a Platform.sh environment, it places an internal request on the `strapi` app container. See [local development](#local-development) for its local assumptions. This file has been largely copied from [Daniel Madalitso Phiri's original article](https://strapi.io/blog/building-a-blog-with-11ty-and-strapi), save for these Platform.sh environment and local development considerations. It also includes several fields included by default on Strapi entries that were not in the original post but are necessary for this template. 
* A `_data/metadata.js` file has been added, which overrides the default `_data/metadata.json` file. This script updates the `metadata` object with information from the Platform.sh environment when deployed.

### Strapi (`strapi`)

* A `.platform.app.yaml` file has been added. All application containers require this file on Platform.sh. It defines how Strapi is built and deployed, and which directories need write access at runtime. It has been written to build a production site on the Master environment, and run a development server on non-production environments. This is because Strapi does not allow collection creation when in production. See the [developing with Strapi](#developing-with-strapi-and-platform-sh) section for more details.
* A `.environment` file has been added. This file provides a way to commit environment variables to a repository, including those that use information about the Platform.sh environment to set them. It is sourced during the start command onwards and when you SSH into the container. It retrieves the current URL for the application, which is used for configuring e-mail and JWT authentication. 
* The `pg` module has been added to allow Strapi to connect to Platform.sh. 
* The Platform.sh Configuration Reader library for Node.js has been added to retrieve database credentials from the Platform.sh environment.
* The `strapi-provider-email-nodemailer` plugin has been added to enable email on the Master environment.
* A `handle_mounts.sh` script has been added. This script handles committed files pushed to directories also defined as mounts on Platform.sh. See the [local development](#local-development) section for more details.
* A `config/database.js` file has been added. When developing on Platform.sh, this file will pull data using an internal request to the `strapi` app container. Otherwise, it will use a local SQLite database. See the [local development](#local-development) section for more details.
* A `config/plugins.js` file has been added. Strapi does not come by default with a quick way to configure email, such as sending an email for a forgotten password. This file configures the `strapi-provider-email-nodemailer` plugin to use SMTP environment variables on Platform.sh to enable e-mail. Note that email is only supported on Master environments by default, but you can change this in your environment settings if desired. 
* The `config/server.js` file has been modified to read information from the Platform.sh environment to configure the Strapi server, admin authentication secrets, and template text for a forgot password email. 
* An `api/article` collection has been included as a part of Strapi's API. In this template, Eleventy expects data at Strapi's `/articles` and `/article/{id}` endpoints, and these files set that up for you automatically. 

## References

* [Building a Blog with 11ty and Strapi](https://strapi.io/blog/building-a-blog-with-11ty-and-strapi) by Daniel Madalitso Phiri
* [Strapi](https://strapi.io/)
* [Strapi documentation](https://strapi.io/documentation/developer-docs/latest/getting-started/introduction.html)
* [Eleventy](https://www.11ty.dev/)
* [Eleventy documentation](https://www.11ty.dev/docs/)
