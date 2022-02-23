# Template Builder notes

This file contains more detailed information about the way `template-builder` functions when defining templates as a `project` - that is, a `BaseProject` or `RemoteProject`. For example, multiple template projects will deviate from how the `update` task is used that is better noted here than written on each of their project scripts. 

## Yarn

### Overwriting `updateCommands`

> **Relevant to:**
> 
> * Gatsby ([`project/gatsby.py`](project/gatsby.py))
> * Next.js ([`project/nextjs.py`](project/nextjs.py))
> * Strapi ([`project/strapi.py`](project/strapi.py))

The `BaseProject` `update` task will [loop through a list of `updateCommands`](project/__init__.py) for a number of different package managers and run them if their respective depedency files (i.e. `package.json`) are present. 

Node.js has two popular package mangers - npm and Yarn. Both use `package.json` to define dependencies, but resolve to different lock files (`package-lock.json` & `yarn.lock`). When deployed, we'll only be using one of them, and it's generally recommended to not have lock files from both package managers present in the same repo. 

Because `update` loops through `updateCommands`, simply adding an upgrade command for Yarn to `BaseProject` would result in that exact situation we'd like to avoid: both `npm update` and `yarn upgrade` will be run, resulting in two lock files. So, `updateCommands` is redefined here for a few templates to prioritize Yarn and avoid it altogether:

```py
from . import BaseProject

class Template(BaseProject):

    updateCommands = {
        'package.json': 'yarn upgrade'
    }
```

## New templates

- [ ] sylius
- [ ] fastapi
- [ ] prefect.io
- [ ] sulu
- [ ] next-drupal

## Auto-updates

Below shows the templates currently included in the auto-update workflow, which runs every 3 days.

1. nodejs
1. wordpress-composer
1. meilisearch
1. drupal9
1. django2
1. nextcloud
1. gatsby
1. strapi4
1. flask
1. php
1. django3
1. python3
1. python3-uwsgi
1. pyramid
1. rails
1. hugo
1. backdrop
1. gin
1. beego
1. pelican
1. nextjs
1. koa
1. django4
1. express
1. echo
1. golang
1. mattermost
1. wagtail
1. strapi
1. wordpress-bedrock
1. wordpress-woocommerce
1. nuxtjs
1. lisp

Below are those templates that will still need to be integrated.

---

- **Left (excluding multi-app)**: 11
- **Left (including multi-app)**: 16
- **Left (all, including Java, .NET Core, & Lisp)**: 35

---

- Node.js (1)
    1. directus
    1. probot
- PHP
    - Drupal 8 (4)
        1. drupal8
        1. drupal8-govcms8
        1. drupal8-multisite
        1. drupal8-opigno
    - WordPress (1)
        1. wordpress-vanilla (EU-3 issue)
    - Other (6)
        1. akeneo
        1. laravel
        1. typo3
        1. magento2ce
        1. pimcore
        1. sculpin
- Multi-apps (5)
    1. elastic-apm
    1. eleventy-strapi
    1. gatsby-drupal
    1. gatsby-strapi
    1. gatsby-wordpress

Below have lower priority, or no clear auto-update path as of yet.

- .NET Core
    1. aspnet-core
- Java
    1. jenkins
    1. jetty
    1. micronaut
    1. microprofile-helidon
    1. microprofile-kumuluzee
    1. microprofile-openliberty
    1. microprofile-payara
    1. microprofile-thorntail
    1. microprofile-tomee
    1. microprofile-wildfly
    1. quarkus
    1. spring-boot-gradle-mysql
    1. spring-boot-maven-mysql
    1. spring-kotlin
    1. spring-mvc-maven-mongodb
    1. tomcat
    1. xwiki
