#!/usr/bin/env bash

export MATTERMOST_VERSION=$(cat mattermost_version)

download_mattermost() {
    printf "\n  ✔ \033[1mDownloading Mattermost...\033[0m ($MATTERMOST_VERSION)\n\n"
    wget --quiet -c https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz -O - | tar -xz
    cp -a mattermost/* .
    chmod +x bin/mattermost
}

set_config() {
    cp config/config.json config.default
}

set -e
download_mattermost
set_config
