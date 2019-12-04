#!/bin/sh

echo "build.sh"

echo "Creating symlinks"
rm -rf  /app/engine/Library
mkdir -p /app/engine/Library
ln -s /app/vendor/shopware/shopware/engine/Library/CodeMirror /app/engine/Library/CodeMirror
ln -s /app/vendor/shopware/shopware/engine/Library/ExtJs /app/engine/Library/ExtJs
ln -s /app/vendor/shopware/shopware/engine/Library/TinyMce /app/engine/Library/TinyMce

rm -rf /app/themes/Frontend/Bare
rm -rf /app/themes/Frontend/Responsive
rm -rf /app/themes/Backend/ExtJs

mkdir -p /app/themes/Backend
mkdir -p /app/themes/Frontend

ln -s /app/vendor/shopware/shopware/themes/Backend/ExtJs /app/themes/Backend/ExtJs
ln -s /app/vendor/shopware/shopware/themes/Frontend/Bare /app/themes/Frontend/Bare
ln -s /app/vendor/shopware/shopware/themes/Frontend/Responsive /app/themes/Frontend/Responsive
ln -s /app/src/theme/Tecosmart /app/themes/Frontend/Tecosmart

ln -s /app/src/plugin/Tecosmart /app/Plugins/Local/Frontend/Tecosmart

rm -rf /app/vendor/shopware/shopware/var
rm -rf /app/vendor/shopware/shopware/web/cache
rm -rf /app/vendor/shopware/shopware/media
rm -rf /app/vendor/shopware/shopware/files
rm -rf /app/vendor/shopware/shopware/custom

echo "Patching shopware internal folders with symlinks"
ln -s /app/var  /app/vendor/shopware/shopware/var
ln -s /app/web/cache /app/vendor/shopware/shopware/web/cache
ln -s /app/media /app/vendor/shopware/shopware/media
ln -s /app/files /app/vendor/shopware/shopware/files
ln -s /app/custom /app/vendor/shopware/shopware/custom

