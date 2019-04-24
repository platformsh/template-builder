#!/usr/bin/env bash

cd $PLATFORM_APP_DIR

cp -a wiki/config mywiki
cp -a wiki/server mywiki

cp -a wiki/data/* mywiki/data
cp -a wiki/underlay/* mywiki/underlay



