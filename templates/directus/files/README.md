<br />
<!-- Platform.sh logo left -->
<p align="left">
    <a href="https://platform.sh">
        <img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
    </a>
</p>
<br /><br />
<!-- Template logo -->
<p align="center">
    <a href="https://github.com/directus/directus">
        <img src="https://raw.githubusercontent.com/directus/directus/main/app/src/assets/logo-dark.svg" alt="Logo" width="300">
    </a>
</p>
<!-- Template title -->
<br/>
<h2 align="center">Deploying Directus on Platform.sh</h2>
<!-- Template info -->
<br/>
<!-- CTAs -->
<p align="center">
    <strong><em>Contribute to the Platform.sh knowledge base, or check out our resources</em></strong>
</p>
<p align="center">
    <a href="#about-platformsh"><strong>About Platform.sh</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Request a feature</strong></a>
</p>
<!-- Badges -->
<p align="center">
    <!-- <a href="https://github.com/platformsh-templates/directus/network/members">
        <img src="https://img.shields.io/github/workflow/status/platformsh/config-reader-python/Quality%20Assurance/master.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Build" alt="Tests" />
    </a>&nbsp&nbsp -->
    <a href="https://github.com/platformsh-templates/directus/issues">
        <img src="https://img.shields.io/github/issues/platformsh-templates/directus.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/pulls">
        <img src="https://img.shields.io/github/issues-pr/platformsh-templates/directus.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
    </a>&nbsp&nbsp
    <a href="https://github.com/directus/directus/blob/main/license">
        <img src="https://img.shields.io/static/v1?label=License&message=GNU%20Public&style=flat-square&labelColor=f4f2f3&color=ffd9d9" alt="License" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9" alt="Conduct" />
    </a>
    <!-- <br /> -->
    <!-- <a href="https://github.com/platformsh-templates/metabase/network/members">
  <img src="https://img.shields.io/github/license/metabase/metabase.svg?style=for-the-badge&labelColor=145CC6&color=FFBDBB" alt="Deploy on Platform.sh"/>
  </a> -->
    <!-- <a href="https://github.com/platformsh-templates/metabase/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/platformsh-templates/metabase.svg?style=for-the-badge&labelColor=145CC6&color=FFBDBB" alt="Deploy on Platform.sh" />
    </a> -->
    <!-- <a href="https://github.com/platformsh-templates/metabase/network/members">
        <img src="https://img.shields.io/github/forks/platformsh-templates/metabase.svg?style=for-the-badge&labelColor=145CC6&color=FFBDBB" alt="Deploy on Platform.sh" />
    </a>
    <a href="https://github.com/platformsh-templates/metabase/stargazers">
        <img src="https://img.shields.io/github/stars/platformsh-templates/metabase.svg?style=for-the-badge&labelColor=145CC6&color=FFBDBB" alt="Deploy on Platform.sh" />
    </a> -->
</p>
<p align="center">
    <strong><em>If you're unfamiliar with Platform.sh, be sure to checkout the <a href="#about-platformsh">About</a> section below.</em></strong>
</p>
<!-- Deploy on Platform.sh button -->
<br />
<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/metabase/.platform.template.yaml&utm_content=metabase&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="175px" />
    </a>
</p>
<br/><br/>

This template demonstrates building Directus for Platform.sh. It includes a quickstart application configured to run with PostgreSQL. It is intended for you to use as a starting point and modify for your own needs.

Directus is an open-source platform that allows you to create and manage an API from data stored in a database.

### Features

* Node.js 12
* PostgreSQL 12
* Redis 6.0
* Automatic TLS certificates
* npm-based build

### Contents

