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

## Auto-updates

Below shows the templates currently included in the auto-update workflow, which runs every 3 days.

- [ ] akeneo
- [ ] aspnet-core
- [ ] backdrop
- [ ] beego
- [ ] directus
- [ ] django2
- [ ] django3
- [ ] django4
- [ ] drupal8
- [ ] drupal8-govcms8
- [ ] drupal8-multisite
- [ ] drupal8-opigno
- [ ] drupal9
- [ ] echo
- [ ] elastic-apm
- [ ] eleventy-strapi
- [ ] express
- [ ] flask
- [ ] gatsby
- [ ] gatsby-drupal
- [ ] gatsby-strapi
- [ ] gatsby-wordpress
- [ ] gin
- [ ] golang
- [ ] hugo
- [ ] jenkins
- [ ] jetty
- [ ] koa
- [ ] laravel
- [ ] lisp
- [ ] magento2ce
- [ ] mattermost
- [ ] meilisearch
- [ ] micronaut
- [ ] microprofile-helidon
- [ ] microprofile-kumuluzee
- [ ] microprofile-openliberty
- [ ] microprofile-payara
- [ ] microprofile-thorntail
- [ ] microprofile-tomee
- [ ] microprofile-wildfly
- [ ] nextcloud
- [ ] nextjs
- [ ] nodejs
- [ ] nuxtjs
- [ ] pelican
- [ ] php
- [ ] pimcore
- [ ] probot
- [ ] pyramid
- [ ] python3
- [ ] python3-uwsgi
- [ ] quarkus
- [ ] rails
- [ ] sculpin
- [ ] spring-boot-gradle-mysql
- [ ] spring-boot-maven-mysql
- [ ] spring-kotlin
- [ ] spring-mvc-maven-mongodb
- [ ] strapi
- [ ] strapi4
- [ ] tomcat
- [ ] typo3
- [ ] wagtail
- [ ] wordpress-bedrock
- [ ] wordpress-composer
- [ ] wordpress-vanilla
- [ ] wordpress-woocommerce
- [ ] xwiki