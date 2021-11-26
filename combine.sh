#!/usr/bin/env bash


MANUAL_MULTIAPPS='eleventy-strapi gatsby-strapi gatsby-drupal gatsby-wordpress'
MANUAL_500STATUS='symfony3 symfony4 symfony5'
MANUAL_DRUPAL_INSTALL='drupal8 drupal8-multisite drupal8-opigno drupal8-govcms8 drupal9'
MANUAL_WP_INSTALL='wordpress-bedrock wordpress-composer wordpress-woocommerce wordpress-vanilla'
MANUAL_MISC_POSTDEPLOY='probot elastic-apm wagtail mattermost jenkins strapi'

# MANUAL_REVIEW=$(string join ' ' $MANUAL_MULTIAPPS $MANUAL_500STATUS $MANUAL_DRUPAL_INSTALL $MANUAL_WP_INSTALL $MANUAL_MISC_POSTDEPLOY)

MANUAL_REVIEW=""
for MANUAL in $MANUAL_MULTIAPPS $MANUAL_500STATUS $MANUAL_DRUPAL_INSTALL $MANUAL_WP_INSTALL $MANUAL_MISC_POSTDEPLOY; do
    MANUAL_REVIEW+="${MANUAL} "
done
echo $MANUAL_REVIEW