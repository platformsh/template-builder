#!/usr/bin/env bash

SOMETHING='eleventy-strapi gatsby-strapi gatsby-drupal gatsby-wordpress symfony4 symfony5 drupal8 drupal8-multisite drupal8-opigno drupal8-govcms8 drupal9 wordpress-bedrock wordpress-composer wordpress-woocommerce wordpress-vanilla probot elastic-apm wagtail mattermost jenkins strapi'

MANUAL_REVIEWS="'$SOMETHING'"

if [[ ${MANUAL_REVIEWS} =~ drupal8 ]]; then
    echo "Template requires manual review. Skipping auto-merge."
else
    echo "Automerge it"
fi