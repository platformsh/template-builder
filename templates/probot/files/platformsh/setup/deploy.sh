#!/usr/bin/env bash


# Add the Platform.sh url to the app.yml `hook_attributes.url` attribute.
node platformsh/utils/update_appyml.js

CHECK="$(node platformsh/utils/get_dotenv.js APP_ID)"

if [ $CHECK != "undefined" ]; then

  if [ -z "${GH_REGISTERED}" ]; then

    # Get the important .env vars
    APP_ID="$(node platformsh/utils/get_dotenv.js APP_ID)"
    WEBHOOK_SECRET="$(node platformsh/utils/get_dotenv.js WEBHOOK_SECRET)"
    WEBHOOK_PROXY_URL="$(node platformsh/utils/get_url.js)"

    # Write a temporary Private Key file in the mount so it can be read.
    node platformsh/utils/get_privatekey.js

    # Turn into proper environment vars so we can branch and merge without over-writing anything.
    platform variable:create --level environment --environment $PLATFORM_BRANCH env:APP_ID --value $APP_ID --inheritable false --json false --sensitive false --enabled true --no-wait
    platform variable:create --level environment --environment $PLATFORM_BRANCH env:WEBHOOK_PROXY_URL --value $WEBHOOK_PROXY_URL --inheritable false --json false --sensitive false --enabled true --no-wait
    platform variable:create --level environment --environment $PLATFORM_BRANCH env:WEBHOOK_SECRET --value $WEBHOOK_SECRET --sensitive true --inheritable false --json false --enabled true --no-wait
    platform variable:create --level environment --environment $PLATFORM_BRANCH env:PRIVATE_KEY --value="$(cat registration/temp-key.txt)" --sensitive true --inheritable false --json false --enabled true --no-wait

    # Include a variable to signfy full registration once all completed.
    platform variable:create --level environment --environment $PLATFORM_BRANCH env:GH_REGISTERED --value true --inheritable false --json false --sensitive false --enabled true --no-wait

  else

    # Clean up all of our tmp work. I think if I create the symlink again, these files get deleted automatically?
    rm registration/temp-key.txt
    rm registration/.env

  fi

fi
