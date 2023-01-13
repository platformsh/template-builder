#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# This script configures the Next.js site associated with the current environment's OAuth consumer, and configures a 
#   site resolver for previews.
#
########################################################################################################################
# 1. Create the site.
printf "    ✔ Creating the NextJS site entity (see https://next-drupal.org/learn/quick-start/create-nextjs-site).\n"

#   a. Use the Platform.sh built-in variable PLATFORM_ENVIRONMENT for the preview secret, and track it.
SITE_PREVIEW_SECRET=$PLATFORM_ENVIRONMENT
UPDATED_DATA=$(jq --arg SITE_PREVIEW_SECRET "$SITE_PREVIEW_SECRET" '.environment.site.preview_secret = $SITE_PREVIEW_SECRET' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS

#   b. Grab the frontend URL defined in .environment to track base, preview, and image_domain urls.
DRUPAL_ENVIRONMENT=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id == "api") | .key')
SITE_BASE_URL=${DRUPAL_ENVIRONMENT%/}
UPDATED_DATA=$(jq --arg SITE_BASE_URL "$SITE_BASE_URL" '.environment.site.url.base = $SITE_BASE_URL' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS
IMAGE_DOMAIN="${SITE_BASE_URL:8}"
UPDATED_DATA=$(jq --arg IMAGE_DOMAIN "$IMAGE_DOMAIN" '.environment.site.url.image_domain = $IMAGE_DOMAIN' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS
NEXTJS_ENVIRONMENT=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id == "client") | .key')
SITE_BASE_URL=${NEXTJS_ENVIRONMENT%/}
SITE_PREVIEW_URL=$SITE_BASE_URL/api/preview
UPDATED_DATA=$(jq --arg SITE_PREVIEW_URL "$SITE_PREVIEW_URL" '.environment.site.url.preview = $SITE_PREVIEW_URL' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS

#   c. Pull out other related settings.
SITE_ID=$(cat $ENV_SETTINGS | jq -r '.environment.site.id')
SITE_LABEL=$(cat $ENV_SETTINGS | jq -r '.environment.site.label')
printf "        * id: $SITE_ID\n"
printf "        * label: $SITE_LABEL\n"
printf "        * base_url: $SITE_BASE_URL\n"
printf "        * preview_url: $SITE_PREVIEW_URL\n"
printf "        * preview_secret: $SITE_PREVIEW_SECRET\n"

#   d. Create the site.
drush scr $DRUPAL_SETUP/environment/03-create-site.php "$SITE_ID" "$SITE_LABEL" "$SITE_BASE_URL" "$SITE_PREVIEW_URL" "$SITE_PREVIEW_SECRET"  

# 2. Configure previews.
printf "    ✔ Configuring previews (see https://next-drupal.org/learn/quick-start/configure-content-types).\n"
PREVIEW_ID=$(cat $ENV_SETTINGS | jq -r '.environment.site.resolver.id')
PREVIEW_RESOLVER=$(cat $ENV_SETTINGS | jq -r '.environment.site.resolver.type')
printf "        * site: $SITE_ID\n"
printf "        * id: $PREVIEW_ID\n"
printf "        * site_resolver: $PREVIEW_RESOLVER\n"
drush scr $DRUPAL_SETUP/environment/03-configure-previews.php "$PREVIEW_ID" "$PREVIEW_RESOLVER" "$SITE_ID"
