
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
<br/>


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

### Post-install

Run through the Drupal installer as normal.  You will not be asked for database credentials as those are already provided.

### Local development

This section provides instructions for running the `drupal9` template locally, connected to a live database instance on an active Platform.sh environment.

In all cases for developing with Platform.sh, it's important to develop on an isolated environment - do not connect to data on your production environment when developing locally. Each of the options below assume the following starting point:

```bash
platform get PROJECT_ID
cd project-name
platform environment:branch updates
```

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


> **Note:**
>
> For many of the steps above, you may need to include the CLI flags `-p PROJECT_ID` and `-e ENVIRONMENT_ID` if you are not in the project directory or if the environment is associated with an existing pull request.


## Migration

The steps below outline the important steps for migrating your application to Platform.sh - adding the required configuration files and dependencies, for example.
Not every step will be applicable to each person's migration.
These steps actually assume the earliest starting point possible - that there is no code at all locally, and that this template repository will be rebuilt completely from scratch.

- [Getting started](#getting-started-1)
- [Adding and updating files](#adding-and-updating-files)
- [Dependencies](#dependencies)
- [Deploying to Platform.sh](#deploying-to-platformsh)
- [Migrating your data](#migrating-your-data)
- [Next steps](#next-steps)

If you already have code you'd like to migrate, feel free to focus on the steps most relevant to your application and skip the first section.

### Getting started



If you are coming to this README with no local application to start with, begin with this section. Otherwise, move on to [Adding and updating files](#adding-and-updating-files) below.



### Adding and updating files

A small number of files need to be added to or modified in your repository at this point. 
Some of them explicitly configure how the application is built and deployed on Platform.sh, while others simply modify files you may already have locally, in which case you will need to replicate those changes.



|  File | Purpose    |
|:-----------|:--------|
| [`config/sync/.gitkeep`](config/sync/.gitkeep) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`web/sites/default/settings.php`](web/sites/default/settings.php) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`web/sites/default/settings.platformsh.php`](web/sites/default/settings.platformsh.php) | Contains Platform.sh-specific configuration, namely setting up the database connection to the MariaDB service and caching via Redis. |
| [`.environment`](.environment) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`.gitignore`](.gitignore) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`.lando.upstream.yml`](.lando.upstream.yml) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`.platform.app.yaml`](.platform.app.yaml) | This file is required to define the build and deploy process for all application containers on Platform.sh. Within this file, the runtime version, relationships to service containers, and writable mounts are configured. Take a look at the [Application](https://docs.platform.sh/configuration/app.html) documentation for more details about configuration. Here's a second custom line about the app itself after the shared generic file. |
| [`drush/platformsh_generate_drush_yml.php`](drush/platformsh_generate_drush_yml.php) | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor. |
| [`.platform/services.yaml`](.platform/services.yaml) |    |
| [`.platform/routes.yaml`](.platform/routes.yaml) |    |



### Dependencies


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec molestie mauris ut magna laoreet tempor.



### Deploying to Platform.sh

Your repository now has all of the code it needs in order to deploy to Platform.sh. 
In order to actually deploy, consult the [Getting started](#getting-started) section of this document, which contains all of the information to either push directly to Platform.sh or to integrate with an external service like GitHub.
When you've finished, come back to this section to learn how to [Migrate your data](#migrating-your-data).



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



### Migrating your data


If you are moving an existing site to Platform.sh, then in addition to code you also need to migrate your data. That means your database and your files.

1. **Importing the database**

    First, obtain a database dump from your current site and save your dump file as `database.sql`. Then, import the database into your Platform.sh site using the CLI:

    ```bash
    platform sql -e main < database.sql
    ```

2. **Importing files**

    You first need to download your files from your current hosting environment. 
    The easiest way is likely with rsync, but consult your old host's documentation. 

    The `platform mount:upload` command provides a straightforward way to upload an entire directory to your site at once. 
    Under the hood, it uses an SSH tunnel and rsync, so it is as efficient as possible. 
    (There is also a `platform mount:download` command you can use to download files later.) 
    Run the following from your local Git repository root (modifying the `--source` path if needed and setting `BRANCH_NAME` to the branch you are using).

    ```bash
    something
    ```

    Note that `rsync` is picky about its trailing slashes, so be sure to include those.



### Next steps

With your application now deployed on Platform.sh, things get more interesting. 
Run the command `platform environment:branch new-feature` for your project, or open a trivial pull request off of your current branch. 

The resulting environment is an *exact* copy of production.
It contains identical infrastructure to what's been defined in your configuration files, and even includes data copied from your production environment in its services. 
On this isolated environment, you're free to make any changes to your application you need to, and really test how they will behave on production. 

After that, here are a collection of additional resources you might find interesting as you continue with your migration to Platform.sh:

- [Local development](#local-development)
- [Troubleshooting](#troubleshooting)
- [Adding a domain and going live](https://docs.platform.sh/domains/steps.html)
- [(CDN) Content Delivery Networks](https://docs.platform.sh/domains/cdn.html)
- [Performance and observability with Blackfire.io](https://docs.platform.sh/integrations/observability/blackfire.html)
- [Pricing](https://docs.platform.sh/overview/pricing.html)
- [Security and compliance](https://docs.platform.sh/security.html)

## Contact

This template is maintained by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channels and ping the `@devrel_team` with any questions.


## Resources

- [Drupal](https://www.drupal.org/)
- [Drupal 9 on Platform.sh](https://docs.platform.sh/guides/drupal9/deploy.html)
- [Platform.sh PHP documentation](https://docs.platform.sh/languages/php.html)




## Contributing

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<p align="center">
<strong>How to contribute</strong>
<br /><br />
<a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9/issues"><strong>Submit a feature request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9/pulls"><strong>Open a pull request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<p align="center">
<strong>Need help?</strong>
<br /><br />
<a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>
<br/>
<p align="center">
<a href="https://github.com/platformsh-templates/drupal9/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=platformsh-templates/drupal9" />
</a>
</p>

<p align="center">
<em>Made with <a href="https://contrib.rocks">contrib.rocks</a><em>
</p>

<br />
<p align="center">
<img src="https://platform.sh/images/linked-block/people.svg" width="100%">
</p>
