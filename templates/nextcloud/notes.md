# NextCloud  Platform.sh template

This template should create a fully functional nextcloud instance.

## TODO

1. We still need to figure-out a clean rewrite rule.
2. Figure-out logging

## Provisioning:

### Barebones

Just create a project from the template. It will generate an admin user and print-out the username and password in the deploy hook output.

### Full featured with S3 support and admin/user

1. When we create the project (on a provisioning machine / CI):

We need to setup enviroment variables:
```
S3_BUCKET my_bucket_name_
S3_KEY im_key
S3_SECRET im_sercret_key
S3_HOSTNAME s3_hostname
S3_REGION S3_region
ADMIN_USER help@example.com
ADMIN_PASSWORD Iam_A_Str0ng_PassW0rd
NEXTCLOUD_USER user@example.com
NEXTCLOUD_PASSWORD Iam_A_Str0ng_Us3r_PassW0rd
NEXTCLOUD_QUOTA 100MB
```

2. And automated project creation as follows:

```
PROJECT_ID=$(platform project:create --title="OVH-NextCloud-Instance" --region="eu-4" --plan="standard" --no-set-remote --yes)
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=S3_BUCKET --value=$S3_BUCKET
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true --level=project --prefix=env: --name=S3_KEY --value=$S3_KEY
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true --level=project --prefix=env: --name=S3_SECRET --value=$S3_SECRET
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=S3_HOSTNAME --value=$S3_HOSTNAME
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=S3_REGION --value=$S3_REGION
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=ADMIN_USER --value=$ADMIN_USER
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true --level=project --prefix=env: --name=ADMIN_PASSWORD --value=$ADMIN_PASSWORD
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=NEXTCLOUD_USER --value=$NEXTCLOUD_USER
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=true --level=project --prefix=env: --name=NEXTCLOUD_PASSWORD --value=$NEXTCLOUD_PASSWORD
platform -p $PROJECT_ID -q variable:create --json=false --sensitive=false --level=project --prefix=env: --name=NEXTCLOUD_QUOTA --value=$NEXTCLOUD_QUOTA
platform environment:init -p $PROJECT_ID -e master https://github.com/platformsh_templates/nextcloud
```

## Updating Nextcloud

### Locally
* Open `update.sh` and set the version in an environment variable, for example `NEXTCLOUD_VERSION=18.0.1`
* Run `update.sh` it will download and overwrite the existing source. Possibly check nothing changed much in the config. Commit and push. It should upgrade itself.

### On  Platform.sh using the API

#### Update checker

Prints-out the latest available release

> make sure you have `pup` and `jq` installed (`go get github.com/ericchiang/pup`)

```
echo "Current: $(curl -L $(platform url -p $PROJECT_ID -e master -1 --pipe)/status.php  2>/dev/null | jq .version)"
echo "Available: $(curl -s https://download.nextcloud.com/server/releases/ | pup 'table tr:nth-last-child(6) td a attr{href}')"

```
Output:
```
Current: "18.0.1.3"
Available: nextcloud-18.0.1.zip
```

#### Update
```
 # create a branch for updates
platform -p $PROJECT_ID branch update
 # call the source-code update API
platform -p $PROJECT_ID -e update source-operation:run update --variable env:NEXTCLOUD_VERSION=18.0.1
 # check that the installation is functional before we merge
NEXTCLOUD_RUNNING=$(curl -L $(platform url -1 --pipe)/status.php  2>/dev/null | jq .installed) 
if [ "$NEXTCLOUD_RUNNING" = true ] ; then
    platform -p $PROJECT_ID merge update
fi
```

### Extra applications: Preview Generator
We add the previewgenerator app and a cron for it to get better performance and less memory utilisation on requests. It is worth noting it does not support installations that have encryption turned on. So this will need to be a decision point.
It is added to _apps and copied over in the build hook.

wget https://github.com/rullzer/previewgenerator/releases/download/v2.2.0/previewgenerator.tar.gz

