#!/usr/bin/env bash

echo "Downloading Mattermost ${MATTERMOST_VERSION}"
wget --quiet https://releases.mattermost.com/${MATTERMOST_VERSION}/mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz

tar xzf mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz
rm mattermost-${MATTERMOST_VERSION}-linux-amd64.tar.gz
cp -a mattermost/* .

chmod +x start.sh
chmod +x bin/mattermost

cp config/config.json config.default
