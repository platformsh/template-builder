#!/bin/bash

unset NPM_CONFIG_PREFIX
export NVM_DIR="$PLATFORM_APP_DIR/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm use $NODE_VERSION
if [ ! -f install/platform.installed ]; then
    # Copy the public files into a writeable directory before running the migration
    # on the initial install. After the first deploy this can be put off to post_deploy.
    rsync -avq --update --ignore-errors _public/ public/
    touch install/platform.installed
fi
bundle exec rake db:migrate
