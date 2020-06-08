#!/bin/bash

unset NPM_CONFIG_PREFIX
export NVM_DIR="$PLATFORM_APP_DIR/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm use $NODE_VERSION
if [ ! -f install/platform.installed ]; then
    # Copy the public files into a writeable directory before running the migration
    # on the initial install. After the first deploy this can be put off to post_deploy.
    rsync -avq --update --ignore-errors _public/ public/

    # The DB migrate must run before asset precompilation, because asset compilation requires
    # the database to be already setup.
    bundle exec rake db:migrate -q

    # Asset compilation needs to happen before the site runs on the first install,
    # but can be delayed to post_deploy thereafter.
    bundle exec rake assets:precompile -q

    touch install/platform.installed
else
    # After the first install, always run any outstanding migrations before the site
    # reopens so it has exclusive DB access.
    bundle exec rake db:migrate -q
fi
