#!/usr/bin/env bash
########################################################################################################################
# NOTE:
#
# This script retrieves the URL for a new instance. Trailing slash in URL is *removed*
#
########################################################################################################################
printf "   Retrieving environment URL... "
newEnvironmentURL=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id == "api") | .key')
newURLNoTrailSlash=${newEnvironmentURL%/}
printf " ✔\n"
printf "   Storing environment URL %s... ✔\n" "${newURLNoTrailSlash}"
UPDATED_DATA=$(jq --arg newApiUrlBase "${newURLNoTrailSlash}" '.environment.api.url.base = $newApiUrlBase' $ENV_SETTINGS)
echo "${UPDATED_DATA}" > "${ENV_SETTINGS}"
