# Apache TomEE MicroProfile for Platform.sh

This project provides a starter kit for Apache TomEE Eclipse MicroProfile projects hosted on [Platform.sh](http://platform.sh).

Apache TomEE is the Eclipse MicroProfile flavor that uses several Apache Project flavors such as Apache Tomcat, Apache OpenWebBeans and so on.

## Services

* Java 8

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).
* [`pom.xml`](pom.xml) A Project Object Model or POM is the fundamental unit of work in Maven. It is an XML file that contains information about the project and configuration details used by Maven to build the project. It contains default values for most projects.
* An additional library dependency, [`platformsh/config-reader-java`](https://github.com/platformsh/config-reader-java), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Maven](https://maven.apache.org/)
* [Apache TomEE](https://tomee.apache.org/)
* [Eclipse MicroProfile](https://microprofile.io/) 
* [Platform Documentation](https://docs.platform.sh/)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
