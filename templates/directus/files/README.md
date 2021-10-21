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

<!-- Main README -->

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

**Contents:**

- [Deploying: Quickstart](#quickstart)
- [Deploying: Starting from an integration to a GitHub repository](#starting-from-an-integration-to-a-github-repository)
- [Post-install instructions](#post-install-instructions)

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

This template does not require any additional configuration once deployed to start developing your Directus application. During the first deploy, however, an admin user has been added to allow you to log in. Those credentials are set during the deploy hook in the `.platform.app.yaml` file:

```yaml
hooks:
    deploy: |
        set -e
        # Installs the database and sets up the initial admin user. Only run on first deploy.
        if [ ! -f var/platformsh.installed ]; then
            echo 'Bootstrapping Directus on first deploy...'

            export PROJECT_NAME='Directus on Platform.sh'
            export ADMIN_EMAIL='admin@example.com'
            export ADMIN_PASSWORD='password'
            
            npx directus bootstrap

            # Create file that indicates first deploy and installation has been completed.
            touch var/platformsh.installed
        fi;
```

After you log in for the first time, be sure to update this password immediately. 

# Customizations

The following files and additions allow Directus to build and deploy on Platform.sh, placed on top of the basic quickstart project (`npm init directus project`). If using this project as a reference for your own existing project, replicate the changes below to your code. 

**Contents:**

- [Changes to the codebase](#changes-to-the-codebase)
- [Platform.sh configuration](#platformsh-configuration)

## Changes to the codebase

- **`.gitignore`**: A `.gitignore` file has been added to the Directus starter project, as it was not already included. It's contents prevent you from committing sensitive information in your `.env` file and SQLite database, as well as your dependencies.
- **`package.json`**: The `argon2-rebuild` script has been added, [as recommended by Directus](https://docs.directus.io/guides/installation/plesk/#bootstrap-directus), so that the database can be initialized during `directus bootstrap`.
- **`.env.example`**: The `npm init directus-project` script generates a `.env` based on your answers to a set of prompts (for example, which database driver you want to use) that contains a set of environment variables for developing a Directus application. Platform.sh has added a `.gitignore` file to this repository which ignores `.env` from being committed, since this is generally considered bad practice and a path for unintentionally committed secrets. A fairly similar `.env.example` file _has_ been included however. It contains many of the same environment variables, including those settings that enable you to develop locally over a tethered connection to Platform.sh services. Please read the [**Tethered** local development](#local-development) instructions below for more details of how to use this file. 

## Platform.sh configuration

Platform.sh is able to build and deploy projects by detecting configuration in a few files, which have been added to the starter repository. View the comments in the individual files, as well as the linked documentation below, for more details.

- **`.platform/routes.yaml`**: This file defines how requests are handled by a [Router container](https://docs.platform.sh/configuration/routes.html).
- **`.platform/services.yaml`**: This file defines which of Platform.sh's [managed service containers](https://docs.platform.sh/configuration/services.html) are included alongside the template. 
- **`.platform.app.yaml`**: This file defines how Directus is built and deployed within a single [application container](https://docs.platform.sh/configuration/app.html).
- **`.environment`**: This file provides Platform.sh-specific environment variable overrides from the generated default `.env` settings for Directus and PostgreSQL. It also sets an initial username and password for an admin user. On Platform.sh, a `.env` file is required to configure Directus but is not committed (see below) in this project. Rather, at build time Directus's `example.env` file (`node_modules/directus/example.env`) is renamed in its place with a set of standard defaults which are then overridden by `.environment`. Consult this file locally, and then override with your own settings in `.environment` when appropriate. 
 
# Usage

Once you have deployed this template, there are a number of next steps you can take to interact with and customize the project.

**Contents:**

- [Setting up local development](#setting-up-local-development)
- [Updating](#updating)
- [Development](#development)
- [Logs](#logs)

## Setting up local development 

There are a few options for developing locally with Directus and Platform.sh.

<details>
<summary><strong>Tethered:</strong> <em>Connect directly to your Platform.sh services over an SSH tunnel</em></summary><br />

This template has been set up to help you develop Directus locally by opening a tunnel to services running on a live Platform.sh requirement. Because of this, there are a few requirements that need to first be met:

**Requirements:**

- [A deployed Directus template](#deploying)
- The [Platform.sh CLI](https://docs.platform.sh/development/cli.html) installed on your machine
- A local copy of this template repository
- npx installed locally

1. Create a development environment. 

    ```bash
    git checkout -b updates
    git push origin updates
    ```

    You can push to the project directly if you have not integrated with GitHub (`platform environment:activate updates`), or otherwise open a pull request for the branch you have just pushed to GitHub. 

2. Tunnel to services

    Once the environment has successfully deployed, you can use the CLI to [open a tunnel]() to start a _tethered_ local development environment to your services. To open the tunnel, run the command:

    ```bash
    platform tunnel:open
    ```

    which will provide the following output:

    ```bash
    SSH tunnel opened to database at: pgsql://main:main@127.0.0.1:30000/main
    SSH tunnel opened to redisratelimit at: redis://127.0.0.1:30001
    SSH tunnel opened to rediscache at: redis://127.0.0.1:30002

    List tunnels with: platform tunnels
    View tunnel details with: platform tunnel:info
    Close tunnels with: platform tunnel:close

    Save encoded tunnel details to the PLATFORM_RELATIONSHIPS variable using:
    export PLATFORM_RELATIONSHIPS="$(platform tunnel:info --encode)"
    ```

    > **Note**
    >
    > If working from an environment created from a pull request on GitHub, make sure to add an environment flag to the `tunnel:open` command (i.e. `platform tunnel:open -e pr-8`).

3. Mock environment variables

    In order to match the environment on Platform.sh, run the suggested command above to retrieve connection credentials for the services now tunneled locally.

    ```bash
    export PLATFORM_RELATIONSHIPS="$(platform tunnel:info --encode)"
    ```

    > **Note**
    >
    > If working from an environment created from a pull request on GitHub, make sure to add an environment flag to the `tunnel:info` command (i.e. `export PLATFORM_RELATIONSHIPS="$(platform tunnel:info -e pr-8 --encode)"`).

    A `.env.example` file has also been included in the repository based on the one provided from Directus. Use that file to create a local, uncommitted `.env` file:

    ```bash
    cp .env.example .env
    ```

4. Start Directus

    With your environment set up, install your dependencies (`npm install`) and then run the Directus server locally:

    ```bash
    npx directus start
    ```

</details>
<br />

There are also some additional things to keep in mind when developing locally, specifically related to how data works on Platform.sh.

<details>
<summary><strong>A Note on data:</strong> <em>Runtime write access and the Platform.sh data model</em></summary><br />

As you develop your Directus application, there are a few things to keep in mind that are specific to how Platform.sh handles data. Platform.sh abstracts much of the operations you would normally have to write and maintain yourself. Part of the assurance provided with the platform comes from treating infrastructure as code, and therefore as an equal part of the build image that identifies the state of your application for a particular commit. 

This is advantageous for a few reasons. First, it means that commits can be rolled back to a previous build image by running a simple `git revert` on your changes. Second, it means that should you make some change to your site that does not affect the build itself, a build slug can be reused when an environment is created (branching) or promoted (merging). Both of these remove any sort of apprehension that might come with merging into production or trying out a new feature quickly on a development environment. 

Code and data work differently in this model. They are separate entities, with different inheritance rules. Code can always be inherited by a child branch/environment. Data (i.e. in a production database, in a parent mounted directory) is also inherited - giving you a true staging environment for any change made to your application in a development environment. 

Merging changes things, however. Code can move upwards from a development environment to its parent, but data cannot. That means that any new endpoints created for Directus in a development environment _will not_ get merged to production unless a database dump is expliticly uploaded to production. Only changes to code (like custom `modules`) will make it to production. This makes up one half of our repeatable builds methodology. The other is that your application and its infrastructure generates a build image, and that that image only changes when the code changes. Part of ensuring this approach is followed for directus prevents write access to the file system post-build. If there are any changes you expect to be able to make to the file system at runtime, you will not be able to do so. It's recommended instead that you make and commit those changes in your local development environment, and then push them to an environment on Platform.sh.

</details>
<br />

## Updating 

This template is managed with npm, so updating to the latest version is as simple as

1. Creating a new environment to test the changes: 

    ```bash
    platform environment:branch update-directus
    ```

2. Retrieving updates with npm

    ```bash
    npm update
    ```

3. Testing those updates on Platform.sh

    ```bash
    git commit -am "Update Directus." && git push origin update-directus
    ```


<details>
<summary><strong>Scheduling automatic updates:</strong> <em>automating upstream updates with source operations</em></summary><br />

**Requirements:**

- [Platform.sh CLI installed in your application container](https://docs.platform.sh/development/cli/api-tokens.html#on-a-platformsh-environment) with a configured token environment variable

> **Note:**
>
> This section describes features only available to Elite and Enterprise customers. [Compare the Platform.sh tiers](https://platform.sh/pricing/#compare) on our pricing page, or [contact our sales team](https://platform.sh/pricing/#compare) for more information.

It is possible to schedule the updates described above using [source operations](https://docs.platform.sh/configuration/app/source-operations.html), which are a set of commands that can be triggered to make changes to your project's code base. For example, a very simple way to automate the updates described above might look like this in your `.platform.app.yaml` file:

```yaml
source:
    operations:
        update_dependencies:
            command: |
                npm update
                git commit -am "Update Directus."
```

Once the operation has been defined, you can trigger it to make the commit on a non-production environment with the CLI (`platform source-operation:run update_dependencies`), or by defining a cron job that runs it periodically:

```yaml
timezone: "Europe/Paris"
crons:
    update:
            spec: '0 3 * * *'
            cmd: |
                if [ "$PLATFORM_BRANCH" == "auto-updates" ]; then
                    platform environment:sync code data --no-wait --yes
                    platform source-operation:run update_dependencies
                fi 
```

With the above configuration, the operation will check for and apply updates on a dedicated `auto-updates` environment every day at 3am Paris time. 

This is, of course, not the only way to implement scheduled updates with source operations - it's a simple example, and you will notice a more complicated implementation of them in this template used by Platform.sh to keep it up-to-date. Another useful resource comes from [our community site](https://community.platform.sh/t/fully-automated-dependency-updates-with-source-operations/801), where we go into much greater detail about how scheduled dependency updates might work for you. 

</details>
<br />

## Developing

Once you have deployed Directus and prepared your local development environment, you are now ready to develop your application. Directus provides an excellent [getting started overview video](https://www.youtube.com/watch?v=AicEmIeuuLw) that you can use to begin setting up your site. 

<p align="center">
    <a href="https://youtu.be/AicEmIeuuLw" rel="noreferrer">
        <img src="https://img.youtube.com/vi/AicEmIeuuLw/hqdefault.jpg" alt="Watch the video">
    </a>
</p>

## Logs

Once you have deployed to an active environment, you will be able to SSH into your application containers, which can be useful for many things including accessing logs. A temporary SSH token will be generated for you (once you have logged in through the browser) by running the command `platform login`. After that from your project's root, simply run the command

```bash
platform ssh
```

to gain access. Everything in your repository plus any artifacts of your build will exist here in `/app`. All logs are available in the subdirectory `/var/log`, and you can find more information about the available logs [in the Development documentation](https://docs.platform.sh/development/logs.html).

You can also view application logs directly using the Platform.sh CLI command `platform logs app`.

# Migrating

If you are trying to migrate your existing Directus application to Platform.sh, there are a few things you will need to accomplish in order to do so:

<details>
<summary><strong>Using different services:</strong> <em>Platform.sh provides managed services so you can match your database</em></summary><br />

This template uses PostgreSQL as its primary database, but this is not the only database available for Directus. 

1. Update the driver

    Remove the current PostgreSQL driver library, and add the one you are currently using. For MariaDB as an example:

    ```bash
    npm uninstall pg && npm install mysql2/promise
    ```

2. Add the service

    Find your service in our [Services documentation](https://docs.platform.sh/configuration/services.html), as well as a supported version that matches the [minimum requirements](https://docs.directus.io/guides/installation/cli/#_1-confirm-minimum-requirements) outlined by Directus. Then you can replace that configuration in `services.yaml` where PostgreSQL is currently configured. An example for MariaDB has already been included in that file as an example commented out. 

3. Update the relationship

    An environment on Platform.sh describes a collection of containers. `.platform.app.yaml` describes how an application container should be built and deployed, while `.platform/services.yaml` describes which managed service containers should be included in the cluster. In order for them to communicate with each other, an application container must be given access through the definition of a `relationship`. Here is the current configuration of PostgreSQL:

    ```yaml
    # From .platform.app.yaml
    relationships:
        database: "db:postgresql"
    
    # From .platform/services.yaml
    db:
        type: postgresql:12
        disk: 256
    ```

    `db` is the name attributed to the PostgreSQL container, and it is used again in the relationship definition `database: "db:postgresql"`. When switching out another service, make sure to repeat the same pattern in this block. If you preserve the alias the application will use to query the database (i.e. `database`), you will not need to update any of the environment variable logic included in `.environment` when switching to another service. The endpoint `postgresql` will be specific to the database you choose to use, so be sure to revisit the [Services documentation](https://docs.platform.sh/configuration/services.html) to configure correctly. 

</details>

<details>
<summary><strong>Importing your database</strong></summary><br />

When you have successfully obtained a dump of your data for Directus, you'll need to populate the production database service that this template uses. You can change the default database type of this template by altering the `.platform/services.yaml` as described above first if needed.

Import the database into your Platform.sh environment. The easiest way to do so is with the Platform.sh CLI by running the following command:

```bash
platform sql -e main < database.sql
```

The above command will connect to the database service on the `main` environment, through an SSH tunnel, and run the SQL import. Make sure to update the command to match the names of your database dump and your default branch on Platform.sh.

</details>

<details>
<summary><strong>Importing your files</strong></summary><br />

You first need to download your files from your current hosting environment. The easiest way is likely with rsync, but consult your current host’s documentation. This sections assumes that you have already downloaded all of your user files to a local directory. The `platform mount:upload` command provides a straightforward way to upload an entire directory to your site at once. Under the hood, it uses an SSH tunnel and rsync, so it is as efficient as possible. 

> **Note:**
> 
> There is also a `platform mount:download` command you can use to download files later.

Run the following from your local Git repository root (modifying the `--source` path if needed and setting `<DEFAULT_BRANCH>` to the name of your projects default branch. Note that rsync is picky about its trailing slashes, so be sure to include those.

```bash
platform mount:upload -e <DEFAULT_BRANCH> --mount uploads --source ./backups/uploads
```

</details>

<br />

After following the above steps, your files and database are now loaded onto your Platform.sh production environment. When you make a new branch environment off of it, all of your data will be fully cloned to that new environment so you can test with your complete dataset without impacting production.

# License

This template uses the [Open Source edition of Directus](https://github.com/directus/directus), which is licensed under the [GNU General Public License v3.0](https://github.com/directus/directus/blob/main/license).

# Resources

- [Directus](https://directus.io/)
- [Directus documentation](https://docs.directus.io/getting-started/introduction/)
- [Directus repository](https://github.com/directus/directus)
- [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)

# About Platform.sh

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
