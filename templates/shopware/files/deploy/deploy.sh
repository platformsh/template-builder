#!/bin/sh

echo "deploy.sh"

SHOPWARE_ENV=prod /usr/bin/php -c /app/deploy/php/php.ini bin/console sw:cache:clear
SHOPWARE_ENV=prod /usr/bin/php -c /app/deploy/php/php.ini bin/console sw:theme:cache:generate
