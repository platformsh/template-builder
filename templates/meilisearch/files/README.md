# Meilisearch for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/meilisearch/.platform.template.yaml&utm_content=meilisearch&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template provides a demo Meilisearch search engine on Platform.sh. The Meilisearch executable itself is downloaded during the build hook, and an example [`movies`](https://github.com/meilisearch/MeiliSearch/tree/master/datasets/movies) index provided by Meilisearch is added to the engine using the [`meilisearch-python`](https://github.com/meilisearch/meilisearch-python) library and Poetry during the deploy hook. You can specifiy the version of Meilisearch by updating the `.platform.app.yaml` file. 

Meilisearch is an open source RESTful search API providing a fast and relevant search engine from a downloaded binary written in Rust. 

## Features

* Python 3.8
* Automatic TLS certificates
* Meilisearch downloaded on the fly during build

## Post-install

There are no further steps required post-install to deploy the Meilisearch template on Platform.sh. However, this template deploys Meilisearch's documented example index and runs in development mode by default so that that demo can be run in the browser out of the box. It is not production ready, but it can be made so with only a few changes. 

First, you will likely want to add an additional application for a frontend site that will communicate with Meilisearch. For this reason, the Meilisearch template resides in a `search` subdirectory. For the purposes of this demo, Meilisearch is accessible from the primary route, but you will likely want to update `routes.yaml` so that `search.{default}` is directed to the Meilisearch engine instead. Then, you can develop your frontend application on the primary route within a `frontend` subdirectory or similar, and communicate with Meilisearch through a relationship defined in the frontend's `.platform.app.yaml` file. 

Second, Meilisearch protects against a user's ability to access search results from within the browser when in production, limiting API requests to those that use a *master key* shared by the server itself. On Platform.sh a project-wide environment variable [`PLATFORM_PROJECT_ENTROPY`](https://docs.platform.sh/development/variables.html#platformsh-provided-variables) is available to both Meilisearch and a frontend application and can be used for this purpose. Run the Meilisearch server in production mode by passing that variable in a modified start command:

```yaml
start: "./meilisearch --http-addr localhost:${PORT} --master-key $PLATFORM_PROJECT_ENTROPY"
```

The frontend app will at some point need to make an internal request (via a definied relationship to the Meilisearch container) to the [`/keys` endpoint](https://docs.meilisearch.com/references/keys.html#get-keys) using the `PLATFORM_PROJECT_ENTROPY` variable to retrieve a *public key* that can then be used in your frontend queries.

Finally, this demo uses an [index of movies](https://github.com/meilisearch/MeiliSearch/tree/master/datasets/movies) sited often in Meilisearch's documentation to seed the search engine using the [`meilisearch-python`](https://github.com/meilisearch/meilisearch-python) library in `update_demo_index.py`. Review and modify this file to add your own index to Meilisearch. 

## Customizations

The following changes have been made to run and intialize Meilisearch on Platform.sh. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* `update_demo_index.py` has been added to add a demo `movies.json` index to the search engine, wiping the previous data on each deploy. 

## References

* [Meilisearch](https://meilisearch.com/)
* [Meilisearch documentation](https://docs.meilisearch.com/)
