
<p align="right">
<a href="https://platform.sh">
<img src="https://platform.sh/logos/redesign/Platformsh_logo_black.svg" width="150px">
</a>

</p>

<p align="center">
<a href="https://www.govcms.gov.au/">
<img src="govcms-logo.png" alt="GovCMS logo"  width="100px"  />
</a>
</p>

<h1 align="center">Deploy GovCMS 9 on Platform.sh</h1>

<p align="center">
<a href="https://github.com/platformsh-templates/drupal9/blob/master/README.md"><strong>Find out about Drupal9 on Platform.sh</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/govCMS/GovCMS/blob/2.x-develop/README.md"><strong>Find out about GovCMS</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br /><br />
</p>

<p align="center">
<a href="https://github.com/platformsh-templates/drupal9-govcms9/issues">
<img src="https://img.shields.io/github/issues/platformsh-templates/drupal9-govcms9.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9-govcms9/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh-templates/drupal9-govcms9.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-templates/drupal9-govcms9/blob/master/LICENSE">
<img src="https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&labelColor=f4f2f3&color=ffd9d9" alt="License" />
</a>&nbsp&nbsp
<br /><br />
<a href="https://console.platform.sh/projects/create-project/?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal9-govcms9/.platform.template.yaml&utm_campaign=deploy_on_platform?utm_medium=button&utm_source=affiliate_links&utm_content=https://raw.githubusercontent.com/platformsh-templates/drupal9/updates/.platform.template.yaml" target="_blank" title="Deploy with Platform.sh"><img src="https://platform.sh/images/deploy/deploy-button-lg-blue.svg" width="175px"></a>
</p>
</p>

<hr>

## About Drupal 9 on Platform.sh

This template builds Drupal using the "GovCMS" distribution install profile.
It is pre-configured to use MariaDB and Redis for caching.
The Drupal installer will skip asking for database credentials as they are already provided.

> You should choose the "GovCMS" install profile when prompted to by the install wizard during initial setup.

### Features

- PHP 8.0
- MariaDB 10.4
- Redis 6
- Drush included
- Automatic TLS certificates
- Composer-based build

Please see [`platformsh-templates/drupal9:README.md`](https://github.com/platformsh-templates/drupal9/blob/master/README.md) for a full introduction to getting started and using the Platform.sh system, including:

* Deployment
* Local Development
* Migration
* Troubleshooting

## About GovCMS

[GovCMS](https://www.govcms.gov.au) is an open source web content management and hosting service, based on Drupal and developed to help agencies create modern, affordable and responsive websites, whilst making it easier to collaborate and innovate. GovCMS also helps reduce the technology and compliance burden on government agencies. GovCMS is managed by the Australian Government Department of Finance.

GovCMS9 Slack channel: https://govcmschat.slack.com/archives/C01BD9B3V5W

Please see [`govCMS/GovCMS:README.md`](https://github.com/https://github.com/govCMS/GovCMS/blob/2.x-develop/README.md/blob/2.x-develop/README.md) for a full introduction to the GovCMS project, including:

* Installation
* Troubleshooting and Contributing

> The GovCMS distribution is a deliberately restricted and curated set of modules, and you are advised to read [the guidelines for usage and development published by the maintainers](https://www.govcms.gov.au/support/tech-talk) before modifying things too much.

## Quickstart

The quickest way to deploy this template on Platform.sh is by clicking the button below.
This will automatically create a new project and initialize the repository for you.

<p align="center">
    <a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/drupal9/.platform.template.yaml&utm_content=drupal9&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
        <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="170px" />
    </a>
</p>
<br/>



You can also quickly recreate this project locally with the following command:

```bash
composer create-project platformsh/drupal9-govcms9 -s dev
```

## About this template

This project template is based on [the public Platform.sh Drupal9 template](https://github.com/platformsh-templates/drupal9/tree/0a0257ddc427d7b7f7d87fb85fdb64604d5556b9) from [the Platform.sh template library](https://docs.platform.sh/development/templates.html).
See the [Platform.sh documentation for deploying Drupal 9](https://docs.platform.sh/guides/drupal9/deploy.html) for more.

This template has been modified slightly, with reference to [the `govCMS/GovCMS-project` installer](https://github.com/govCMS/GovCMS8-project) to add a few requirements to the `composer` configurations to suit the GovCMS installation.

### Upgrading

#### Upgrading GovCMS and Drupal

The template requires the Drupal distribution `govcms/govcms: ~2` which at the time of release (v 2.23.0) means Drupal 9 (v 9.4.7).

Running `composer upgrade` should be sufficient to keep your project up to date with newer releases to both GovCMS and Drupal core, as well as security releases.
It is not advised to require or define the Drupal core version yourself, the GovCMS template will pin the latest compatible Drupal version itself.

#### Upgrading Platform.sh configurations

You are expected to review and modify this template code  (`.platformsh.app.yaml` etc) to your specific application requirements [as described in the documentation](https://docs.platform.sh/create-apps/app-reference.html), so it's normal to use the template only as a reference once you've started building your app.

Over time, there may be minor updates added to the base Platform.sh Drupal template.
Although it's seldom neccessary, you can follow the updates from the repository [starting from this commit date](https://github.com/platformsh-templates/drupal9/tree/0a0257ddc427d7b7f7d87fb85fdb64604d5556b9)
Patches like this should be applied manually as your own configuration is expected to diverge from the template as you develop.

<hr/>

<p align="center">
<strong>Need help?</strong>
<br /><br />
<a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
