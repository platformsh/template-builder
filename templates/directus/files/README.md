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
        <img src="https://raw.githubusercontent.com/directus/directus/main/app/src/assets/logo-dark.svg" alt="Logo" height="120">
    </a>
</p>
<!-- Template title -->
<br/><br/>
<h2 align="center">Deploying Directus on Platform.sh</h2>
<!-- Template info -->
<br/>
<p align="center">
    <strong><em>Contribute to the Platform.sh knowledge base, or check out our resources</em></strong>
</p>
<p align="center">
    <a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/issues"><strong>Request a feature</strong></a>
</p>
<p align="center">
    <!-- <a href="https://github.com/platformsh-templates/directus/network/members">
        <img src="https://img.shields.io/github/workflow/status/platformsh/config-reader-python/Quality%20Assurance/master.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Build" alt="Tests" />
    </a>&nbsp&nbsp -->
    <a href="https://github.com/platformsh-templates/directus/issues">
        <img src="https://img.shields.io/github/issues/platformsh-templates/metabase.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/directus/pulls">
        <img src="https://img.shields.io/github/issues-pr/platformsh-templates/metabase.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
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
<!-- Deploy on Platform.sh button -->
<br />
<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/metabase/.platform.template.yaml&utm_content=metabase&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="200px" />
    </a>
</p>
<br/><br/>
<!-- <hr> -->
<!-- <br/><br/> -->

This template demonstrates building Directus for Platform.sh. It includes a quickstart application configured to run with PostgreSQL. It is intended for you to use as a starting point and modify for your own needs.

Directus is an open-source platform that allows you to create and manage an API from data stored in a database.

## Features

* Node.js 12
* PostgreSQL 12
* Redis 6.0
* Automatic TLS certificates
* npm-based build

## Contents

