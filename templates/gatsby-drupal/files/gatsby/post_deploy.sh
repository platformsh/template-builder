#!/usr/bin/env bash

# Environment-specific post_deploy hook for Gatsby.
if [ "$PLATFORM_BRANCH" = master ]; then
   npm run build
fi
