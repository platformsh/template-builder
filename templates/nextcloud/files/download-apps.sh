#!/bin/bash

echo "Installing Additional Apps"
cd src/apps
file="../../apps.txt"
while read -r line; do
    [ "$line" = "\#*" ] && continue
    echo "Installing ${line}"
    wget --quiet -c $line -O - | tar -xz
done < "$file"
cd ..
