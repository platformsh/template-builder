#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# Because Platform.sh associates branches with active environments, and because we want the relationship between 
#   frontend and backend app containers to translate across environments, we need to clear our settings occasionally. 
#   This script runs ONLY when the first commit/deployment event occurs on a newly created development environment.
#
########################################################################################################################
PROD_HAS_BEEN_INSTALLED=$1
CURRENT_ENV_SETTINGS=$2

printf "* Preparing Drupal for NextJS consumer.\n"
printf "    ✔ Production installed: $PROD_HAS_BEEN_INSTALLED\n"
printf "    ✔ Current env settings: $CURRENT_ENV_SETTINGS\n"
printf "    ✔ Current environment: $PLATFORM_BRANCH\n"

if [ "$PROD_HAS_BEEN_INSTALLED" = false ]; then
    # Skip reset if this is the project's first deploy.
    printf "* Fresh project detected. Skipping reset.\n"
else
    # Delete entities configured for the parent environment.
    printf "* New environment detected.\n"
    printf "    ✔ Deleting parent environment's configuration\n"
    drush -q entity:delete consumer
    drush -q entity:delete next_site
    drush -q entity:delete next_entity_type_config
fi
printf "* Configuring the current environment.\n"
