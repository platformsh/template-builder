# Spring Boot Maven template for Platform.sh

This project provides a starter kit for Spring Boot Maven with MySQL projects hosted on [Platform.sh](http://platform.sh).

We include recommended .platform.app.yaml and .platform files that should suffice for most use cases. You are free to tweak them as needed for your particular site.

## Platform.sh configuration files

* [.platform/routes.yaml](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [.platform/services.yaml](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [.platform.app.yaml](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).

## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Maven](https://maven.apache.org/)
* [Spring-Boot](https://spring.io/projects/spring-boot) 
* [Platform Documentation](https://docs.platform.sh/)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
