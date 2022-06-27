#!/usr/bin/env bash

rm .env
mv .env.production .environment
yarn run build
