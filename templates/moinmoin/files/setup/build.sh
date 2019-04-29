#!/usr/bin/env bash

MOINVERSION=1.9.10

# Download MoinMoin.
curl -o moin-install.tar.gz http://static.moinmo.in/files/moin-$MOINVERSION.tar.gz
tar xvzf moin-install.tar.gz
mv moin-$MOINVERSION moin-install

# Apply patches.
patch moin-install/MoinMoin/logfile/editlog.py ~/setup/editlog.patch
patch moin-install/MoinMoin/logfile/eventlog.py ~/setup/eventlog.patch

# Move install to app_dir.
mv ~/moin-install/* /app/

# Remove the install.
rm -rf ~/moin-install
rm ~/moin-install.tar.gz

# Stage files that will go to mounts on first deploy.
mkdir ~/setup/temp
mv ~/wiki/data/pages ~/setup/temp
mv ~/wiki/data/cache ~/setup/temp
mv ~/wiki/data/edit-log ~/setup/temp
mv ~/wiki/data/event-log ~/setup/temp
mv ~/wiki/underlay ~/setup/temp
