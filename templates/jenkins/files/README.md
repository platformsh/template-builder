# Jenkins for Platform.sh

This project provides a starter kit for Jenkins projects hosted on [Platform.sh](http://platform.sh).

Jenkins is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery.

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).

## Services

* Java 8

## References

* [Maven](https://maven.apache.org/)
* [Jenkins](https://jenkins.io/) 
* [Platform Documentation](https://docs.platform.sh/)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
