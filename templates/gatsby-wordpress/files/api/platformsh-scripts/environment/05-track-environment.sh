#!/usr/bin/env bash
########################################################################################################################
# NOTE:
#
# This script tracks settings that have changed related to the the Next.js-WordPress connection for a particular
#   environment on Platform.sh. Throughout setup, plenty has been updated to ensure that for any given environment,
#   a unique Next.js app container connects with its own unique Drupal container, and that this relationship is seemless
#   across branching commits as well as local development work.
#
# Here, a few last minute things are updated:
#   1) The current frontend URL is updated for the environment.
#   2) If this is the project's first every push, successful installation is logged.
#   3) Next.js, both on Platform.sh and locally, relies on environment variables typically included in a .env file.
#       Rather than forcing the Next.js container to build this file, the CMS is considered to be the source of truth and
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
# FRONTEND_URL is determined and defined in the .environment file
UPDATED_DATA=$(jq --arg FRONTEND_URL "${FRONTEND_URL}" '.environment.client.url.base = $FRONTEND_URL' "${ENV_SETTINGS}")
echo "${UPDATED_DATA}" > "${ENV_SETTINGS}"
# FRONTEND_PREVIEW_LOCATION is determined and defined in the .environment file
UPDATED_DATA=$(jq --arg PREVIEW_URL "${FRONTEND_PREVIEW_LOCATION}" '.environment.client.url.preview = $PREVIEW_URL' "${ENV_SETTINGS}")
echo "${UPDATED_DATA}" > "${ENV_SETTINGS}"

# b. Track the overall installation.
if [[ "production" == "${PLATFORM_ENVIRONMENT_TYPE}" ]]; then
    printf "    ✔ Logging production installation\n"
    SETTINGS_UPDATES=$(jq '.project.production.installed = true' "${ENV_SETTINGS}")
    echo "${SETTINGS_UPDATES}" > "${ENV_SETTINGS}"
fi

# 2. Generate the .env files that will be needed on Platform.sh environments and local development.

# a. Organize everything we need.
printf "* Preparing credentials to hand off to frontend container.\n"
# WORDPRESS_API_URL
wpGraphqlURL=$(jq -r '.environment.api.url.graphql' < "${ENV_SETTINGS}")
# WORDPRESS_AUTH_REFRESH_TOKEN
wpAuthRefreshToken=$(jq -r '.environment.consumer.secret' < "${ENV_SETTINGS}")
# WORDPRESS_PREVIEW_SECRET - already defined in .environment
# IMAGE_DOMAIN - just the raw domain of our api URL
# @todo is it possible this will ever need to be a different domain?
wpBaseURL=$(jq -r '.environment.api.url.base' < "${ENV_SETTINGS}")
imageDomain=$(jq -r '.environment.api.url.base' < "${ENV_SETTINGS}" | awk -F/ '{print $3}')

# b. Create the .env file used for local development.

printf "* Writing remote configuration.\n"
printf "# This .environment file is generated programmatically within the backend WordPress app for each Platform.sh
# environment and stored within an network storage mount so it can be shared between apps.
export WORDPRESS_API_URL=%s
export WORDPRESS_PREVIEW_SECRET=%s
export IMAGE_DOMAIN=%s
export WORDPRESS_AUTH_REFRESH_TOKEN=%s
" "${wpGraphqlURL}" "${WORDPRESS_PREVIEW_SECRET}" "${imageDomain}" "${wpAuthRefreshToken}" > "${VARS_PSH}"

echo "${SPLIT_LINE}"
# cant we just cat here instead of cat'ing inside of a printf?
#printf "$(cat %s)\n" "${VARS_LOCAL}"
cat "${VARS_PSH}"
echo "${SPLIT_LINE}"

#now that we have our platformsh.environment file, let's create a duplicate minus the `export` keyword
printf "* Writing local configuration.\n"
sed 's/export //' "${VARS_PSH}" > "${VARS_LOCAL}"
#now we just need to adjust the message in the file. This is a .env file not a .environment file
sed -i 's/ .env / .environment /' "${VARS_LOCAL}"
#and we'll use it locally not between apps
sed  -i 's/ shared between apps/ used locally/' "${VARS_LOCAL}"

echo "${SPLIT_LINE}"
cat "${VARS_LOCAL}"
echo "${SPLIT_LINE}"
