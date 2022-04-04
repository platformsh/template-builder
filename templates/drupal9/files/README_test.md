
<p align="right">
<a href="https://platform.sh">
<img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
</a>
</p>

<p align="center">
<a href="https://www.drupal.org/">
<img src="header_test.svg">
</a>
</p>

<h1 align="center">Deploy Drupal 9 on Platform.sh</h1>

<p align="center">
<strong>Contribute, request a feature, or check out our resources</strong>
<br />
<br />
<a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Request a feature</strong></a>
<br /><br />
</p>

<p align="center">
<a href="https://github.com/platformsh-templates/drupal9/issues">
<img src="https://img.shields.io/github/issues/platformsh-templates/drupal9.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh-templates/drupal9.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9/blob/master/LICENSE">
<img src="https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&labelColor=f4f2f3&color=ffd9d9" alt="License" />
</a>&nbsp&nbsp
<br /><br />
<a href="https://console.platform.sh/projects/create-project/?template=https://raw.githubusercontent.com/platformsh-templates/drupal9/updates/.platform.template.yaml&utm_campaign=deploy_on_platform?utm_medium=button&utm_source=affiliate_links&utm_content=https://raw.githubusercontent.com/platformsh-templates/drupal9/updates/.platform.template.yaml" target="_blank" title="Deploy with Platform.sh"><img src="https://platform.sh/images/deploy/deploy-button-lg-blue.svg" width="175px"></a>
</p>
</p>

<hr>

<p align="center">
<strong>Contents</strong>
<br /><br />
<a href="#about"><strong>About</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#getting-started"><strong>Getting started</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#customizations"><strong>Customizations</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#migration"><strong>Migration</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contact"><strong>Contact</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#resources"><strong>Resources</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contributing"><strong>Contributing</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<hr>

## About

This template builds Drupal 9 using the "Drupal Recommended" Composer project.  It is pre-configured to use MariaDB and Redis for caching. The Drupal installer will skip asking for database credentials as they are already provided.

Drupal is a flexible and extensible PHP-based CMS framework.

### Features

- PHP 8.1
- MariaDB 10.4
- Redis 6
- Drush included
- Automatic TLS certificates
- Composer-based build

### Platform.sh

Platform.sh is a unified, secure, enterprise-grade platform for building, running and scaling web applications. We’re the leader in Fleet Ops: Everything you need to manage your fleet of websites and apps is available from the start. Because infrastructure and workflows are handled from the start, apps just work, so teams can focus on what really matters: making faster changes, collaborating confidently, and scaling responsibly. Whether managing a fleet of ten or ten thousand sites and apps, Platform.sh is the Developer- preferred solution that scales right.

Our key features include:

<details>
<summary><strong>GitOps: Git as the source of truth</strong></summary><br />

Every branch becomes a development environment, and nothing can change without a commit. 

</details>

<details>
<summary><strong>Batteries included: Managed infrastructure</strong></summary><br />