- [Getting started](#-getting-started-)
- [Customizations](#customizations)
- [About Platform.sh](#about-platformsh)
- [Usage](#usage)
- [Migrating](#migrating)
- [License](#license)
- [Contact](#contact)
- [Resources](#resources)
- [Contributors](#contributors)

<br/><hr><br/>

# Getting started

<br />
<h1>Getting started </h1>

If you are unfamiliar with Metabase, with Platform.sh, or otherwise want to quickly deploy this template, **Start here**.

This template contains all of the files needed to deploy on Platform.sh, but you have a few options for doing so. Whichever method you choose, be sure to make note of all of the information included in this README, as it will be a great deal of help once your project has been deployed.

## Deploying

The quickest method to deploy Metabase on Platform.sh is by clicking the button below. This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/metabase/.platform.template.yaml&utm_content=metabase&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>

If you do not already have a Platform.sh account, you will be asked to fill out some basic information, after which you will be given a 30-day free trial to experiment with our platform.

<details>
<summary><strong>Deploy manually</strong></summary><br />

If you would instead to deploy this template from your command line, you can do so through the following steps.

> **Note:**
>
> If you do not already have a Platform.sh account, you will need to [start a free trial](https://accounts.platform.sh/platform/trial/general/setup) before creating a new project.

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/metabase
   ```

2. Install the Platform.sh CLI:

   ```bash
   curl -sS https://platform.sh/cli/installer | php
   ```

3. Create a new project:

   ```bash
   cd metabase && platform project:create
   ```

4. Set the project as a remote for the repository (prompt):

   ```bash
   Set the new project Metabase as the remote for this repository? [Y/n]   Y
   ```

   Once you have verified the project creation steps, you will receive some additional information about the project.

   ```text
   The Platform.sh Bot is activating your project

       ▄     ▄
       ▄█▄▄▄█▄
     ▄██▄███▄██▄
     █ █▀▀▀▀▀█ █
        ▀▀ ▀▀

   The project is now ready!
   <PROJECT ID>

   Region: <PROJECT REGION>.platform.sh
   Project ID: <PROJECT ID>
   Project title: Metabase
   URL: https://console.platform.sh/<USERNAME>/<PROJECT ID>
   Git URL: <PROJECT ID>@git.<PROJECT REGION>.platform.sh:<PROJECT ID>.git

   Setting the remote project for this repository to: Metabase (<PROJECT ID>)
   ```

5. Push to Platform.sh:

   ```bash
   git push platform main
   ```

</details>

## Post-install

After the first deployment, give the JVM a minute to finish completing it's initialization tasks (until it does, you will see a 502 error page.) which take only a minute or so. Run through the Metabase installer as normal. You will not be asked for database credentials, as those are already provided via the [`.environment`](.environment) that is sourced during the deploy hook. With the installer you will be able to create admin credentials and choose your language.

The installer will allow you to add databases. Configure the database you are trying to connect, or skip that step and Metabase will load an H2 Sample Dataset to start off with.

<br />
<h1>Customizations </h1>

**Some more general explanation of why these files are necessary additions to replicate**

The following files have been added in order to download Metabase during the build hook and to deploy the application on Platform.sh. If using this template as a reference for your own project, replicate the changes below.

### Configuration

Every application you deploy on Platform.sh is built as a **virtual cluster** containing a set of containers which defines a particular **environment**. The default branch (`master`, `main`, etc.) is always deployed as your production environment, whereas any other branch can be deployed as a development environment.
Within an environment there are three types of containers, each of which are managed by three required files that have been included in this repository:

<details>
<summary><strong>The Router container (<code>.platform/routes.yaml</code>)</strong></summary><br />

For each cluster/environment there will always be exactly one Router container, which is a single nginx process. It's configuration file [**`.platform/routes.yaml`**](.platform/routes.yaml) defines how incoming requests map the the appropriate Application container, while providing basic caching of responses if so configured. The Router Container has no persistent storage.

**Metabase**

For Metabase, two routes have been defined. One `upstream` route directs requests directly to the Metabase application container at the `www` subdomain, which defined by the `upstream` value `"app:http"`. Notice that the application container name `app` is matched in the `name` attribute in [`.platform.app.yaml`](.platform.app.yaml).

```yaml
'https://www.{default}/':
  type: upstream
  upstream: 'app:http'

'https://{default}/':
  type: redirect
  to: 'https://www.{default}/'
```

There is also a `redirect` route configured, which automatically redirects all request to the `www` subdomain upstream route.

<!-- **Some second application** -->

A `{default}` placeholder is included on all defined routes. This placeholder will be replaced with the production domain name configured for your project's production branch, and will be substituted with a unique generated domain for each of your development environments based on the region, project ID, and branch name.

</details>

<details>
<summary><strong>Service containers (<code>.platform/services.yaml</code>)</strong></summary><br />

Each virtual cluster can have zero or more Service containers, but the file which configures them [**`.platform/services.yaml`**](.platform/services.yaml) is still required in your repository. Each top level key in that file will correspond to a separate Service container, with the kind of service determined by its `type`.

For Metabase's primary database, a single PostgreSQL service container has been added, identifiable by the service name `db`. Notice that in order for the application container to be granted access to this service it's necessary that a [**relationship**](https://docs.platform.sh/configuration/app/relationships.html) is defined in [`.platform.app.yaml`](.platform.app.yaml).

```yaml
# .platform.app.yaml

relationships:
  database: 'db:postgresql'
```

With this relationship defined, the database will now be made accessible to the application on the internal network at `database.internal` with its credentials visible within the [`PLATFORM_RELATIONSHIPS`](https://docs.platform.sh/configuration/services/postgresql.html#relationship) environment variable, which is a base64-encoded JSON object. Along with a number of other Metabase-specific environment variables, service credentials are set within the [`.environment`](.environment) file, which is sourced in the application root when the environment starts as well as when logging into that environment over SSH. You will notice that this file leverages [jq](https://stedolan.github.io/jq/), a lightweight command-line JSON processor that comes pre-installed on all application containers.

</details>

<details>
<summary><strong>Application containers (<code>.platform.app.yaml</code>)</strong></summary><br />

There must always be one Application container in your cluster, but there [may be more](https://docs.platform.sh/configuration/app/multi-app.html). It is from this file that you are able to define the container's runtime language and version, it's relationships to other containers, and how it is [built and deployed](#builds-and-deploys).

Every project you deploy on Platform.sh exists on a writable file system at build time, but it will become read-only once it enters the deploy phase (see [Builds and deploys](#builds-and-deploys)) for more information. Because of this, any directories that require write access to the file system at runtime must be declared as `mounts`, and must include the `disk` attribute that defines the available disk space for the data in these directories.

**Metabase**

For Metabase, the `temp` and `data` directories are required in order to load the example dataset that comes with Metabase. Since the upstream jar file is unpacked during the start command, which includes writing a number of plugins to the filesystem, `plugins` will also be a mounted directory.

```yaml
# The name of this application, which must be unique within a project.
name: app

# The type key specifies the language and version for your application.
type: java:11
```

Metabase's `.platform.app.yaml` file has a `type` specified such that Java 11 will be the container's primary runtime language. This container is accessible to the rest of the cluster by the name `app`, which you will notice is also the name used in defining Metabase's `upstream` route in `.platform/routes.yaml`.

<!-- **Some second application** -->

The `.platform.app.yaml` file comes with many more features than are described here, so visit the [**Configure your application**](https://docs.platform.sh/configuration/app.html) section of the documentation for more details.

</details>

### Builds and deploys

Every time you push to a live branch (a git branch with an active environment attached to it) or activate an [environment](https://docs.platform.sh/administration/web/environments.html) for a branch, there are two main processes that happen: Build and Deploy.

1. The build process looks through the configuration files in your repository and assembles the necessary containers.
2. The deploy process makes those containers live, replacing the previous versions, with virtually no interruption in service.

<p align="center">
    <a href="https://docs.platform.sh/overview/build-deploy.html">
        <img src="https://docs.platform.sh/images/workflow/build-pipeline.svg" alt="Build & deploy">
    </a>
</p>

### Upstream modifications

At this time, Platform.sh's Metabase template does not include any of the upstream code in this repository. The Metabase `jar` file is installed during the build hook according to the version defined in a [`metabase.version`](metabase.version) file.

<br />
<h1>About Platform.sh </h1>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. 

<details>
<summary><strong>Overview</strong></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel. 

Nulla ornare, nisl et vehicula convallis, felis arcu sagittis nibh, luctus faucibus nunc magna sed est. Proin blandit porta ligula. Ut euismod lectus eu tincidunt blandit. Nulla nec urna sit amet felis facilisis volutpat. Vestibulum sed lectus vulputate, dapibus leo sit amet, porta mi. Maecenas ac convallis eros, id efficitur quam. Nunc ornare tristique eleifend. Donec consectetur, eros in hendrerit cursus, velit erat pretium sem, ac viverra ligula odio nec odio. Vestibulum sit amet tellus tempor tellus faucibus laoreet sit amet in tortor.

</details>

<details>
<summary><strong>Projects</strong></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel. 

Nulla ornare, nisl et vehicula convallis, felis arcu sagittis nibh, luctus faucibus nunc magna sed est. Proin blandit porta ligula. Ut euismod lectus eu tincidunt blandit. Nulla nec urna sit amet felis facilisis volutpat. Vestibulum sed lectus vulputate, dapibus leo sit amet, porta mi. Maecenas ac convallis eros, id efficitur quam. Nunc ornare tristique eleifend. Donec consectetur, eros in hendrerit cursus, velit erat pretium sem, ac viverra ligula odio nec odio. Vestibulum sit amet tellus tempor tellus faucibus laoreet sit amet in tortor.

</details>

<details>
<summary><strong>Builds</strong></summary><br />


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel. 

Nulla ornare, nisl et vehicula convallis, felis arcu sagittis nibh, luctus faucibus nunc magna sed est. Proin blandit porta ligula. Ut euismod lectus eu tincidunt blandit. Nulla nec urna sit amet felis facilisis volutpat. Vestibulum sed lectus vulputate, dapibus leo sit amet, porta mi. Maecenas ac convallis eros, id efficitur quam. Nunc ornare tristique eleifend. Donec consectetur, eros in hendrerit cursus, velit erat pretium sem, ac viverra ligula odio nec odio. Vestibulum sit amet tellus tempor tellus faucibus laoreet sit amet in tortor.

</details>

<details>
<summary><strong>Deploys</strong></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel. 

Nulla ornare, nisl et vehicula convallis, felis arcu sagittis nibh, luctus faucibus nunc magna sed est. Proin blandit porta ligula. Ut euismod lectus eu tincidunt blandit. Nulla nec urna sit amet felis facilisis volutpat. Vestibulum sed lectus vulputate, dapibus leo sit amet, porta mi. Maecenas ac convallis eros, id efficitur quam. Nunc ornare tristique eleifend. Donec consectetur, eros in hendrerit cursus, velit erat pretium sem, ac viverra ligula odio nec odio. Vestibulum sit amet tellus tempor tellus faucibus laoreet sit amet in tortor.

</details>

<details>
<summary><strong>Environments</strong></summary><br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu est lacus. Integer magna est, pellentesque vitae lorem a, molestie pharetra felis. Quisque massa lorem, ullamcorper sed urna eu, gravida placerat ipsum. Quisque tempus ex at sapien finibus, consequat condimentum lorem vehicula. Quisque posuere justo velit, vel luctus ipsum rutrum vel. 

Nulla ornare, nisl et vehicula convallis, felis arcu sagittis nibh, luctus faucibus nunc magna sed est. Proin blandit porta ligula. Ut euismod lectus eu tincidunt blandit. Nulla nec urna sit amet felis facilisis volutpat. Vestibulum sed lectus vulputate, dapibus leo sit amet, porta mi. Maecenas ac convallis eros, id efficitur quam. Nunc ornare tristique eleifend. Donec consectetur, eros in hendrerit cursus, velit erat pretium sem, ac viverra ligula odio nec odio. Vestibulum sit amet tellus tempor tellus faucibus laoreet sit amet in tortor.

</details>

<br />
<h1>Usage </h1>

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


<br />
<h1>License</h1>

This template uses the [Open Source edition of Metabase](https://github.com/metabase/metabase), which is licensed under the [GNU Affero General Public License (AGPL)](https://github.com/metabase/metabase/blob/master/LICENSE-AGPL.txt).

<br />
<h1>Contact</h1>

This template is maintained primarily by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channels and ping the `@devrel_team` with any questions.
<!-- - **E-mail:** You can also reach the DevRel team directly at `devrel@platform.sh`. -->

<br />
<h1>Resources</h1>

<!-- ### General -->

- [Metabase.com](https://www.metabase.com/)
- [Metabase Documentation](https://www.metabase.com/docs/latest/)
- [Metabase Repository](https://github.com/metabase/metabase)
- [Java on Platform.sh](https://docs.platform.sh/languages/java.html)

<!-- ### Blog posts

- Any related blog posts

### Community

- Community questions -->

<br />
<h1>Contributing</h1>

<h2 align="center">Help us keep top-notch templates!</h2>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<h3 align="center"><strong>How to contribute</strong></h3>
<br />
<p align="center">
    <a href="#"><strong>Read the Contributing Guidelines</strong></a><br />
    <a href="#"><strong>Report a bug</strong></a><br />
    <a href="#"><strong>Submit a feature request</strong></a><br />
    <a href="#"><strong>Open a pull request</strong></a><br />
</p>
<br />
<h3 align="center"><strong>Need help?</strong></h3>
<br />
<p align="center">
    <a href="#"><strong>Ask the Platform.sh Community</strong></a><br />
    <a href="#"><strong>Join us on Slack</strong></a><br />
</p>
<br /><br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>

<br/>

![GitHub Contributors Image](https://contrib.rocks/image?repo=chadwcarlson/metabase)

<br />

Additional thanks to [@rhubinak](https://github.com/rhubinak) for creating the original template.