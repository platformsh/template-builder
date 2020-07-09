#!/usr/bin/env bash

echo "Downloading Mattermost ${MATTERMOST_VERSION}"
wget --quiet -c https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz -O - | tar -xz
cp -a mattermost/* .

chmod +x start.sh
chmod +x bin/mattermost

cp config/config.json config.default