[Simple abstraction in YAML](https://docs.platform.sh/configuration/yaml.html) for [committing and configuring infrastructure](https://docs.platform.sh/overview/structure.html), fully managed patch updates, and 24 [runtimes](https://docs.platform.sh/languages.html) & [services](https://docs.platform.sh/configuration/services.html) that can be added with a single line of code.

</details>

<details>
<summary><strong>Instant cloning: Branch, merge, repeat</strong></summary><br />

[Reusable builds](https://docs.platform.sh/overview/build-deploy.html) and automatically inherited production data provide true staging environments - experiment in isolation, test, then destroy or merge.  

</details>

<details>
<summary><strong>FleetOps: Fleet management platform</strong></summary><br />

Leverage our public API along with custom tools like [Source Operations](https://docs.platform.sh/configuration/app/source-operations.html) and [Activity Scripts](https://docs.platform.sh/integrations/activity.html) to [manage thousands of applications](https://youtu.be/MILHG9OqhmE) - their dependency updates, fresh content, and upstream code. 

</details>
<br/>

To find out more, check out the demo below and go to our [website](https://platform.sh/product/).

<br/>
<p align="center">
<a href="https://platform.sh/demo/"><img src="https://img.youtube.com/vi/ny2YeD6Qt3M/0.jpg" alt="The Platform.sh demo"></a>
</p>



## Getting started

### Deploy

#### Quickstart


The quickest way to deploy this template on Platform.sh is by clicking the button below. This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal9/.platform.template.yaml&utm_content=drupal9&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>

> **Note:**
>
> If you do not already have a Platform.sh account, you will be asked to fill out some basic information, after which you will be given a 30-day free trial to experiment with our platform.


#### Other deployment options

<details>
<summary>Deploy directly to Platform.sh from the command line</summary><br />

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/drupal9
   ```

1. Create a free trial:

   [Register for a 30 day free trial with Platform.sh](https://auth.api.platform.sh/register). When you have completed signup, select the **Create from scratch** project option. Give you project a name, and select a region where you would like it to be deployed. As for the *Production environment* option, make sure to match it to this repository's settings, or to what you have updated the default branch to locally.

1. Install the Platform.sh CLI

   #### Linux/OSX

   ```bash
   curl -sS https://platform.sh/cli/installer | php
   ```

   #### Windows

   ```bash
   curl -f https://platform.sh/cli/installer -o cli-installer.php
   php cli-installer.php
   ```

   You can verify the installation by logging in (`platformsh login`) and listing your projects (`platform project:list`).

1. Set the project remote

   Find your `PROJECT_ID` by running the command `platform project:list` 

   ```bash
   +---------------+------------------------------------+------------------+---------------------------------+
   | ID            | Title                              | Region           | Organization                    |
   +---------------+------------------------------------+------------------+---------------------------------+
   | PROJECT_ID    | Your Project Name                  | xx-5.platform.sh | your-username                   |
   +---------------+------------------------------------+------------------+---------------------------------+
   ```

   Then from within your local copy, run the command `platform project:set-remote PROJECT_ID`.

1. Push

   ```bash
   git push platform DEFAULT_BRANCH
   ```


</details>

<details>
<summary>Deploy from GitHub</summary><br />

If you would instead to deploy this template from your own repository on GitHub, you can do so through the following steps.

> **Note:**
>
> You can find the full [GitHub integration documentation here](https://docs.platform.sh/integrations/source/github.html).

1. Clone this repository:

   Click the [Use this template](https://github.com/platformsh-templates/drupal9/generate) button at the top of this page to create a new repository in your namespace containing this demo. Then you can clone a copy of it locally with `git clone git@github.com:YOUR_NAMESPACE/drupal9.git`.

1. Create a free trial:

   [Register for a 30 day free trial with Platform.sh](https://auth.api.platform.sh/register). When you have completed signup, select the **Create from scratch** project option. Give you project a name, and select a region where you would like it to be deployed. As for the *Production environment* option, make sure to match it to whatever you have set at `https://YOUR_NAMESPACE/nextjs-drupal`.

1. Install the Platform.sh CLI

   #### Linux/OSX

   ```bash
   curl -sS https://platform.sh/cli/installer | php
   ```

   #### Windows

   ```bash
   curl -f https://platform.sh/cli/installer -o cli-installer.php
   php cli-installer.php
   ```

   You can verify the installation by logging in (`platformsh login`) and listing your projects (`platform project:list`).

1. Setup the integration:

   Consult the [GitHub integration documentation](https://docs.platform.sh/integrations/source/github.html#setup) to finish connecting your repository to a project on Platform.sh. You will need to create an Access token on GitHub to do so.


</details>

<details>
<summary>Deploy from GitLab</summary><br />

If you would instead to deploy this template from your own repository on GitLab, you can do so through the following steps.

> **Note:**
>
> You can find the full [GitLab integration documentation here](https://docs.platform.sh/integrations/source/gitlab.html).

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/drupal9
   ```

1. Create a free trial:

   [Register for a 30 day free trial with Platform.sh](https://auth.api.platform.sh/register). When you have completed signup, select the **Create from scratch** project option. Give you project a name, and select a region where you would like it to be deployed. As for the *Production environment* option, make sure to match it to this repository's settings, or to what you have updated the default branch to locally.

1. Install the Platform.sh CLI

   #### Linux/OSX

   ```bash
   curl -sS https://platform.sh/cli/installer | php
   ```

   #### Windows

   ```bash
   curl -f https://platform.sh/cli/installer -o cli-installer.php
   php cli-installer.php
   ```

   You can verify the installation by logging in (`platformsh login`) and listing your projects (`platform project:list`).

1. Create the repository

   Create a new repository on GitLab, set it as a new remote for your local copy, and push to the default branch. 

1. Setup the integration:

   Consult the [GitLab integration documentation](https://docs.platform.sh/integrations/source/gitlab.html#setup) to finish connecting a repository to a project on Platform.sh. You will need to create an Access token on GitLab to do so.


</details>

<details>
<summary>Deploy from Bitbucket</summary><br />

If you would instead to deploy this template from your own repository on Bitbucket, you can do so through the following steps.

> **Note:**
>
> You can find the full [Bitbucket integration documentation here](https://docs.platform.sh/integrations/source/bitbucket.html).

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/drupal9
   ```

1. Create a free trial:

   [Register for a 30 day free trial with Platform.sh](https://auth.api.platform.sh/register). When you have completed signup, select the **Create from scratch** project option. Give you project a name, and select a region where you would like it to be deployed. As for the *Production environment* option, make sure to match it to this repository's settings, or to what you have updated the default branch to locally.

1. Install the Platform.sh CLI

   #### Linux/OSX

   ```bash
   curl -sS https://platform.sh/cli/installer | php
   ```

   #### Windows

   ```bash
   curl -f https://platform.sh/cli/installer -o cli-installer.php
   php cli-installer.php
   ```

   You can verify the installation by logging in (`platformsh login`) and listing your projects (`platform project:list`).

1. Create the repository

   Create a new repository on Bitbucket, set it as a new remote for your local copy, and push to the default branch. 

1. Setup the integration:

   Consult the [Bitbucket integration documentation](https://docs.platform.sh/integrations/source/bitbucket.html#setup) to finish connecting a repository to a project on Platform.sh. You will need to create an Access token on Bitbucket to do so.


</details>

## Post-install

Run through the Drupal installer as normal.  You will not be asked for database credentials as those are already provided.

### Local development

This section provides instructions for running the `drupal9` template locally, connected to a live database instance on an active Platform.sh environment.

In all cases for developing with Platform.sh, it's important to develop on an isolated environment - do not connect to data on your production environment when developing locally. Each of the options below assume the following starting point:

```bash
platform get PROJECT_ID
cd project-name
platform environment:branch updates
```

> **Note:**
>
> For many of the steps below, you may need to include the CLI flags `-p PROJECT_ID` and `-e ENVIRONMENT_ID` if you are not in the project directory or if the environment is associated with an existing pull request.

<details>
<summary><strong>Drupal: using ddev</strong></summary><br />

ddev provides an integration with Platform.sh that makes it simple to develop Drupal locally. Check the [providers documentation](https://ddev.readthedocs.io/en/latest/users/providers/platform/) for the most up-to-date information. 

In general, the steps are as follows:

1. A configuration file has already been provided at `.ddev/providers/platform.yaml`, so you should not need to run `ddev config`.
1. [Retrieve an API token](https://docs.platform.sh/development/cli/api-tokens.html#get-a-token) for your organization via the management console.
1. Update your dedev global configuration file to use the token you've just retrieved:
    
    ```yaml
    web_environment:
    - PLATFORMSH_CLI_TOKEN=abcdeyourtoken`
    ```

1. Run `ddev restart`.
1. Get your project ID with `platform project:info`. If you have not already connected your local repo with the project (as is the case with a source integration, by default), you can run `platform project:list` to locate the project ID, and `platform project:set-remote PROJECT_ID` to configure Platform.sh locally.
1. Update the `.ddev/providers/platform.yaml` file for your current setup:

    ```yaml
    environment_variables:
    project_id: PROJECT_ID
    environment: CURRENT_ENVIRONMENT
    application: drupal
    ```

1. Get the current environment's data with `ddev pull platform`. 
1. When you have finished with your work, run `ddev stop` and `ddev poweroff`.

</details><details>
<summary><strong>Drupal: using Lando</strong></summary><br />

Lando supports PHP applications configured to run on Platform.sh, and pulls from the same registry Platform.sh uses on your remote environments during your local builds through its own [recipe and plugin](https://docs.lando.dev/platformsh/). 

1. When you have finished with your work, run `lando stop` and `lando poweroff`.

</details>
<details>
<summary><strong>Next.js: building the frontend locally</strong></summary><br />

After you have created a new environment, you can connect to a backend Drupal instance and develop the frontend locally with the following steps.

1. `cd client`
1. Update the environment variables for the current environment by running `./get_local_config.sh`. This will pull the generated `.env.local` file for the current environment.

   ```bash
   # This .env file is generated programmatically within the backend Drupal app for each Platform.sh environment
   # and stored within an network storage mount so it can be used locally.

   NEXT_PUBLIC_DRUPAL_BASE_URL=https://api.ENVIRONMENT-HASH-PROJECTID.REGION.platformsh.site
   NEXT_IMAGE_DOMAIN=api.ENVIRONMENT-HASH-PROJECTID.REGION.platformsh.site
   DRUPAL_SITE_ID=nextjs_site
   DRUPAL_FRONT_PAGE=/node
   DRUPAL_CLIENT_ID=CONSUMER_CLIENT_ID
   DRUPAL_CLIENT_SECRET=GENERATED_SECRET
   ```

1. Install dependencies: `yarn --frozen-lockfile`.
1. Run the development server: `yarn dev`. Next.js will then run on http://localhost:3000.

</details>



## Customizations

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. Aliquam sed est egestas neque ultricies dictum a non dui. Maecenas placerat non tortor non porta. Curabitur iaculis nisi risus, vel sollicitudin diam cursus a. Proin in cursus ipsum, eget semper eros. Nulla in semper urna. Etiam lorem magna, pretium ac nibh eu, consequat facilisis odio. Aliquam auctor efficitur nisi sit amet sollicitudin. Morbi ut lacus metus. Nam lacinia eget enim eu molestie.

Ut nisi nulla, facilisis convallis tortor sed, ultricies accumsan magna. Fusce pretium velit id purus luctus luctus. In ac libero nunc. Integer mattis, ligula non ullamcorper sollicitudin, augue ex finibus elit, quis ornare tellus ex finibus tortor. Maecenas vel suscipit nunc, eget mollis turpis. Sed nunc nibh, rutrum ut diam quis, sagittis porta ex. Suspendisse potenti. Nulla faucibus justo ligula, eget vestibulum mauris sodales non. Donec commodo rhoncus elit ut malesuada. Aenean ac ex libero. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla luctus tempor justo, et rutrum purus ullamcorper et.


## Migration

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. Aliquam sed est egestas neque ultricies dictum a non dui. Maecenas placerat non tortor non porta. Curabitur iaculis nisi risus, vel sollicitudin diam cursus a. Proin in cursus ipsum, eget semper eros. Nulla in semper urna. Etiam lorem magna, pretium ac nibh eu, consequat facilisis odio. Aliquam auctor efficitur nisi sit amet sollicitudin. Morbi ut lacus metus. Nam lacinia eget enim eu molestie.

Ut nisi nulla, facilisis convallis tortor sed, ultricies accumsan magna. Fusce pretium velit id purus luctus luctus. In ac libero nunc. Integer mattis, ligula non ullamcorper sollicitudin, augue ex finibus elit, quis ornare tellus ex finibus tortor. Maecenas vel suscipit nunc, eget mollis turpis. Sed nunc nibh, rutrum ut diam quis, sagittis porta ex. Suspendisse potenti. Nulla faucibus justo ligula, eget vestibulum mauris sodales non. Donec commodo rhoncus elit ut malesuada. Aenean ac ex libero. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla luctus tempor justo, et rutrum purus ullamcorper et.

## Contact

This template is maintained by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channels and ping the `@devrel_team` with any questions.


## Resources

- [Next.js Drupal website](https://next-drupal.org/)
- [Quickstart documentation](https://next-drupal.org/learn/quick-start)
- [Documentation](https://next-drupal.org/docs)
- [Drupal 9 on Platform.sh](https://docs.platform.sh/guides/drupal9/deploy.html)
- [Platform.sh PHP documentation](https://docs.platform.sh/languages/php.html)
- [Platform.sh Node.js documentation](https://docs.platform.sh/languages/nodejs.html)
- [Platform.sh multi-app deployments documentation](https://docs.platform.sh/configuration/app/multi-app.html)




## Contributing

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<h4 align="center"><strong>How to contribute</strong></h4>
<br />
<p align="center">
    <a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Report a bug</strong></a><br />
    <a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Submit a feature request</strong></a><br />
    <a href="https://github.com/platformsh-templates/drupal9/pulls"><strong>Open a pull request</strong></a><br />
</p>
<br />
<h4 align="center"><strong>Need help?</strong></h4>
<br />
<p align="center">
    <a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a><br />
    <a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a><br />
</p>
<br /><br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>

<br/>

![GitHub Contributors Image](https://contrib.rocks/image?repo=platformsh-templates/drupal9)

<br />
