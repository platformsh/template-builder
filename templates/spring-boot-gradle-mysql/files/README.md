# Spring Boot Gradle for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/spring-boot-gradle-mysql/.platform.template.yaml&utm_content=spring-boot-gradle-mysql&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building a Spring Boot application. It uses Gradle to build the application and deploy it to Platform.sh.

A sample Hello World application is provided as a starting point.  It includes an Oracle MySQL database, and the sample application shows how to make the database connection. The example code also demonstrates how to access the Platform.sh environment variables using the Platform.sh Config Reader library.

## Features

* Java 8
* Oracle MySQL 8.0
* Automatic TLS certificates
* Gradle-based build

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [.platform/routes.yaml](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [.platform/services.yaml](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [.platform.app.yaml](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).
* An additional library dependency, [`platformsh/config-reader-java`](https://github.com/platformsh/config-reader-java), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Gradle](https://gradle.org/)
* [Spring-Boot](https://spring.io/projects/spring-boot)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
