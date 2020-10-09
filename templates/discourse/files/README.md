# Discourse for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/discourse/.platform.template.yaml&utm_content=discourse&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Discourse on Platform.sh.  Note that it does require some post-install setup.

Discourse is a community forum application built in Ruby.

## Services

* Ruby 2.6
* PostgreSQL 9.6
* Redis 5
* Network storage

## Post-install steps

Discourse requires certain information to be added as custom environment variables before it can run its own installer.  This information cannot be injected by the Platform.sh setup process and so requires manual steps.

### Option 1: Create admin account on the CLI

Once the site is deployed, login via SSH (either with `platform ssh` or using the command provided in the `SSH` dropdown in the Web Console).  You may then create the administrator account interactively with the command:

```bash
rake admin:create
```

That command will prompt you for the administrator username or password.  When asked if you want the account to have Admin privileges, say `Yes`.  Once complete you will be able to login and configure the site using the information you provided.

### Option 2: Create admin account through the web interface

In order to use the Discourse web interface to create the administrator, you must provide a whitelist of allowed email addresses that may do so.  In virtually every case you need only one.

Run the following command to set a "developer email" address, replacing the email given with your own email.  It must be an address capable of receiving messages.

```bash
platform vset -e master env:DISCOURSE_DEVELOPER_EMAILS myemail@example.com
```

If you do not have a checkout of your project, you will need to also include the project ID, e.g., `-p abc12345`.

Once the site redeploys, visit it in a web browser.  You will be prompted to register the administrator user, using the email address you just provided.  Enter your desired username and password and the site will email you a confirmation.  You can then login and begin configuring your site.

## Customizations

The following changes have been made relative to Discourse project downloaded from Discourse.org.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `build.sh` and `deploy.sh` scripts are called from `.platform.app.yaml`.  See the inline comments for an explanation of the steps they take.  You may edit these files if you wish, but be aware that changing the existing code may result in Discourse failing to build or deploy.
* The `.environment` file sets necessary environment variables for Discourse that cannot be pre-set in the `.platform.app.yaml` file.  You may add to this file if you wish.
* The file `config/discourse.platformsh.conf` is copied over the `discourse.conf` file from Discourse during build.  It contains modifications to pull most configuration from the Platform.sh environment.
* The `_bin` directory includes a number of additional shell utilities required by Discourse's file compression system that are not normally installed on Platform.sh.  It is added to the path by `.environment`.  Do not remove these files.

## References

* [Discourse](https://www.discourse.org/)
* [Ruby on Rails](https://rubyonrails.org/)
* [Ruby on Platform.sh](https://docs.platform.sh/languages/ruby.html)
