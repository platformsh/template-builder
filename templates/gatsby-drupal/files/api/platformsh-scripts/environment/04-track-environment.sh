#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# This script tracks settings that have changed related to the the Next.js-Drupal connection for a particular 
#   environment on Platform.sh. Throughout setup, plenty has been updated to ensure that for any given environment, 
#   a unique Next.js app container connects with its own unique Drupal container, and that this relationship is seemless
#   across branching commits as well as local development work. 
#
# Here, a few last minute things are updated:
#   1) The current frontend URL is updated for the environment. 
#   2) If this is the project's first every push, successful installation is logged.
#   3) Next.js, both on Platform.sh and locally, relies on environment variables typically included in a .env file. 
#       Rather than forcing the Next.js container to build this file, Drupal is considered to be the source of truth and
#       assumes that responsibility here. This script pulls everything Next.js needs from our settings file we've been
#       using to track the environment, and generates the required file in a Network Storage mount that Next.js can access.
#       For now, this approach seemed best, as it gives a readily accessible environment file for switching out a variety
#       of frontend consumers simply by defining a mount. This may change, but seemed like the best option currently. 
#
########################################################################################################################
SPLIT_LINE="-------------------------------------------------------------------------------------------------------------"
# 1. Track the latest changes to the environment.

# a. Get the current environment's frontend url from its id ('client').
printf "    ✔ Logging frontend configuration.\n"
FRONTEND=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id == "client") | .key')
FRONTEND_URL=${FRONTEND%/}
UPDATED_DATA=$(jq --arg FRONTEND_URL "$FRONTEND_URL" '.environment.client.url.base = $FRONTEND_URL' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS
PREVIEW_URL=$FRONTEND_URL/api/preview
UPDATED_DATA=$(jq --arg PREVIEW_URL "$PREVIEW_URL" '.environment.client.url.preview = $PREVIEW_URL' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS

# b. Track the overall installation. 
if [[ "$PLATFORM_ENVIRONMENT_TYPE" == "production" ]]; then
    printf "    ✔ Logging production installation\n"
    SETTINGS_UPDATES=$(jq '.project.production.installed = true' $ENV_SETTINGS)
    echo $SETTINGS_UPDATES > $ENV_SETTINGS
fi

# 2. Generate the .env files that will be needed on Platform.sh environments and local development.

# a. Organize everything we need.
printf "* Preparing credentials to hand off to frontend container.\n"
NEXT_PUBLIC_DRUPAL_BASE_URL=$(cat $ENV_SETTINGS | jq -r '.environment.site.url.base')
NEXT_IMAGE_DOMAIN=$(cat $ENV_SETTINGS | jq -r '.environment.site.url.image_domain')
DRUPAL_SITE_ID=$(cat $ENV_SETTINGS | jq -r '.environment.site.id')
DRUPAL_FRONT_PAGE=$(cat $ENV_SETTINGS | jq -r '.environment.site.front_page')
DRUPAL_PREVIEW_SECRET=$(cat $ENV_SETTINGS | jq -r '.environment.site.preview_secret')
DRUPAL_CLIENT_ID=$(cat $ENV_SETTINGS | jq -r '.environment.consumer.uid')
DRUPAL_CLIENT_SECRET=$(cat $ENV_SETTINGS | jq -r '.environment.consumer.secret')

# b. Create the .env file used for local development.
printf "* Writing local configuration.\n"
printf "# This .environment file is generated programmatically within the backend Drupal app for each Platform.sh
# environment and stored within an network storage mount so it can be used locally.

NEXT_PUBLIC_DRUPAL_BASE_URL=$NEXT_PUBLIC_DRUPAL_BASE_URL
NEXT_IMAGE_DOMAIN=$NEXT_IMAGE_DOMAIN
DRUPAL_SITE_ID=$DRUPAL_SITE_ID
DRUPAL_FRONT_PAGE=$DRUPAL_FRONT_PAGE
DRUPAL_PREVIEW_SECRET=$DRUPAL_PREVIEW_SECRET
DRUPAL_CLIENT_ID=$DRUPAL_CLIENT_ID
DRUPAL_CLIENT_SECRET=$DRUPAL_CLIENT_SECRET
" > $VARS_LOCAL
echo $SPLIT_LINE
printf "$(cat $VARS_LOCAL)\n"
echo $SPLIT_LINE

# c. Create the .environment file the Platform.sh environment will use.
printf "* Writing remote configuration.\n"
printf "# This .env file is generated programmatically within the backend Drupal app for each Platform.sh environment
# and stored within an network storage mount so it can be shared between apps.

export NEXT_PUBLIC_DRUPAL_BASE_URL=$NEXT_PUBLIC_DRUPAL_BASE_URL
export NEXT_IMAGE_DOMAIN=$NEXT_IMAGE_DOMAIN
export DRUPAL_SITE_ID=$DRUPAL_SITE_ID
export DRUPAL_FRONT_PAGE=$DRUPAL_FRONT_PAGE
export DRUPAL_PREVIEW_SECRET=$DRUPAL_PREVIEW_SECRET
export DRUPAL_CLIENT_ID=$DRUPAL_CLIENT_ID
export DRUPAL_CLIENT_SECRET=$DRUPAL_CLIENT_SECRET
" > $VARS_PSH
echo $SPLIT_LINE
printf "$(cat $VARS_PSH)\n"
echo $SPLIT_LINE
