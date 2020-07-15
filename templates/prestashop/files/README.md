# Prestashop for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/prestashop/.platform.template.yaml&utm_content=prestashop&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template demonstrates building a Spring Boot application. It uses Gradle to build the application and deploy it to Platform.sh.

This template builds Prestashop project.  It is pre-configured to use MariaDB.

PrestaShop is a freemium, open source e-commerce solution. The software is published under the Open Software License. It is written in the PHP programming language with support for the MySQL database management system. PrestaShop is currently used by 300,000 shops worldwide and is available in 60 different languages.


## Features

* PHP 7.4
* MariaDB 10.4
* Automatic TLS certificates

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* [.platform/routes.yaml](.platform/routes.yaml): Platform.sh allows you to define the [routes](https://docs.platform.sh/configuration/routes.html).
* [.platform/services.yaml](.platform/services.yaml):  Platform.sh allows you to completely define and configure the topology and [services you want to use on your project](https://docs.platform.sh/configuration/services.html).
* [.platform.app.yaml](.platform.app.yaml): You control your application and the way it will be built and deployed on Platform.sh [via a single configuration file](https://docs.platform.sh/configuration/app-containers.html).


## References

* [Platform.sh post](https://platform.sh/blog/2019/java-hello-world-at-platform.sh/)
* [Prestashop](https://www.prestashop.com/en)
* [PHP at Platform.sh](https://docs.platform.sh/languages/php.html)

## How to install

1. Clone this repository
2. Create a new platform.sh project

```
platform project:create
```

3. Add specific environment variables

```
platform -p<project> variable:set ADMIN_EMAIL your@email.com
platform -p<project> variable:set ADMIN_PASSWORD yourpassword
```

4. Push to platform.sh

```
git remote add platform <project id>@git.<project region>.platform.sh:<project id>.git
git push platform master
```

5. Backend

You can access your backend at `/admin-fwp` with the credentials that you defined as variables.
