#!/usr/bin/env bash

DOWNLOAD=https://github.com/gohugoio/hugo/releases/download/v$HUGOVERSION/hugo_${HUGOVERSION}_Linux-64bit.tar.gz
wget --quiet -c $DOWNLOAD -O - | tar -xz

./hugo
