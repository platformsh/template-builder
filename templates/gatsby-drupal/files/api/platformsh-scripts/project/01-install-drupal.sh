#!/usr/bin/env bash
########################################################################################################################
# NOTE:
# 
# This script installs Drupal with default settings. An initial admin user is created, using the slug id from the
#   project's first commit, pulled from the environment.
#
########################################################################################################################
printf "    ✔ Installing Drupal with a Standard profile (see https://next-drupal.org/learn/quick-start/install-drupal).\n"

# 1. Define initial admin password. 
INIT_ADMIN_PASS=${PLATFORM_PROJECT_ENTROPY}

# 2. Install the site.
drush si -q --site-name="Drupal" --account-pass=$INIT_ADMIN_PASS -y

# 3. Warn the user about the initial admin account.
printf "    ✔ Installation complete.\n"
printf "    ✔ Your Drupal site has been installed with the following credentials:\n"
printf "        * \033[1muser:\033[0m admin\n"
printf "        * \033[1mpass:\033[0m $INIT_ADMIN_PASS\n"
printf "    ✗ \033[1mWARNING: Update your password and email immediately. They will only be available once.\033[0m\n"
