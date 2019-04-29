#!/usr/bin/env bash

if [ ! -f wiki/underlay/moin.installed ]; then

    # Copy staged files to mounts.
    cp -a ~/setup/temp/pages/* ~/wiki/data/pages
    cp -a ~/setup/temp/cache/* ~/wiki/data/cache
    cp -a ~/setup/temp/underlay/* ~/wiki/underlay
    cp -a ~/setup/temp/edit-log ~/wiki/data/logging
    cp -a ~/setup/temp/event-log ~/wiki/data/logging

    touch wiki/underlay/moin.installed
fi
