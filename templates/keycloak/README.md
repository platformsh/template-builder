# Keycloak for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/keycloak/.platform.template.yaml&utm_content=keycloak&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This project provides a starter kit for Keycloak projects hosted on Platform.sh.

Keycloak is an Open Source software tool to allow single sign-on with Identity Management and Access Management aimed at modern applications and services.

## Services

* Java 11

## Customizations

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).

> **note**
>
> This template must be initialized on a *Large* Platform.sh plan, due to Keycloak's [minimum memory requirements](https://www.keycloak.org/docs/latest/server_installation/).
>
> After the project has been initialized, make sure to [increase the size of your application containers on development environments](https://platform.sh/blog/2019/supersize-app-containers-in-your-dev-environments/) as well.


## References

* [Keycloak](https://www.keycloak.org/) 
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
