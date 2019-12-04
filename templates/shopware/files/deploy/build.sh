#!/bin/sh

echo "build.sh"

echo "Creating symlinks"
rm -rf  $PLATFORM_APP_DIR/engine/Library
mkdir -p $PLATFORM_APP_DIR/engine/Library
ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/engine/Library/CodeMirror $PLATFORM_APP_DIR/engine/Library/CodeMirror
ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/engine/Library/ExtJs $PLATFORM_APP_DIR/engine/Library/ExtJs
ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/engine/Library/TinyMce $PLATFORM_APP_DIR/engine/Library/TinyMce

rm -rf $PLATFORM_APP_DIR/themes/Frontend/Bare
rm -rf $PLATFORM_APP_DIR/themes/Frontend/Responsive
rm -rf $PLATFORM_APP_DIR/themes/Backend/ExtJs

mkdir -p $PLATFORM_APP_DIR/themes/Backend
mkdir -p $PLATFORM_APP_DIR/themes/Frontend

ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/themes/Backend/ExtJs $PLATFORM_APP_DIR/themes/Backend/ExtJs
ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/themes/Frontend/Bare $PLATFORM_APP_DIR/themes/Frontend/Bare
ln -s $PLATFORM_APP_DIR/vendor/shopware/shopware/themes/Frontend/Responsive $PLATFORM_APP_DIR/themes/Frontend/Responsive

rm -rf $PLATFORM_APP_DIR/vendor/shopware/shopware/var
rm -rf $PLATFORM_APP_DIR/vendor/shopware/shopware/web/cache
rm -rf $PLATFORM_APP_DIR/vendor/shopware/shopware/media
rm -rf $PLATFORM_APP_DIR/vendor/shopware/shopware/files
rm -rf $PLATFORM_APP_DIR/vendor/shopware/shopware/custom

echo "Patching shopware internal folders with symlinks"
ln -s $PLATFORM_APP_DIR/var  $PLATFORM_APP_DIR/vendor/shopware/shopware/var
ln -s $PLATFORM_APP_DIR/web/cache $PLATFORM_APP_DIR/vendor/shopware/shopware/web/cache
ln -s $PLATFORM_APP_DIR/media $PLATFORM_APP_DIR/vendor/shopware/shopware/media
ln -s $PLATFORM_APP_DIR/files $PLATFORM_APP_DIR/vendor/shopware/shopware/files
ln -s $PLATFORM_APP_DIR/custom $PLATFORM_APP_DIR/vendor/shopware/shopware/custom
