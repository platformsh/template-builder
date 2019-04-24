#!/usr/bin/env bash

cd $PLATFORM_APP_DIR

cp -a wiki/config mywiki
cp -a wiki/data mywiki
cp -a wiki/server mywiki

cp wiki/underlay.tar /mnt/mywiki

cd /mnt/mywiki

tar xf underlay.tar
