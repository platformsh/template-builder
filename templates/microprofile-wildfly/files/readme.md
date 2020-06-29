# Wildfly MicroProfile for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/microprofile-wildfly/.platform.template.yaml&utm_content=microprofile-wildfly&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This project provides a starter kit for Wildfly Eclipse MicroProfile projects hosted on Platform.sh.  It includes a minimalist application skeleton that is intended for you to use as a starting point and modify for your own needs, along with the Platform.sh Config Reader to simplify accessing Platform.sh environment variables.

WildFly is a flexible, lightweight, managed application runtime that helps you build amazing applications.

## Features

* Java 11
* Automatic TLS certificates
* Maven-based build

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).
* An additional library dependency, [`platformsh/config-reader-java`](https://github.com/platformsh/config-reader-java), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Maven](https://maven.apache.org/)
* [Wildfly](https://wildfly.org/)
* [Eclipse MicroProfile](https://microprofile.io/)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
