#!/usr/bin/env bash

#found out where we are so we can include other files
DIR="${BASH_SOURCE%/*}"
#if BASH_SOURCE didn't return what we want, try PWD
if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
#Include our common.sh
. "${DIR}/common.sh"

# if our pshInstalled file isn't present, begin the installation process
if [ ! -f "${pshInstalled}" ]; then
  echo "Installing Typo3..."
  # Since we haven't installed, then we need to make sure we sync all the directories/files that the typo3 composer
  # installer extender generates during composer install
  # we only want to do this if we're running on a platform environment, and not local development.
  if [[ -n ${PLATFORM_TREE_ID+x} && $PLATFORM_TREE_ID =~ $pshTreeIDPttrn  ]]; then
    echo "$mountsToSync" | tr ' ' '\n' | while read dir; do
      if [ -d "${PLATFORM_APP_DIR}/${dir}.${tmpDirExtension}" ]; then
        rsync -r "${PLATFORM_APP_DIR}/${dir}.${tmpDirExtension}/" "${PLATFORM_APP_DIR}/${dir}/"
      fi
    done
  fi

  cp "${PLATFORM_APP_DIR}/public/typo3conf/LocalConfiguration.FromSource.php" "${PLATFORM_APP_DIR}/${varPath}/LocalConfiguration.php"
  # On first install, create an initial admin user with a default password.
  # *CHANGE THIS VALUE IMMEDIATELY AFTER INSTALLATION*
  composer exec typo3cms install:setup -- \
      --install-steps-config=src/SetupDatabase.yaml \
      --site-setup-type=no \
      --site-name="TYPO3 on Platform.sh" \
      --admin-user-name=admin \
      --admin-password=password \
      --skip-extension-setup \
      --no-interaction

  # Create the file that indicates first deploy and installation has been completed.
  touch "${pshInstalled}"
# this isn't a new install BUT the PackageArtifacts.php in var/build might have been updated by composer, so we need to
# rsync it just in case but only if we're not local
elif [[ -n ${PLATFORM_TREE_ID+x} && $PLATFORM_TREE_ID =~ $pshTreeIDPttrn  ]]; then
  echo "Typo3 is already installed, so we only need to sync the PackageArtifacts.php file"
  if [ -d "${PLATFORM_APP_DIR}/${varPath}/build.${tmpDirExtension}" ]; then
    rsync -r "${PLATFORM_APP_DIR}/${varPath}/build.${tmpDirExtension}/" "${PLATFORM_APP_DIR}/${varPath}/build/"
  fi
fi

# Now set up all extensions that may have been added via composer (build step) but not set up yet (db-related)
composer exec typo3cms install:extensionsetupifpossible

