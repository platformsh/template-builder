#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# The demos settings file contains an array of modules that need to be enabled to make the Next.js+Drupal connection
#   work, which are outlined in https://next-drupal.org/learn/quick-start/enable-modules.
#
########################################################################################################################
printf "    ✔ Enabing modules (see https://next-drupal.org/learn/quick-start/enable-modules).\n"

# 1. Get the modules.
MODULES=$(cat $ENV_SETTINGS | jq -r '.project.modules | join(" ")')
for row in $(cat $ENV_SETTINGS | jq -r '.project.modules [] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode
    }
printf "        * $(_jq '.')\n"
done 

# 2. Enable them.
drush -q pm:enable $MODULES -y

# 3. Configure Gatsby w/ Recommended settings.
# JSON API
drush -q config:set jsonapi_extras.settings include_count true -y
# Gatsby
drush -q config:set --input-format=yaml gatsby.settings supported_entity_types [node]

# These have to be updated on every new environment.
drush -q config:set gatsby.settings server_url https://pr-15-jheso3q-rurwlw7e4kjz2.eu-2.platformsh.site -y
drush -q config:set gatsby.settings preview_callback_url https://pr-15-jheso3q-rurwlw7e4kjz2.eu-2.platformsh.site/__refresh -y  
# Figure out how to trigger incremental builds, and use localhost:8000 for the above setting.
drush -q config:set gatsby.settings preview_target https://pr-15-jheso3q-rurwlw7e4kjz2.eu-2.platformsh.site -y
drush -q config:set gatsby.settings incrementalbuild_url https://pr-15-jheso3q-rurwlw7e4kjz2.eu-2.platformsh.site/__refresh -y
drush -q config:set gatsby.settings contentsync_url https://pr-15-jheso3q-rurwlw7e4kjz2.eu-2.platformsh.site/__refresh -y
