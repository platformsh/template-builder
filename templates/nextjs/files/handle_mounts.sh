#!/usr/bin/env bash

MOUNT_TMP=platformsh-mounts

handle_hidden_mounts(){
    MOUNT=$1
    if [[ ${MOUNT:0:1} == "/" ]] ; then echo "${MOUNT:1}"; else echo $MOUNT; fi
}

stage_files() {
    MOUNT=`handle_hidden_mounts $1`
    if [ -d $PLATFORM_APP_DIR$1 ]; then
        if [ ! -d $PLATFORM_APP_DIR$MOUNT_TMP ]; then
            mkdir $PLATFORM_APP_DIR$MOUNT_TMP
        fi
        mkdir -p $PLATFORM_APP_DIR$MOUNT_TMP/$MOUNT-tmp && mv $PLATFORM_APP_DIR$MOUNT/* $PLATFORM_APP_DIR$MOUNT_TMP/$MOUNT-tmp
    fi
}

restore_files() {
    MOUNT=`handle_hidden_mounts $1`
    if [ -d $MOUNT_TMP$MOUNT-tmp ]; then
        rm -r $PLATFORM_APP_DIR$MOUNT/*
        cp -r $MOUNT_TMP$MOUNT-tmp/* $PLATFORM_APP_DIR$MOUNT
    fi
}

# Use PLATFORM_APPLICATION to find all user-defined mounts.
MOUNTS=$(echo $PLATFORM_APPLICATION | base64 --decode | jq '.mounts | keys')
for mount in $(echo "${MOUNTS}" | jq -r '.[]'); do 
    _jq() {
        # hooks.build: Copy directory content to tmp directory.
        if [ -z "${PLATFORM_BRANCH}" ]; then
            stage_files $mount
        # hooks.deploy: Copy tmp directory content back into the mounts.
        else
            restore_files $mount
        fi
    }
    echo $(_jq)
done
