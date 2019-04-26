#!/usr/bin/env bash

# Download MoinMoin
curl -O http://static.moinmo.in/files/moin-1.9.10.tar.gz
tar xvzf moin-1.9.10.tar.gz

# Stage MoinMoin log files
mv ~/setup/editlog.py moin-1.9.10/MoinMoin/logfile
mv ~/setup/eventlog.py moin-1.9.10/MoinMoin/logfile

# Move the app directory
cp -a ~/moin-1.9.10/* /app/

# Remove the install
rm -rf ~/moin-1.9.10
rm ~/moin-1.9.10.tar.gz

# Stage files that will go to mounts on deploy
mkdir ~/setup/temp
mv ~/wiki/data/pages ~/setup/temp
mv ~/wiki/data/cache ~/setup/temp
mv ~/wiki/data/edit-log ~/setup/temp
mv ~/wiki/data/event-log ~/setup/temp
mv ~/wiki/underlay ~/setup/temp
