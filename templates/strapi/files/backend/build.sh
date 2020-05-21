#!/usr/bin/env bash

# Create quickstart Strapi project.
yarn create strapi-app tmp-app --quickstart --no-run
mv tmp-app/* . && rm -rf tmp-app

# Install additional dependencies.
yarn add pg
yarn add platformsh-config

# Move the Platform.sh-specific configuration.
rm config/environments/development/database.json && mv platformsh/database.js config/environments/development/database.js
rm config/environments/development/server.json && mv platformsh/server.json config/environments/development/server.json

# Move index.html with working admin link.
mv platformsh/index.html public/index.html

# Rebuild the admin panel.
yarn build

# Make start command executable.
chmod +x start.sh
