#!/bin/sh

rm -rf /app/var/cache/production_*/doctrine/* && \
rm -rf /app/var/cache/production_*/general/* && \
rm -rf /app/var/cache/production_*/html/* && \
rm -rf /app/var/cache/production_*/mpdf/* && \
rm -rf /app/var/cache/production_*/proxies/* && \
rm -rf /app/var/cache/production_*/templates/* && \
SHOPWARE_ENV=prod /usr/bin/php -c /app/deploy/php/php.ini bin/console --no-interaction sw:cache:clear && \
SHOPWARE_ENV=prod /usr/bin/php -c /app/deploy/php/php.ini bin/console --no-interaction sw:theme:cache:generate && \
SHOPWARE_ENV=prod /usr/bin/php -c /app/deploy/php/php.ini bin/console --no-interaction sw:warm:http:cache
