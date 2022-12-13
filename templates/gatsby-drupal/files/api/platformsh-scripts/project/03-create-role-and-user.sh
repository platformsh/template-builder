#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# An OAuth consumer will be configured to access preview routes, which requires a user and role for those scopes to be
#   created first. Steps are outlined in https://next-drupal.org/learn/quick-start/create-role.
#
# https://www.gatsbyjs.com/plugins/gatsby-source-drupal/#fastbuilds - This will require authentication to your Drupal 
# site and a Drupal user with the Drupal permission to sync gatsby fastbuild log entities.
#
########################################################################################################################
# 1. Create role for the OAuth consumer.
printf "    ✔ Creating role (see https://next-drupal.org/learn/quick-start/create-role).\n"
ROLE_ID=$(cat $ENV_SETTINGS | jq -r '.project.consumer.role.id')
ROLE_LABEL=$(cat $ENV_SETTINGS | jq -r '.project.consumer.role.label')
printf "        * id: $ROLE_ID\n"
printf "        * label: $ROLE_LABEL\n"
drush -q role:create "$ROLE_ID" "$ROLE_LABEL"

# 2. Assign permissions to the new role.
printf "    ✔ Defining role permissions (see https://next-drupal.org/learn/quick-start/create-role).\n"
ROLE_PERMISSIONS=$(cat $ENV_SETTINGS | jq -r '.project.consumer.role.permissions | join(", ")')
for row in $(cat $ENV_SETTINGS | jq -r '.project.consumer.role.permissions [] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode
    }
printf "        * $(_jq '.')\n"
done 
drush -q role:perm:add "$ROLE_ID" "$ROLE_PERMISSIONS"

# 3. Create a user.
USER_ID=$(cat $ENV_SETTINGS | jq -r '.project.consumer.user.id')
printf "    ✔ Creating user (see https://next-drupal.org/learn/quick-start/create-role).\n"
printf "        * id: $USER_ID\n"
drush -q user:create "$USER_ID"
drush -q user:password "$USER_ID" "$PLATFORM_PROJECT_ENTROPY"

# 4. Grant permissions to the user.
printf "    ✔ Granting role permissions to user (see https://next-drupal.org/learn/quick-start/create-role)\n"
drush -q user:role:add "$ROLE_ID" "$USER_ID"
printf "        * user_id: $USER_ID\n"
printf "        * role_id: $ROLE_ID\n"

# 5. Track the user we just created across environments in our settings file.
printf "    ✔ Tracking user (see https://next-drupal.org/learn/quick-start/create-role).\n"
printf "        * id: $USER_ID\n"
CONSUMER_USER_ID=$(drush user:information "$USER_ID" --format=json | jq -r 'to_entries[] | .value.uid')
printf "        * uid: $CONSUMER_USER_ID\n"
UPDATED_SETTINGS=$(jq --arg CONSUMER_USER_ID "$CONSUMER_USER_ID" '.project.consumer.user.uid = $CONSUMER_USER_ID' $ENV_SETTINGS)
echo $UPDATED_SETTINGS > $ENV_SETTINGS
