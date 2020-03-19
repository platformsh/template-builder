#!/usr/bin/env bash

# Set the site url during the start command once routes are available
MM_SERVICESETTINGS_SITEURL=$(echo "$PLATFORM_ROUTES" | base64 --decode | jq -r 'to_entries[] | select(.value.primary) | .key') ./bin/mattermost
