#!/bin/sh

rm -rf /app/var/cache/production_*/doctrine/* && \
rm -rf /app/var/cache/production_*/general/* && \
rm -rf /app/var/cache/production_*/html/* && \
rm -rf /app/var/cache/production_*/mpdf/* && \
rm -rf /app/var/cache/production_*/proxies/* && \
rm -rf /app/var/cache/production_*/templates/* && \
php bin/console --no-interaction sw:cache:clear && \
php bin/console --no-interaction sw:theme:cache:generate && \
php bin/console --no-interaction sw:warm:http:cache
