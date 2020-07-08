#!/bin/bash

if [ ! -f config/config.json ] || [ ! -s config/config.json ]; then
    cp config.default config/config.json
fi
