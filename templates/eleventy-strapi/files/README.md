<br />
<p align="left">
    <a href="https://platform.sh">
        <img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
    </a>
</p>
<br /><br />
<p align="center">
    <a href="https://github.com/strapi/foodadvisor">
        <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d2ecfe9f-fa41-4caa-98e6-1354850c39d1/Logo.WhiteBackground.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220311T182042Z&X-Amz-Expires=86400&X-Amz-Signature=7304a7f6d04754b75ce437049b853bc5abd05998fd17e4f2d1a2bd36d32840b4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Logo.WhiteBackground.png%22&x-id=GetObject" width="300">
    </a>
</p>
<br /><br />
<h1 align="center">Deploy Next.js and Strapi on Platform.sh</h1>

<p align="center">
    <strong>Contribute to the Platform.sh knowledge base, or check out our resources</strong>
    <br />
    <br />
    <a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Request a feature</strong></a>
    <br /><br />
</p>

<p align="center">
    <a href="https://github.com/platformsh-templates/metabase/issues">
        <img src="https://img.shields.io/github/issues/platformsh-templates/nextjs-strapi.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/pulls">
        <img src="https://img.shields.io/github/issues-pr/platformsh-templates/nextjs-strapi.svg?style=flat-square&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
    </a>&nbsp&nbsp
    <a href="https://github.com/platformsh-templates/nextjs-strapi/blob/master/LICENSE">
        <img src="https://img.shields.io/static/v1?label=License&message=MIT&style=flat-square&labelColor=f4f2f3&color=ffd9d9" alt="License" />
    </a>&nbsp&nbsp
    <br /><br /><br />
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextjs-strapi/.platform.template.yaml&utm_content=nextjs-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="175px" />
    </a>
</p>
</p>

<hr>
<br />

## Contents

