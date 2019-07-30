# KumuluzEE for Platform.sh

This project provides a starter kit for KumuluzEE Eclipse MicroProfile projects hosted on Platform.sh.

KumuluzEE is a lightweight framework for developing microservices using standard Java, Java EE / Jakarta EE technologies and migrating existing Java applications to microservices. KumuluzEE packages microservices as standalone JARs. KumuluzEE microservices are lightweight and optimized for size and start-up time. 

## Services

* Java 8

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).
* An additional library dependency, [`platformsh/config-reader-java`](https://github.com/platformsh/config-reader-java), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Maven](https://maven.apache.org/)
* [KumuluzEE](https://ee.kumuluz.com/)
* [Eclipse MicroProfile](https://microprofile.io/) 
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
