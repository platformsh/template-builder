
<p align="right">
<a href="https://platform.sh">
<img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
</a>

</p>

<p align="center">
<a href="https://www.govcms.gov.au/">
<img src="header.svg"  />
</a>
</p>

<h1 align="center">Deploy GovCMS 10 on Platform.sh</h1>

<p align="center">
<a href="https://github.com/platformsh-templates/drupal10/blob/master/README.md"><strong>Find out about Drupal 10 on Platform.sh</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/govCMS/GovCMS/blob/3.x-develop/README.md"><strong>Find out about GovCMS</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br /><br />
</p>

<p align="center">
<a href="https://github.com/platformsh-templates/drupal10-govcms10/issues">
<img src="https://img.shields.io/github/issues/platformsh-templates/drupal10-govcms10.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal10-govcms10/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh-templates/drupal10-govcms10.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal10-govcms10/blob/master/LICENSE">
<img src="https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&labelColor=f4f2f3&color=ffd9d9" alt="License" />
</a>&nbsp&nbsp
<br /><br />
<a href="https://console.platform.sh/projects/create-project/?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal10-govcms10/.platform.template.yaml&utm_campaign=deploy_on_platform?utm_medium=button&utm_source=affiliate_links&utm_content=https://raw.githubusercontent.com/platformsh-templates/drupal10/updates/.platform.template.yaml" target="_blank" title="Deploy with Platform.sh"><img src="https://platform.sh/images/deploy/deploy-button-lg-blue.svg" width="175px"></a>
</p>
</p>

<hr>

## About Drupal 10 on Platform.sh

This template builds Drupal using the "GovCMS" distribution install profile.
It is pre-configured to use MariaDB and Redis for caching.
The Drupal installer will skip asking for database credentials as they are already provided.

> You should choose the "GovCMS" install profile when prompted to by the install wizard during initial setup.

### Features

- PHP 8.3
- MariaDB 10.11
- Redis 7.2
- Drush included
- Automatic TLS certificates
- Composer-based build

Please see [`platformsh-templates/drupal10:README.md`](https://github.com/platformsh-templates/drupal10/blob/master/README.md) for a full introduction to getting started and using the Platform.sh system, including:

* Deployment
* Local Development
* Migration
* Troubleshooting

## About GovCMS

[GovCMS](https://www.govcms.gov.au) is an open source web content management and hosting service, based on Drupal and developed to help agencies create modern, affordable and responsive websites, whilst making it easier to collaborate and innovate. GovCMS also helps reduce the technology and compliance burden on government agencies. GovCMS is managed by the Australian Government Department of Finance.

GovCMS Slack channel: https://govcmschat.slack.com/archives/C01BD9B3V5W

Please see [`govCMS/GovCMS:README.md`](https://github.com/govCMS/GovCMS/blob/3.x-develop/README.md/) for a full introduction to the GovCMS project, including:

* Installation
* Troubleshooting and Contributing

> The GovCMS distribution is a deliberately restricted and curated set of modules, and you are advised to read [the guidelines for usage and development published by the maintainers](https://www.govcms.gov.au/support/tech-talk) before modifying things too much.

## Quickstart

The quickest way to deploy this template on Platform.sh is by clicking the button below.
This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal10/.platform.template.yaml&utm_content=drupal10&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>
<br/>



You can also quickly recreate this project locally with the following command:

```bash
composer create-project platformsh/drupal10-govcms10 -s dev
```

## About this template

This project template is based on [the public Platform.sh Drupal10 template](https://github.com/platformsh-templates/drupal10/tree/0a0257ddc427d7b7f7d87fb85fdb64604d5556b9) from [the Platform.sh template library](https://docs.platform.sh/development/templates.html).
See the [Platform.sh documentation for deploying Drupal](https://docs.platform.sh/guides/drupal/deploy.html) for more.

This template has been modified slightly, with reference to [the `govCMS/GovCMS` installer](https://github.com/govCMS/GovCMS) to add a few requirements to the `composer` configurations to suit the GovCMS installation.

### Upgrading

#### Upgrading GovCMS and Drupal

The template requires the Drupal distribution `govcms/govcms: ^3` which at the time of release (v 3.15) means Drupal 10 (v 10.2.7).

Running `composer upgrade` should be sufficient to keep your project up to date with newer releases to both GovCMS and Drupal core, as well as security releases.
It is not advised to require or define the Drupal core version yourself, the GovCMS template will pin the latest compatible Drupal version itself.

#### Upgrading Platform.sh configurations

You are expected to review and modify this template code  (`.platformsh.app.yaml` etc) to your specific application requirements [as described in the documentation](https://docs.platform.sh/create-apps/app-reference.html), so it's normal to use the template only as a reference once you've started building your app.

Over time, there may be minor updates added to the base Platform.sh Drupal template.
Although it's seldom necessary, you can follow the updates from the repository starting from the first commit.
Patches like this should be applied manually as your own configuration is expected to diverge from the template as you develop.

<hr/>

<p align="center">
<strong>Need help?</strong>
<br /><br />
<a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
