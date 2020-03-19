# Nextcloud for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextcloud/.platform.template.yaml&utm_content=nextcloud&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Nextcloud on Platform.sh.

Nextcloud is a PHP-based groupware server with installable apps, file synchronization, and federated storage.

## Services

* PHP 7.3
* MariaDB 10.4
* Redis 5.0

## Post-installation

On first deploy, Nextcloud will be installed automatically.  The administrative user will be created for you.  The username and password will be shown in the deploy log and allow you to login the first time.

*Please remember to change the password immediately after logging in.*

You should also set an email address for the administrative user after logging in.

## Customizations

The following changes have been made relative to Nextcloud as it is downloaded from the Nextcloud website.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* Nextcloud itself is installed in the `src` directory, as downloaded from Nextcloud.org.
* The `install.sh` script is used for the initial installation of Nextcloud on the first deploy.  It is not needed afterward unless you want to reinitialize the installation.  (Note: "reinitialize" means "delete all data and start over".  This is a destructive operation with no rollback option.)  You may delete it if you wish.
* The `nukedb.sql` file is used to wipe the SQL database.  It is used as part of `install.sh`.  Do not use it yourself unless you want to lose all of your data.  You may delete it if you wish.
* There is a symlink `occ` in the project root that points to the `src/occ` file.  It allows you to run `occ` commands from the project root once deployed.
* The `update.sh` script will read a desired Nextcloud version from a project variable and use that to download that version of Nextcloud and replace the code in `src` with it.  You can then commit and push the changes.  This is the preferred way to update your version of Nextcloud.  (The built-in self-updater will not work.)
* The `_apps` and `_themes` directories are for you to add Nextcloud apps and themes you wish to have installed.  They will be copied into the `src/apps` and `src/themes` directories, respectively, during the build process.  (The built-in app downoader will not work.)


## References

* [Nextcloud](https://nextcloud.org/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
