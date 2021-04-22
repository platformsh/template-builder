# Next.js for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextjs/.platform.template.yaml&utm_content=nextjs&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a simple application using the Next.js web framework. It includes a minimal application skeleton that demonstrates how to set up an optimized build using Next.js and Yarn, as well as how to begin defining individual pages (such as the `/api/hello`) endpoint that comes pre-defined with this template.

Next.js is an open-source web framework written for Javascript.

## Features

* Node.js 14
* Automatic TLS certificates
* yarn-based build

## Customizations

The following files and additions make the framework work on Platform.sh, modified from the `npx` command [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app). If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional module, [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A `handle_mounts.sh` script has been added. This script handles committed files pushed to directories also defined as mounts on Platform.sh.

## References

* [Next.js](https://nextjs.org/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
