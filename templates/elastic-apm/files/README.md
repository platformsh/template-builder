# Elastic APM with Kibana for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/elastic-apm/.platform.template.yaml&utm_content=elastic-apm&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Elastic APM (Application Performance Monitoring) with a Kibana front-end.  It is intended as a complete self-contained monitoring solution, although authentication needs to be configured for your specific application.

## Services

* Elasticsearch 7.2

## Post-install

1. Run through the Drupal installer as normal.  You will not be asked for database credentials as those are already provided.

2. Once Drupal is fully installed, edit your `.platform.app.yaml` file and uncomment the line under the `relationships` block that reads `redis: 'rediscache:redis'`.  Commit and push the changes.  That will enable Drupal's Redis cache integration.  (The Redis cache integration cannot be active during the installer.)

## Structure

This is an unusual project in that it contains no application code.  Both APM and Kibana are downloaded as part of the build step in their respective application containers.  Only the configuration files are provided.  You may adjust the configuration files as appropriate for your use case.  Committing APM or Kibana themselves to the repository is not recommended.

The versions of Kibana and APM that are downloaded are specified as environment variables in the build hooks.  Kibana and APM are very sensitive to version compatibility, so if upgrading the version ensure that you upgrade both in tandem, and possibly Elasticsearch itself as well.

## Customizations

On initial run, Kibana by default will run a self-optimize step.  This step is very memory intensive and will not complete successfully on a Platform.sh `S` sized container (used by development environments).  Instead, this repository includes the optimized asset files pre-loaded, and copies them into place in the Kibana deploy hook.  That skips the self-optimize step.

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
