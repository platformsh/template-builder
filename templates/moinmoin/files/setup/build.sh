#!/usr/bin/env bash

MOINVERSION=1.9.10

# Download MoinMoin.
curl -o moin-install.tar.gz http://static.moinmo.in/files/moin-$MOINVERSION.tar.gz
tar xvzf moin-install.tar.gz
mv moin-$MOINVERSION moinmoin
rm moin-install.tar.gz

# Apply patches.
patch moinmoin/MoinMoin/logfile/editlog.py setup/editlog.patch
patch moinmoin/MoinMoin/logfile/eventlog.py setup/eventlog.patch

# Move local configuration to the install.
mv wikiconfig_local.py moinmoin
mv wikiserverconfig_local.py moinmoin

# Stage files that will go to mounts on first deploy.
mkdir setup/temp
mv moinmoin/wiki/data/pages setup/temp
mv moinmoin/wiki/data/cache setup/temp
mv moinmoin/wiki/data/edit-log setup/temp
mv moinmoin/wiki/data/event-log setup/temp
mv moinmoin/wiki/underlay setup/temp
