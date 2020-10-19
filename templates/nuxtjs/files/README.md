# NuxtJS for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nuxtjs/.platform.template.yaml&utm_content=nuxtjs&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a simple application using the NuxtJS web framework that can be used a starting point.

NuxtJS is an open-source web framework based on Vue.js.

## Features

* Node.js 14
* Automatic TLS certificates
* yarn-based build

## Customizations

The following files and additions make the framework work on Platform.sh, modified from the `npx` command [`create-nuxt-app`](https://github.com/nuxt/create-nuxt-app). If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added. These provide Platform.sh-specific configuration and are present in all projects on Platform.sh. You may customize them as you see fit.

## References

* [NuxtJS](https://nuxtjs.org/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
