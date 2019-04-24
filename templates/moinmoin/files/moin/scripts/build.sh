#!/usr/bin/env bash

cd moin/

curl -O http://static.moinmo.in/files/moin-1.9.10.tar.gz
tar xvzf moin-1.9.10.tar.gz

mv seeds/wikiconfig.py moin-1.9.10
mv seeds/wikiserverconfig.py moin-1.9.10

cp -a moin-1.9.10/* /app/

cd $PLATFORM_APP_DIR
