#!/usr/bin/env bash

HUGOVERSION=0.66.0

wget https://github.com/gohugoio/hugo/releases/download/v$HUGOVERSION/hugo_${HUGOVERSION}_Linux-64bit.tar.gz
tar xvzf hugo_${HUGOVERSION}_Linux-64bit.tar.gz

rm hugo_${HUGOVERSION}_Linux-64bit.tar.gz

./hugo
