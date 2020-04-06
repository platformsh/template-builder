# Nextcloud for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/nextcloud/.platform.template.yaml&utm_content=nextcloud&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds Nextcloud on Platform.sh.

Nextcloud is a PHP-based groupware server with installable apps, file synchronization, and federated storage.

## Services

* PHP 7.4
* MariaDB 10.4
* Redis 5.0

## Post-installation

On first deploy, Nextcloud will be installed automatically.  The administrative user will be created for you.  The username and password will be shown in the deploy log and allow you to login the first time.

*Please remember to change the password immediately after logging in.*

You should also set an email address for the administrative user after logging in.

## Customizations

The following changes have been made relative to Nextcloud as it is downloaded from the Nextcloud website.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* Nextcloud itself is downloaded on the fly into the `src` directory during the build step by the `download-nextcloud.sh` script.  It leverages the build cache to avoid redownloading the application each time.
* The `install.sh` script is used for the initial installation of Nextcloud on the first deploy.  It is not needed afterward unless you want to reinitialize the installation.  (Note: "reinitialize" means "delete all data and start over".  This is a destructive operation with no rollback option.)  You may delete it if you wish.
* The `nukedb.sql` file is used to wipe the SQL database.  It is used as part of `install.sh`.  Do not use it yourself unless you want to lose all of your data.  You may delete it if you wish.
* There is a symlink `occ` in the project root that points to the `src/occ` file.  It allows you to run `occ` commands from the project root once deployed.
* The `update.sh` script will read a desired Nextcloud version from a project variable and use that to download that version of Nextcloud and replace the code in `src` with it.  You can then commit and push the changes.  This is the preferred way to update your version of Nextcloud.  (The built-in self-updater will not work.)
* The `_apps` and `_themes` directories are for you to add Nextcloud apps and themes you wish to have installed.  They will be copied into the `src/apps` and `src/themes` directories, respectively, during the build process.  (The built-in app downoader will not work.)

## Installing applications

Nextcloud features an in-application app store and app updating functionality.  Those features require a writeable disk at runtime, while Platform.sh offers only a read-only disk for security reasons.

Instead, applications can be installed via Git.

1. Locate an application  you wish to install on the [Nextcloud Apps](https://apps.nextcloud.com/) site.
2. Download the latest version for the appropriate verison of Nextcloud.
3. Unpack the downloaded `tgz` file into the `_apps` directory of your project.

As part of the build process, applications and themes will be copied from the `_apps` and `_themes` directories to the appropriate directories in the codebase.  (The code to do so is in the `hooks.build` section of `.platform.app.yaml`.)  They can then be enabled through the Nextcloud UI as normal.

This separate setup allows the `update.sh` script to update Nextcloud itself without losing the code for any extensions you have added.

## Using Amazon S3 for storage

Nextcloud supports using Amazon S3 (or any S3 compatible storage service) for the primary data backend.  That allows you to use the far cheaper S3 storage, but *all environments on Platform.sh will connect to the same S3 bucket and thus be working with live data*.  There may also be a performance impact, which will vary depending on the type of data you're storing.

Nextcloud also must be configured for S3 at the time of installation.  That means you cannot use the one-click install button above as it will run through the installation process before you have a chance to provide S3 credentials.  Instead, follow these steps:

1. Create a new empty Platform.sh project through the UI; when asked if you want to create a "New Project" or "Use a template", select "New Project".

2. Create an Amazon S3 bucket and user that has write access to it.  You will need a number of pieces of information, which you must set on the newly created project as project-level variables.  The easiest way to do so is from the command line:

    ```bash
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --name="env:S3_BUCKET"   --value=$S3_BUCKET
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true  --level=project --name="env:S3_KEY"      --value=$S3_KEY
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true  --level=project --name="env:S3_SECRET"   --value=$S3_SECRET
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --name="env:S3_REGION"   --value=$S3_REGION
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --name="env:S3_HOSTNAME" --value=$S3_HOSTNAME
    ```

Where `$PROJECT_ID` is the ID of the Platform.sh project you just created, and `$S3_BUCKET`, `$S3_KEY`, `$S3_SECRET`, `$S3_REGION`, and `$S3_HOSTNAME` are the appropriate values for the S3 bucket you wish to use.

3. (Optional) If you would like to specify the name and password for the admin user up front, you may also set that.  You will be able to change these later after logging in, and should remove these variables once the project is installed.  If you do not specify a name and password they will be auto-created for you, and available in the deploy log output.

    ```bash
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --name="env:ADMIN_USER" --value=$ADMIN_USER
    platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true  --level=project --name="env:ADMIN_PASSWORD" --value=$ADMIN_PASSWORD
    ```

4. Initialize the code from this GitHub repository.  That can be done directly with:

    ```bash
    platform environment:init -p $PROJECT_ID -e master https://github.com/platformsh-templates/nextcloud
    ```

That will initialize the project with the code from this template and deploy it, which will trigger the installer.  The default configuration file will detect that you have S3 parameters already defined and use those in the initial configuration of the site.

5. Go to your site in a browser and login with the user and password you specified above, or the user and password shown in the shell output from the previous command.  Your Nextcloud site is now ready to use.

*Please remember to change your admin password immediately.*

## References

* [Nextcloud](https://nextcloud.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
