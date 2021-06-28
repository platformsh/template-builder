# Jenkins for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/jenkins/.platform.template.yaml&utm_content=jenkins&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This project provides a starter kit for Jenkins projects hosted on Platform.sh.  The Jenkins `.war` file is downloaded during the build hook and not included in the repository.

Jenkins is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery.

## Features

* Java 11
* Automatic TLS certificates
* Jenkins downloaded on the fly during build

## Post-install

After the deployment has finished, you will need to log into the Jenkins admin dashboard, where an administrator user has already been created (`admin`). To retrieve the initial password, you can use the CLI command `platform ssh -p PROJECT_ID cat /app/.jenkins/secrets/initialAdminPassword`.

## Customizations

The following files and additions make the Jenkins work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [`.platform/routes.yaml`](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [`.platform/services.yaml`](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [`.platform.app.yaml`](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).

## References

* [Maven](https://maven.apache.org/)
* [Jenkins](https://jenkins.io/)
* [Java at Platform.sh](https://docs.platform.sh/languages/java.html)
