#!/usr/bin/env bash

# Environment-specific configuration for Gatsby.
if [ "$PLATFORM_BRANCH" = master ]; then
   sleep infinity
else
   npm run develop
fi
