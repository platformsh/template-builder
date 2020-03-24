# Mattermost for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/mattermost/.platform.template.yaml&utm_content=mattermost&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Mattermost on Platform.sh, configuring the deployment through user-defined environment variables.

Mattermost is an open-source messaging framework written in Go and React.

## Services

* Go 1.14
* PostgreSQL 12
* Elasticsearch 7.2

## Post-install

When Mattermost has been deployed, you can complete the installation by creating your first admin user through the site itself.

## Customizations

The following changes have been made relative from initializing a Mattermost project from its upstream binaries. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* Mattermost binaries are downloaded during the build hook in `setup.sh`. You can edit that file to download a newer version of the upstream on a new environment to update.
* Environment variables are set in the `.environment` file, which override default settings created in Mattermost's `/app/config/config.json` file, which allow  allow Mattermost to connect to PostgreSQL and Elasticsearch.

## References

* [Mattermost](https://mattermost.com/)
* [GitHub upstream](https://github.com/mattermost/mattermost-server)
* [Mattermost documentation](https://docs.mattermost.com/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
