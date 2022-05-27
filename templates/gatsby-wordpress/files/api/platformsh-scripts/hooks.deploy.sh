#!/usr/bin/env bash

########################################################################################################################
# ABOUT:
#
# This script has been included to deploy a demo WordPress application, that is seeded with a number of dummy posts, and
#   that is meant to have its API consumed by a frontend Next.js client. Not all pieces of this script will be relevant
#   for your migration. It's meant to automate steps outlined in the Nextjs-WordPress demo, which you can follow
#   manually during your own migration from there (https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress).
#
# When migrating your own site, the only pieces that will not be immediately relevant are those involved with creating
#   demo content posts, which is run when the project level environment variable CREATE_DEMO_CONTENT is set to true in
#   WordPress' .platform.app.yaml file. If copying these files exactly, you can remove or set to false, and it should
#   contain everything you need to run Next.js and WordPress across environments.
#
# It is meant to be run on a Platform.sh environment during the deploy hook.
#
########################################################################################################################
# NOTE:
#
# There are a lot of moving pieces in this demo, so included is a platformsh-scripts/settings.default.json file meant to
#   track it all. In this first step, the file is copied to the Network Storage mount 'deploy'. This does two things.
#   First, we can write to it at runtime, and second, the Next.js app will have access to it as well, which is helpful
#   for keeping the two apps in sync across environments. Initial settings committed to the demo (INITAL_DEMO_SETTINGS)
#   are moved to the mount early in the script (ENV_SETTINGS).
#
########################################################################################################################
# STEPS:
#
#   a. Setup WordPress: performed on every deployment.
#   b. Project installation: only performed during first deployment on a new project.
#   c. Environment configuration: performed during the first push on a new environment.
#   d. WordPress tasks: performed on every deployment.
#
########################################################################################################################

########################################################################################################################
# b. Project installation: only performed during first deployment on a new project.
if [ -f "$ENV_SETTINGS" ]; then
    printf "\n* Project already installed. Skipping installation.\n"
else
    printf "\n* Fresh project detected.\n"
    # 0. Track the installation in a writable file, making note of the current environment before anything else. (See NOTE).
    UPDATED_DATA=$(jq --arg PLATFORM_BRANCH "$PLATFORM_BRANCH" '.environment.branch = $PLATFORM_BRANCH' $INITIAL_DEMO_SETTINGS)
    echo $UPDATED_DATA > $ENV_SETTINGS

    # 1. Install WordPress
    $WP_SETUP/project/01-install.sh

    # 2. Enable plugins.
    $WP_SETUP/project/02-enable-plugins.sh

    # 3. Set up permalink structure
    $WP_SETUP/project/03-set-permalink-structure.sh
    # 4. Configure content.
    $WP_SETUP/project/04-create-content.sh
fi
########################################################################################################################
# c. Environment configuration: performed during the first push on a new environment.
if [ -f "$ENV_SETTINGS" ]; then

    printf "* Configuring the environment.\n"
    # 1. Check the current environment and project status.
    PROD_INSTALL=$(jq -r '.project.production.installed' < "${ENV_SETTINGS}")
    PREPPED_ENV=$(jq -r '.environment.branch' < "${ENV_SETTINGS}")

   # 2. Run setup if a) very first project deploy on production environment, or b) first deploy on a new environment.
    if [ "$PROD_INSTALL" = false ]  || [ "$PREPPED_ENV" != "$PLATFORM_BRANCH" ]; then

        # a. Clear the previous environment's configuration.
        "${WP_SETUP}"/environment/01-verify-user.sh

				# b. Update environment URLS
				"${WP_SETUP}"/environment/02-update-urls.sh

        # c. Get & set our GraphQL endpoint
        "${WP_SETUP}"/environment/03-get-graphql-endpoint.sh

        # d. Generate our new refreshToken.
        "${WP_SETUP}"/environment/04-generate-refresh-token.sh

       # d. Track the installation and configure the frontend.
       "${WP_SETUP}"/environment/05-track-environment.sh

    else
        printf "* Environment already prepped for frontend. Skipping setup.\n"
    fi
else
    printf "✗ Something went wrong during the installation phase. Investigate!\033"
    exit 1
fi
########################################################################################################################
# d. WordPress tasks: performed on every deployment.
wp cache flush
wp core update-db
wp cron event run --due-now
