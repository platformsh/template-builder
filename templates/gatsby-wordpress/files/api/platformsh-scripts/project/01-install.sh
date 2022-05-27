#!/usr/bin/env bash
########################################################################################################################
# NOTE:
#
# This script installs WordPress with default settings. An initial admin user is created
#
########################################################################################################################
printf "    ✔ Installing WordPress \n"

# 1. Define initial admin password.
INIT_ADMIN_PASS=$(echo -n "${PLATFORM_PROJECT_ENTROPY}" | sha1sum | awk '{print $1}')

# 2. Install the site.
# We need:
# a. Admin name - go with "admin" for now
# b. Admin email address - we'll have to go with a fake email address and instructions to update it
# c. Site URL - get that from
# d. Site Title
adminName=$(jq -r '.project.admin_user.name' < "${ENV_SETTINGS}")
adminEmail=$(jq -r '.project.admin_user.email' < "${ENV_SETTINGS}")
siteTitle=$(jq -r '.project.title' < "${ENV_SETTINGS}")
siteURL=$(echo "${PLATFORM_ROUTES}" | base64 --decode | jq -r 'to_entries[] | select(.value.id == "api") | .key')

#we create our admin user at the same time as we install the site
wp core install --url="${siteURL}" --title="${siteTitle}" --admin_user="${adminName}" --admin_password="${INIT_ADMIN_PASS}" --admin_email="${adminEmail}"
# @todo should we check for an error before reporting success?

# 3. Warn the user about the initial admin account.
printf "    ✔ Installation complete.\n"
printf "    ✔ Site is available at %s\n" "${siteURL}"
printf "    ✔ Your WordPress site has been installed with the following credentials:\n"
printf "        * \033[1muser: \033[0m %s\n" "${adminName}"
printf "        * \033[1mpass: \033[0m %s\n" "${INIT_ADMIN_PASS}"
printf "        * \033[1memail:\033[0m %s\n" "${adminEmail}"
printf "    ✗ \033[1mWARNING: Update your password and email immediately. They will only be available once.\033[0m\n"
printf "    ✗ \033[1mWARNING: Make sure to update the email address for both the %s user and in Settings --> General.\033[0m\n" "${adminName}"

# Save the site URL
UPDATED_SETTINGS=$(jq --arg SITEURL "${siteURL}" '.environment.api.url.base = $SITEURL' "$ENV_SETTINGS")
echo "${UPDATED_SETTINGS}" > "$ENV_SETTINGS"