- [About this project](#about-this-project)
- [Getting started](#getting-started)
- [Customizations](#customizations)
- [License](#license)
- [Contact](#contact)
- [Resources](#resources)
- [Contributing](#contributing)

## About this project

This template demonstrates a multi-app deployment on Platform.sh, in this case, a Next.js frontend consuming data from a Strapi backend running on the same environment. It is based on Strapi's official demo repository, [Foodadvisor](https://github.com/strapi/foodadvisor), and is identical to that project aside from a few small modifications needed to deploy on Platform.sh. 

Next.js is an open-source web framework written for Javascript, and Strapi is a Headless CMS framework written in Node.js.

### Features

- Strapi v4
- Node.js 16
- MySQL 8
- Automatic TLS certificates
- Multi-app configuration
- yarn-based builds
- Delayed SSG build (post deploy hook)

## Getting started

### Deploy

#### Quickstart

The quickest way to deploy this template on Platform.sh is by clicking the button below. This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextjs-strapi/.platform.template.yaml&utm_content=nextjs-strapi&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
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
   git clone https://github.com/platformsh-templates/nextjs-strapi
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

   Click the [Use this template](https://github.com/platformsh-templates/nextjs-strapi/generate) button at the top of this page to create a new repository in your namespace containing this demo. Then you can clone a copy of it locally with `git clone git@github.com:YOUR_NAMESPACE/nextjs-strapi.git`.

1. Create a free trial:

   [Register for a 30 day free trial with Platform.sh](https://auth.api.platform.sh/register). When you have completed signup, select the **Create from scratch** project option. Give you project a name, and select a region where you would like it to be deployed. As for the *Production environment* option, make sure to match it to whatever you have set at `https://YOUR_NAMESPACE/nextjs-strapi`.

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
   git clone https://github.com/platformsh-templates/nextjs-strapi
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
> You can find the full [Bitbucket integration documentation here](https://docs.platform.sh/integrations/source/bitbuckethtml).

1. Clone this repository:

   ```bash
   git clone https://github.com/platformsh-templates/nextjs-strapi
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

This demo repository is set up to deploy both front and backend application containers to the production environment, and to initialize the database with files and data from the original Foodadvisor demo provided by Strapi. 

To login to the Strapi Admin UI, you can use the credentials `admin@example.com/Admin1234` to start, after which you are free to update them at `https://api.GENERATED_URL/admin/me`.

### Local development

This section provides instructions for running the Next.js + Strapi template locally, connected to a live database instance on an active Platform.sh environment. Alternatively, if you would like to run this demo as originally intended by Strapi using SQLite, you can follow the instructions found in `README_upstream.md`. 

In all cases for developing with Platform.sh, it's important to develop on an isolated environment - do not open SSH tunnels to your production environment when developing locally. Each of the options below assume the following starting point:

```bash
platform get PROJECT_ID
cd project-name
platform environment:branch updates
```

> **Note:**
>
> For many of the steps below, you may need to include the CLI flags `-p PROJECT_ID` and `-e ENVIRONMENT_ID` if you are not in the project directory or if the environment is associated with an existing pull request.

<details>
<summary>Running the Strapi backend</summary><br />

```bash
# Open a SSH tunnel to the environment's database.
platform tunnel:open -A strapi

# Mock environment variable that contains service credentials. 
export PLATFORM_RELATIONSHIPS="$(platform tunnel:info -A strapi --encode)"

# Pull public/uploads files from the environment.
cd api
platform mount:download -A strapi -m public/uploads --target public/uploads -y

# Build Strapi and start the server.
yarn --frozen-lockfile
yarn develop
```

Strapi will then serve on `localhost:1337` using a live service on the isolated Platform.sh environment.

</details>

<details>
<summary>Running the Next.js frontend</summary><br />

You have two options when running Next.js locally. You can connect to a Strapi instance on an active Platform.sh environment, or run Strapi locally in parallel and connect to that.

1. **Option 1:** Connecting to Strapi on a Platform.sh environment:

    > **Requirements:**
    >
    > In order to retrieve the backend url within live environment from environment variables, this demo uses [jq](https://stedolan.github.io/jq/manual/v1.6/) - the JSON filtering command line tool. jq comes pre-installed on all Platform.sh runtime containers, and in order to replicate the behavior described below and build Next.js locally, you will need to also have it [installed on your system](https://stedolan.github.io/jq/download/). 

    ```bash
    cd client

    # Get the live backend Strapi url (note the 'id' attribute defined in .platform/routes.yaml).
    BACKEND_URL=$(platform ssh 'echo $PLATFORM_ROUTES | base64 --decode' -A nextjs -q | jq -r 'to_entries[] | select (.value.id == "api") | .key')

    # Get the preview secret.
    PREVIEW_SECRET=$(platform ssh 'echo $PLATFORM_PROJECT-$PLATFORM_BRANCH' -A nextjs -q)

    # Output to .env.development.
    printf "NEXT_PUBLIC_API_URL="${BACKEND_URL:8:${#BACKEND_URL}-9}"\nPREVIEW_SECRET=$PREVIEW_SECRET\n" > .env.local

    # Build and run the Next.js server.
    yarn --frozen-lockfile
    yarn dev
    ```

2. **Option 2:** Connecting to a locally running Strapi development server

    This demo assumes a locally running Strapi instance by default, so once you have followed the steps above for Strapi you will be able to start the Next.js development server normally.

    ```bash
    # Build and run the Next.js server.
    cd client
    yarn --frozen-lockfile
    yarn dev
    ```

    Next.js will be served from `localhost:3000` pulling data from a local Strapi instance running at `localhost:1337`.

</details>

## Customizations

The following changes have been made relative to the [Strapi Foodadvisor official demo](https://github.com/strapi/foodadvisor) to run on Platform.sh. If using this project as a reference for your own existing project, replicate the changes below to your project.

<details>
<summary>Shared files</summary><br />

- The upstream `README.md` was renamed, and this Platform.sh-specific README was committed in its place.
- `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration for provisioning an Oracle MySQL container and for defining how traffic is handled between the two application containers, respectively. They are present in all projects on Platform.sh, and you may customize them as you see fit. Consult those files for more information, or take a look at the [Routes](https://docs.platform.sh/configuration/routes.html) and [Services](https://docs.platform.sh/configuration/services.html) documentation for details about configuration. 

</details>

<details>
<summary>Strapi customizations (<code>api</code>)</summary><br />

- `http:/*` was added to `.gitignore`, as this directory was sometimes generated during local development.
- The `mysql` dependency was added, so as to connect to the database service on Platform.sh.
- A number of dependencies are pinned to specific versions in the upstream [Foodadvisor](https://github.com/strapi/foodadvisor). Those dependencies have been unpinned so that our template maintenance workflows can reliable update dependencies on a schedule. 
- A zipped file (`api/foodadvisor.tar.gz`) was added, which contains a database dump and a collection of demo images used in the original Foodadvisor demo, altered to work with Oracle MySQL. It is used on the first deployment within the Strapi deploy hook to set up the database. You are free to delete this file after this demo has been deployed.
- A `api/.platform.app.yaml` file has been added, which is required to define the build and deploy process for all application containers on Platform.sh. It is set to run Strapi if production mode across all environments, so you will need to clone the repository (`platform get PROJECT_ID`) local and run a development server in order to add new collections. Take a look at the [Application](https://docs.platform.sh/configuration/services.html) documentation for more details about configuration.
- A `api/config/database.js` file has been added, which does two things. First, it reads from Platform.sh environment variables to detect the database service connected to the `database` relationship in `api/.platform.app.yaml`. In this case, that's Oracle MySQL, and it uses credentials provided in the `PLATFORM_RELATIONSHIPS` environment variable to connect to that service. Second, it detects whether or not Strapi is actually running on Platform.sh, and makes accomodations to run Strapi locally depending on if an SSH tunnel has been opened to a database running on an active Platform.sh environment. 
- A `.environment` file has been added. This file is sourced on a Platform.sh environment during startup, at the beginning of the deploy hook, and whenever you SSH into the environment (`platform ssh -e ENVIRONMENT_ID`). It initializes environment variables specific to this demo, such as Strapi security tokens, relevant Next.js frontend URLs, and defines database credential aliases used during the deploy hook. 
- There is an [open issue](https://github.com/strapi/strapi/issues/12101) where Strapi rejects collections with names that are too long, so the demo has been altered slightly (the collection `name` within `api/src/components/blocks/related-restaurants.json` has been shortened) for this demo repo.

</details>

<details>
<summary>Next.js customizations (<code>client</code>)</summary><br />

- A `.environment` file has been added. This file is sourced on a Platform.sh environment during startup, at the beginning of the deploy hook, and whenever you SSH into the environment (`platform ssh -e ENVIRONMENT_ID`). It initializes environment variables specific to this demo, specifically the backend Strapi url for the current environment. You will need to replicate these commands to run Next.js locally, so see the [Local development](#local-development) section for more details. 
- A `client/.platform.app.yaml` file has been added, which is required to define the build and deploy process for all application containers on Platform.sh. Because of how Platform.sh works, the Next.js build is delayed considerably to the `post_deploy` hook after the Strapi container has fully deployed and has begun serving its endpoints. Take a look at the [Application](https://docs.platform.sh/configuration/services.html) documentation for more details about configuration.

</details>

## License

This template uses the [Foodadvisor demo repository]() provided by Strapi.io as its base, which is licensed under the [MIT License](https://github.com/strapi/foodadvisor/blob/master/LICENSE).

## Contact

This template is maintained primarily by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channels and ping the `@devrel_team` with any questions.

## Resources

- [Strapi.io](https://strapi.io)
- [Strapi Documentation](https://docs.strapi.io/developer-docs/latest/getting-started/introduction.html)
- [Strapi Foodadvisor Repository](https://github.com/strapi/foodadvisor)
- [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)

## Contributing

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<h4 align="center"><strong>How to contribute</strong></h4>
<br />
<p align="center">
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Report a bug</strong></a><br />
    <a href="https://github.com/platformsh-templates/nextjs-strapi/issues"><strong>Submit a feature request</strong></a><br />
    <a href="https://github.com/platformsh-templates/nextjs-strapi/pulls"><strong>Open a pull request</strong></a><br />
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

![GitHub Contributors Image](https://contrib.rocks/image?repo=platformsh-templates/nextjs-strapi)

<br />

@todo
- update user name in tar.gz file from Node Workshop --> Platform.sh Templates
- Trailing question mark on title? Dump error?
