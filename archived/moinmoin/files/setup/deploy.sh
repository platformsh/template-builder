#!/usr/bin/env bash

if [ ! -f moinmoin/wiki/underlay/moin.installed ]; then

    # Copy staged files to mounts.
    cp -a setup/temp/pages/* moinmoin/wiki/data/pages
    cp -a setup/temp/cache/* moinmoin/wiki/data/cache
    cp -a setup/temp/underlay/* moinmoin/wiki/underlay
    cp -a setup/temp/edit-log moinmoin/wiki/data/logging
    cp -a setup/temp/event-log moinmoin/wiki/data/logging

    touch moinmoin/wiki/underlay/moin.installed
fi