- [Getting started](#-getting-started-)
- [Customizations](#customizations)
- [Usage](#usage)
- [Migrating](#migrating)
- [License](#license)
- [About Platform.sh](#about-platformsh)
- [Contact](#contact)
- [Resources](#resources)
- [Contributors](#contributors)

<br/><hr><br/>

# Getting started

If you are unfamiliar with Directus, with Platform.sh, or otherwise want to quickly deploy this template, **Start here**. This template contains all of the files needed to deploy on Platform.sh, but you have a few options for doing so. Whichever method you choose, be sure to make note of all of the information included in this README, as it will be a great deal of help once your project has been deployed.

## Deploying

Everything needs to deploy and develop a Directus application on Platform.sh is included in this project. Whether you choose to develop using a Platform.sh project as your primary remote, or work on an integrated repository here on GitHub is up to you.

### Quickstart

The quickest method to deploy Directus on Platform.sh is by clicking the **Deploy on Platform.sh** button at the top of the page. This will automatically create a new project and initialize the repository for you. If you do not already have a Platform.sh account, you will be asked to fill out some basic information, after which you will be given a 30-day free trial to experiment with our platform.

<details>
<summary><strong>Start working with the project</strong></summary><br />

After you have deployed to a project, you can begin developing using Platform.sh as your primary remote repository. To clone the project, you have two options.

- Within the management console, go to the production environment for your default branch. At the top right-hand side under your avatar and account details there will be a dropdown element labelled **GIT**. Copy and run the command locally to retrieve your repository. 
- [Install the Platform.sh CLI](https://docs.platform.sh/development/cli.html#installation). With this tool you can quickly authenticate with Platform.sh (with the command `platform login`), and view your available projects (with the command `platform projects:list`). When you see your project, you will notice that it has a unique `PROJECT_ID`. With that hash, you can quickly clone a local copy with the command `platform get PROJECT_ID`.

In both cases, you will now be able to branch and push commits to Platform.sh. When you push a new branch to Platform.sh, it will remain in an *inactive* state by default initially. [Install the Platform.sh CLI](https://docs.platform.sh/development/cli.html#installation) if you have not already done so, and then run the command `platform environment:activate BRANCH_NAME` to begin the build and deploy phases in a new isolated environment. You are also able to activate this environment within the management console, by visiting the **Settings** pane for the environment and editing the **Status is Inactive** dropdown section.

</details>
<br />

### Starting from an integration to a GitHub repository

You also have the option of setting up a copy of this repository in your own namespace, and the integrating a Platform.sh to it as the continuous delivery component of its pipeline. 

<details>
<summary><strong>Setting up the integration</strong></summary><br />

1. [Generate a copy of this template](https://github.com/platformsh-templates/generate), or click the **Use this template** button at the top of this repository, to create a fresh copy of this codebase in your own namespace. 
2. [Start your 30 day free trial on Platform.sh](https://auth.api.platform.sh/register?trial_type=general). 
3. Create a new project on Platform.sh. After you create your account, you'll be able to create a new project. Select the **Create from scratch** option, give the project a name, like `directus`, and select a region where the application will live.
4. Save your `PROJECT_ID`. Every project on Platform.sh comes with a unique project ID that you will need to set up your integration to GitHub, and you can find this value in two places:
    - At the project URL in the management console. Your project will have a unique location at `https://console.platform.sh/<USERNAME>/<PROJECT-ID>`.
    - At the top right-hand corner, below your avator and account settings, click the three dot menu. The first option in the dropdown is the `ID`, which you can quickly copy from there.
5. [Generate a personal access token on your GitHub account](https://github.com/settings/tokens/new). Consult our integrations documentation to ensure that the token has been granted the [required scopes](https://docs.platform.sh/integrations/source/github.html#1-generate-a-token).
6. [Install the Platform.sh CLI](https://docs.platform.sh/development/cli.html#installation). With this tool you will also be able to retrieve your project's ID using the command `platform project:list`. 
7. Authenticate the CLI. You can do this quickly with the command `platform login`, which will use your current browser session to generate a local SSH key.
8. [Enable the integration](https://docs.platform.sh/integrations/source/github.html#2-enable-the-integration). Using the CLI, as well as the `PROJECT_ID` on Platform.sh, your `GITHUB_TOKEN`, and your repository, run the following command:

    ```bash
    platform integration:add --type=github --project=PROJECT_ID --token=GITHUB_TOKEN --repository=GITHUB_USER/GITHUB_REPOSITORY
    ```

</details>

<details>
<summary><strong>Developing on GitHub</strong></summary><br />

Once you have run the above command, Platform.sh will validate and then mirror your repository on the project you just created. It will then build and deploy the template for you. From this point forward, you can continue to develop your application on GitHub. 

With the default settings, your default branch will be your production environment, while every pull request opened on the repository will become active development environments on Platform.sh.

</details>
<br />

## Post-install instructions

This template does not require any additional configuration once deployed to start developing your Directus application. During the first deploy, however, an admin user has been added to allow you to log in. Those credentials are set (along with many other Platform.sh-specific settings) in the `.environment` file:

```txt
# Initial admin user on first deploy.
export INIT_ADMINUSER='admin@example.com'
export INIT_ADMINPW='password'
```

After you log in for the first time, be sure to update this password immediately. 

# Customizations

The following files and additions allow Directus to build and deploy on Platform.sh, placed on top of the basic quickstart project (`npx create-directus-project`). If using this project as a reference for your own existing project, replicate the changes below to your code. 

## Changes to the codebase

- **`.gitignore`**: A `.gitignore` file has been added to the Directus starter project, as it was not already included. It's contents prevent you from committing sensitive information in your `.env` file and SQLite database, as well as your dependencies.

## Platform.sh configuration

Platform.sh is able to build and deploy projects by detecting configuration in a few files, which have been added to the starter repository. View the comments in the individual files, as well as the linked documentation below, for more details.

- **`.platform/routes.yaml`**: This file defines how requests are handled by a [Router container](https://docs.platform.sh/configuration/routes.html).
- **`.platform/services.yaml`**: This file defines which of Platform.sh's [managed service containers](https://docs.platform.sh/configuration/services.html) are included alongside the template. 
- **`.platform.app.yaml`**: This file defines how Directus is built and deployed within a single [application container](https://docs.platform.sh/configuration/app.html).
- **`.environment`**: This file provides Platform.sh-specific environment variable overrides from the generated default `.env` settings for Directus and PostgreSQL. It also sets an initial username and password for an admin user. On Platform.sh, a `.env` file is required to configure Directus but is not committed (see below) in this project. Rather, at build time Directus's `example.env` file (`node_modules/directus/example.env`) is renamed in its place with a set of standard defaults which are then overridden by `.environment`. Consult this file locally, and then override with your own settings in `.environment` when appropriate. 

## Community and issues

A `.github` subdirectory for handling issue templates, as well as our `CODE_OF_CONDUCT` and `CONTRIBUTING` guides have been added.
 
# Usage

Once you have deployed this template, there are a number of next steps you can take to interact with and customize the project.

## Logs

Once you have deployed to an active environment, you will be able to SSH into your application containers, which can be useful for many things including accessing logs. A temporary SSH token will be generated for you (once you have logged in through the browser) by running the command `platform login`. After that from your project's root, simply run the command

```bash
platform ssh
```

to gain access. Everything in your repository plus any artifacts of your build will exist here in `/app`. All logs are available in the subdirectory `/var/log`, and you can find more information about the available logs [in the Development documentation](https://docs.platform.sh/development/logs.html).

You can also view application logs directly using the Platform.sh CLI command `platform logs app`.

<!-- <details>
<summary><strong>Log forwarding</strong></summary><br />

<em>Coming soon!</em>

</details> -->

### Local development

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum.

<details>
<summary><strong>Lando:</strong> <em>Use the Platform.sh recommended local development tool</em></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<details>
<summary><strong>Docksal:</strong> <em>Docker-based local development</em></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<details>
<summary><strong>DDEV:</strong> <em>PHP local development</em></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<details>
<summary><strong>Tethered:</strong> <em>Connect directly to your Platform.sh services over an SSH tunnel</em></summary><br />

You are able to test out or build this template on your local machine by following the steps below:

#### Requirements

- [Platform.sh CLI](https://docs.platform.sh/development/cli.html)
- These steps open a tunnel to a PostgreSQL container on Platform.sh, so it is assumed that you have pushed to Platform.sh or clicked the **Deploy on Platform.sh** button above, and have followed the [post-install instructions](#post-install).

#### Steps

You are able to run the `build.sh` and `start.sh` `scripts` just as they're defined in `.platform.app.yaml` to run Metabase locally.

Download the project's current live committed version of Metabase (defined in the [`metabase.version`](metabase.version) file):

```bash
./scripts/build.sh
```

Then start the application for the downloaded jar file:

```bash
./scripts/start.sh
```

The script will automatically open a tunnel to the PostgreSQL instance on the current environment, so be sure to create a new one before making any changes.

</details>

<details>
<summary><strong>Untethered:</strong> <em>Using local services</em></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

### Updating

This template downloads the Metabase jar file during the build hook using the `build.sh` script. The version downloaded is dependendent on the version listed in the [`metabase.version`](metabase.version) file in the repository.

```bash
./scripts/update.sh
```

An `update.sh` script has been included in this repository, which checks to see if a [new version of Metabase is available](<(https://github.com/metabase/metabase/releases)>), and if so updates the contents of `metabase.version` that will used on subsequent builds.

<details>
<summary><strong>Scheduling automatic updates:</strong> <em>automating upstream updates with source operations</em></summary><br />

> **Note:**
>
> This section describes features only available to Elite and Enterprise customers. [Compare the Platform.sh tiers](https://platform.sh/pricing/#compare) on our pricing page, or [contact our sales team](https://platform.sh/pricing/#compare) for more information.

It is possible to schedule the updates described above using [source operations](https://docs.platform.sh/configuration/app/source-operations.html), which are a set of commands that can be triggered to make changes to your project's code base.

A source operation has been defined for this template that is scheduled to run regularly with a cron job:

```yaml
source:
  operations:
    update:
      command: !include
        type: string
        path: scripts/update.sh
```

The [`update.sh` script](scripts/update.sh) - when a new version of Metabase has been released - will write the latest version to `metabase.version`. That change will be staged and committed in an isolated build container source operations run on, ultimately causing a full rebuild of the environment (but not using that latest version).

This command can be triggered at any time for any environment with the CLI command:

```bash
platform source-operation:run update
```

Ideally we would like:

1. For this update to occur automatically.
2. To only occur in an isolated environment, rather than to production.

The [cron job](https://docs.platform.sh/configuration/app/cron.html) defined in [`.platform.app.yaml`](.platform.app.yaml) does exactly this:

```yaml
crons:
  auto-updates:
    spec: '0 1 * * *'
    cmd: |
      if [ "$PLATFORM_BRANCH" = updates ]; then
          platform environment:sync code data --no-wait --yes
          platform source-operation:run update --no-wait --yes
      fi
```

With this definition, the `update` source operation will check to see if a new version of Metabase is available every day at 1:00 am UTC, but _only_ on the `updates` environment. If that environment does not exist on your project it will never run.

<hr></details>

<br />
<h1>Migrating </h1>

#### Data

Moving from using Metabase Cloud to a Self hosted version means you also would need to migrate your data yourself. For the migration to happen, you'll need to obtain your database dump from metabase, you can do that by refering to this [guide](https://www.metabase.com/docs/latest/operations-guide/migrating-from-h2.html) in the Metabase documentation.

> **Note:**
>
> It is advised you backup your database before proceeding with the dump.

When you have successfully obtained a dump of your data (MySQL, MariaDB or PostgreSQL) from Metabase, you'll need to populate the postgresql database service that this template uses. You can change the default database type of this template by altering the `.platform/services.yaml` file in the `.platform` folder if needed.

Next, you'll need to save your as `database.sql`. (Or any name, really, as long as it’s the same as you use below.)

Next, import the database into your Platform.sh site. The easiest way to do so is with the Platform.sh CLI by running the following command:

```bash
platform sql -e master < database.sql
```

The above command will connect to the database service on the `master` environment, through an SSH tunnel, and run the SQL import.

#### Adding data sources

If you need to add your previous data sources, all you need to do is to build and deploy your metabase site, visit the generated route to see the metabase site live.

Next thing is to follow this [guide](https://www.metabase.com/docs/latest/administration-guide/01-managing-databases.html) in the Metabase official documentation to learn how to add various data sources.

> **Note:**
>
> If you have a CSV file containing your data you'll need to upload the csv files to a database, then connect Metabase to the database.

### Customizing Metabase

<details>
<summary>Adding a datasource</summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<details>
<summary>Adding a domain</summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<details>
<summary>Authentication</summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel.

</details>

<!-- ## Roadmap

This template will be actively updated and maintained. Moving forward we would be improving this template with more features like:

- [ ]
- [ ]
- [ ]
- [ ]

## Contributing

Before sending a PR, please see the [Contributing Guide](/CONTRIBUTING.md)

<!-- ### Code of Conduct

WIP

### Community License Agreement

WIP -->


# License

This template uses the [Open Source edition of Directus](https://github.com/directus/directus), which is licensed under the [GNU General Public License v3.0](https://github.com/directus/directus/blob/main/license).

## About Platform.sh

Platform.sh is a Platform-as-a-Service (PaaS) provider, and a DevOps platform for deploying and managing your web applications. It attempts to simplify DevOps according to a level of abstraction that keeps your applcations secure, your development unblocked, and your time focused on your sites rather than on operations and infrastructure. 

Some of the key features of Platform.sh include:

<details>
<summary><strong>Infrastructure-as-code:</strong> <em>Your infrastructure is a dependency of your app</em></summary><br />
All of your services can be defined in a set configuration files described above and committed to your repository. These files are committed, such that your infrastructure becomes another dependency of your application like any other, and so that every branch is capable of inheriting the identical infrastructure used in production.

</details>
<details>
<summary><strong>Development environments:</strong> <em>Every pull request should get a real staging environment</em></summary><br />

Every project has a live production site, but the concept of branching your repository has been extended to the provisioning of staging and development infrastructure. Every branch can become an active, deployed environment, that contains the same infrastructure as production until you explicitly change its configuration. 

Each environment receives its own unique preview URL, automatically renewed Let's Encrypt certificates, as well as scoped access permissions and environment variables. Environments exist in isolation from production: they are exact copies with fresh containers that cannot affect the production site. During the branching process, a development environment also receives copies of all production data at the time of the branching. You are free to use that data for your tests, and can resync to more current data at any time. 

</details>
<details>
<summary><strong>Reusable builds:</strong> <em>Provision the infrastructure diff, Deploy on Friday</em></summary><br />

The build and deploy tasks defined in your configuration are committed, and Platform.sh is capable to define infrastructure provisioning requirements for a particular commit to the same differences that define the Git protocol. That is to say, a single commit is associated with a unique build image. If the build and deploy stages of your pipeline remain undefined between commits, that unique build image is reused on that second commit. 

This makes branching to a new development environment on Platform.sh possible, and also virtually removed any concern associated with merging a particular commit into production. When the merge is initiated, it isn't necessary to run through the build and deploy again and risk failure. The build image has already been created and defined on an identical development environment, so it can simply be reused on production from then on.

</details>
<details>
<summary><strong>Managed infrastructure:</strong> <em>Focus on your application, not operations, infrastructure, or patch updates</em></summary><br />
Every service and runtime container can be specified at the minor version level by an appropriate and supported `type` attribute, while security and patch updates are applied automatically in the background by Platform.sh between deployments when they become available.
</details>
<details>
<summary><strong>FleetOps:</strong> <em>Extend Platform.sh-powered DevOps to hundreds of applications</em></summary><br />
The Platform.sh API extends past single projects. It is possible to define your own upstream template repositories that are used to initialize a Fleet of of websites. There are also definable operations and activity notification scripts that can be used to fully manage hundreds of applications under the same logic and assurances of a single project. 
</details>

You can see Platform.sh in action in the brief demo below.

https://user-images.githubusercontent.com/5473659/137526518-65bcfa5b-7858-4fd0-ae17-74c5734c8157.mp4

For more information, check out our [website](https://platform.sh) and [public documentation](https://docs.platform.sh).

# Contact

This template is maintained primarily by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channel and ping the `@devrel_team` with any questions.
<!-- - **E-mail:** You can also reach the DevRel team directly at `devrel@platform.sh`. -->

# Resources

<!-- ### General -->

- [Directus](https://directus.io/)
- [Directus documentation](https://docs.directus.io/getting-started/introduction/)
- [Directus repository](https://github.com/directus/directus)
- [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)

<!-- ### Blog posts

- Any related blog posts

### Community

- Community questions -->

# Contributing

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or to better understand how to best run software on our platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<h3 align="center"><strong>How to contribute</strong></h3>
<p align="center">
    <a href="/CONTRIBUTING.md"><strong>Read the Contributing Guidelines</strong></a><br />
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Report a bug</strong></a><br />
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Submit a feature request</strong></a><br />
    <a href="https://github.com/platformsh-templates/directus/compare"><strong>Open a pull request</strong></a><br />
</p>

<h3 align="center"><strong>Need help?</strong></h3>
<p align="center">
    <a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a><br />
    <a href="https://chat.platform.sh/"><strong>Join us on Slack</strong></a><br />
</p>
<br /><br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>

<br/>

![GitHub Contributors Image](https://contrib.rocks/image?repo=platformsh-templates/directus)
