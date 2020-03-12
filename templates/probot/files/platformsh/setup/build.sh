#!/usr/bin/env bash


# Create a symlink for the .env file, where GitHub App credentials need to be written during registration hand shake.
ln -s registration/.env .env

# Remame user-supplied app.yml file, so that correct WEBHOOK_PROXY_URL can be written to it during deploy.
mv app.yml probot.app.yml

# Create a symlink for the app.yml file, which will need to be writable during deploy, but in project root.
ln -s registration/app.yml app.yml

# Install Platform.sh CLI
curl -sS https://platform.sh/cli/installer | php
