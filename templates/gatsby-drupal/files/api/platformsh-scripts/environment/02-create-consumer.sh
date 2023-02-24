#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# This script actually creates the OAuth consumer that will be used for the current environment.
#
########################################################################################################################
# 1. Generate keys, and update simple oauth settings.
KEY_LOCATION=$(cat $ENV_SETTINGS | jq -r '.environment.key_path')
printf "    ✔ Generating keys (see https://next-drupal.org/learn/quick-start/create-consumer).\n"
printf "        * location: $KEY_LOCATION\n"
printf "        * public_key: $KEY_LOCATION/public.key\n"
printf "        * private_key: $KEY_LOCATION/private.key\n"
drush -q simple-oauth:generate-keys $KEY_LOCATION
drush -q config:set simple_oauth.settings public_key $KEY_LOCATION/public.key -y
drush -q config:set simple_oauth.settings private_key $KEY_LOCATION/private.key -y

# 2. Create the OAuth consumer.
#   a. Get values from environment settings file.
printf "    ✔ Creating the OAuth consumer for the current environment (see https://next-drupal.org/learn/quick-start/create-consumer).\n"
CONSUMER_USER_UID=$(cat $ENV_SETTINGS | jq -r '.project.consumer.user.uid')
printf "        * user_uid: $CONSUMER_USER_UID\n"
CONSUMER_ID=$(cat $ENV_SETTINGS | jq -r '.environment.consumer.id')
printf "        * consumer_id: $CONSUMER_ID\n"
CONSUMER_LABEL=$(cat $ENV_SETTINGS | jq -r '.environment.consumer.label')
printf "        * consumer_label: $CONSUMER_LABEL\n"
CONSUMER_SITE=$(cat $ENV_SETTINGS | jq -r '.project.consumer.role.id')
printf "        * consumer_site: $CONSUMER_SITE\n"
CONSUMER_DESC=$(cat $ENV_SETTINGS | jq -r '.environment.consumer.description')

#   b. Use Platform.sh built-in variable PLATFORM_PROJECT_ENTROPY for the consumer secret, and keep track of that value for later.
CONSUMER_SECRET=$PLATFORM_PROJECT_ENTROPY
printf "        * consumer_secret: $CONSUMER_SECRET\n"
UPDATED_DATA=$(jq --arg CONSUMER_SECRET "$PLATFORM_PROJECT_ENTROPY" '.environment.consumer.secret = $CONSUMER_SECRET' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS

#   c. Get the consumer UUID, and track it in our environment settings.
CONSUMER_UUID=$(drush scr $DRUPAL_SETUP/environment/02-create-consumer.php "$CONSUMER_USER_UID" "$CONSUMER_ID" "$CONSUMER_LABEL" "$CONSUMER_DESC" "$CONSUMER_SITE" "$CONSUMER_SECRET")
printf "        * consumer_uid: $CONSUMER_UUID\n"
UPDATED_DATA=$(jq --arg CONSUMER_UUID "$CONSUMER_UUID" '.environment.consumer.uid = $CONSUMER_UUID' $ENV_SETTINGS)
echo $UPDATED_DATA > $ENV_SETTINGS
