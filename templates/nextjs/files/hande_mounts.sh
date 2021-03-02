#!/usr/bin/env bash

MOUNT_TMP=platformsh-mounts

prepare_mount() {
    if [ -d $PLATFORM_APP_DIR$1 ]; then
        if [ ! -d $MOUNT_TMP ]; then
            mkdir $MOUNT_TMP
        fi
        mkdir $MOUNT_TMP/$1-tmp && mv $PLATFORM_APP_DIR$1/* $MOUNT_TMP/$1-tmp
    fi
}

restore_mount() {
    if [ -d $MOUNT_TMP$1-tmp ]; then
        rm -r $PLATFORM_APP_DIR$1/*
        cp -r $MOUNT_TMP$1-tmp/* $PLATFORM_APP_DIR$1
    fi
}

MOUNTS=$(echo $PLATFORM_APPLICATION | base64 --decode | jq '.mounts | keys')
for mount in $(echo "${MOUNTS}" | jq -r '.[]'); do 
    _jq() {
        if [ -z "${PLATFORM_BRANCH}" ]; then
            prepare_mount $mount
        # I don't remember why I didn't want this to occur on master.
        # elif [ "$PLATFORM_BRANCH" != master ]; then
        else
            restore_mount $mount
        fi
    }
    echo $(_jq)
done
