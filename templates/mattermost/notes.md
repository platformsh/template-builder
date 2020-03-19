# Hardcoded service credentials

For now, PostgreSQL and Elasticsearch credentials are hardcoded in `.environment`, which overrides Mattermost's default settings in `/app/config/config.json`. This is obviously, not ideal.

My plan was to use `jq` to update these credentials, but I was not successful as of yet.

```
DATABASE_REL=database
DBUSERNAME=$( echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq .$DATABASE_REL[0].username ))
DB_PASSWORD=$( echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq .$DATABASE_REL[0].password | echo $(read s; echo ${s//\"} ))
DB_PATH=$( echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq .$DATABASE_REL[0].path | echo $(read s; echo ${s//\"} ))
DB_HOST=$( echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq .$DATABASE_REL[0].host | echo $(read s; echo ${s//\"} ))
DB_PORT=$( echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq .$DATABASE_REL[0].port | echo $(read s; echo ${s//\"} ))

export MM_SQLSETTINGS_DATASOURCE=$(echo \"${MM_SQLSETTINGS_DRIVERNAME//\"}://$DB_USERNAME:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_PATH?sslmode=disable&connect_timeout=10\")
```

The goal here would be to figure out why `.environment` files are having trouble handling `PLATFORM_RELATIONSHIPS`, despite the fact that our docs make it seem that this file is not regarded until post-build.

related: https://platformsh.slack.com/archives/CEDK8KCSC/p1584569822222200

# Working from binaries

This was a rather quick turn-around, and we would probably be better off building from source. At the moment, users can specify a new version in `setup.sh` that is installed in the build hook, giving the zipped binaries. 

# Template-builder independent updates via source operations

Part of Ori's original work wanted to be able to call an `update.sh` script via source operations. It has not been included here as of yet.

```
#!/usr/bin/env bash

echo $MATTERMOST_VERSION
#if [ -z "$MATTERMOST_VERSION" ] ; then
  mkdir -p _update
  cd _update
  if [ ! -f "mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz" ]; then
    wget https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz;
  fi
  tar xzf mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz;
  rm -rf ../ENTERPRISE-EDITION-LICENSE.txt  ../NOTICE.txt  ../README.md  ../bin  ../client  ../fonts  ../i18n  ../logs  ../prepackaged_plugins  ../templates
  cp -Rf mattermost/* ../
#else
#    echo "Required environment variable MATTERMOST_VERSION have not been set. Update can not proceed." 1>&2
#    exit 1
#fi
```
