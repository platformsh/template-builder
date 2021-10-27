#!/usr/bin/env bash
# list of mounts we need to resync between build + deploy on first install
mountsToSync="var public/fileadmin public/typo3temp"
# Where Typo3 stores most of their variable stuff
# @todo we could extract it from mountsToSync. Also the variable needs a better name
varPath="var"
#name+location of file that we use to determine if we need to run the installers
pshInstalled="${PLATFORM_APP_DIR}/${varPath}/platformsh.installed"
# the "extension" to add to our directories we need to sync between build & deploy
tmpDirExtension="psh"
# Regex pattern for checking PLATFORM_TREE_ID to make sure we're running on a Platform.sh environment
pshTreeIDPttrn="^[a-z0-9]{40}$"
