# Elastic APM with Kibana for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/elastic-apm/.platform.template.yaml&utm_content=elastic-apm&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Elastic APM (Application Performance Monitoring) with a Kibana front-end.  It is intended as a complete self-contained monitoring solution, although authentication needs to be configured for your specific application.

## Features

* Elasticsearch 7.2
* Kibana
* Elastic APM
* Automatic TLS certificates
* APM and Kibana downloaded on-the-fly during build

## Post-install

1. Elasticsearch is configured to require authentication with a user and password that is generated automatically and available in the relationships array.  Kibana is configured to inherit those credentials.  To access them, run `platform relationships -A kibana -p <URL of your site>`.  That will show the relationship information for the kibana application, which will include `username` and `password` keys.  You may use those to login at your site's URL.

> **Note**
>
> Although the Kibana UI has a way for you to change the user and password, do not do so.  Trying to change the password will leave Kibana and Elasticsearch out of sync and inaccessible.

2. After logging into Kibana, go to `/app/apm`.  You will get a message that no APM services are installed and a "Setup instructions" button.  Click that.  It will present you with instructions to install an APM server which you can ignore as that is already done by the template.  Instead, consult the APM Agent instructions for your chosen language further down for instructions on how to connect your application to APM.

3. (Optional) Elasticsearch is not publicly routable by default.  It can only be accessed through Kibana or APM.  If you wish to expose Elasticsearch to the public, you may add a route to `routes.yaml` that uses `elasticsearch:http` as its upstream.  Note that all connections to Elasticsearch will require HTTP Basic Authentication, using the same user and password that you use to login to Kibana.

## Structure

This is an unusual project in that it contains no application code.  Both APM and Kibana are downloaded as part of the build step in their respective application containers.  Only the configuration files are provided.  You may adjust the configuration files as appropriate for your use case.  Committing APM or Kibana themselves to the repository is not recommended.

The versions of Kibana and APM that are downloaded are specified as environment variables in the build hooks.  Kibana and APM are very sensitive to version compatibility, so if upgrading the version ensure that you upgrade both in tandem, and possibly Elasticsearch itself as well.

## Embedding into another project

If you would prefer to include the full APM suite inside another project, do the following:

1. Copy the `kibana` and `apm` directories to your application as-is.

2. Copy the `elasticsearch` service definition from `services.yaml` to your project's `services.yaml`.  Do not rename the service or else the default configuration provided will not work.

3. Add an additional route in your project at the subdomain of your choosing that has an upstream of `kibana:http`, and another that has an upstream of `apm:http`.

## Customizations

On its initial run, Kibana by default will run a self-optimize step.  This step is very memory intensive and will not complete successfully on a Platform.sh `S` sized container (used by development environments).  Instead, this repository includes the optimized asset files pre-loaded, and copies them into place in the Kibana deploy hook.  That skips the self-optimize step.

If you upgrade Kibana, you will need to re-generate the pre-optimized files.  To do so, run the following command locally:

```bash
# If you are on Mac, use the "darwin" line.  Otherwise use the "linux" line.
# KIBANA_PLATFORM=darwin-x86_64
export KIBANA_PLATFORM=linux-x86_64
export KIBANA_VERSION=7.2.1
./download_and_install.sh
./optimize.sh
```

Update the `KIBANA_VERSION` variable in that set of commands and run it to download and optimize Kibana.  You can then commit the resulting `_kibana_optimize` folder to the repository at the same time that you increase the Kibana version in `kibana/.platform.app.yaml`.

## References

* [Kibana](https://www.elastic.co/products/kibana)
* [Elastic APM](https://www.elastic.co/products/apm)
