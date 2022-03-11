#!/usr/bin/env bash
# Some vars.
UPDATER_HOME=$(pwd)
TEMPLATES_HOME=$UPDATER_HOME/templates
DEMOS_HOME=$UPDATER_HOME/demos/foodadvisor
DATA_FILE=foodadvisor.sql
DATA_TAR=foodadvisor.tar.gz
# Relevant templates to apply the updates.
templates=( 
    nextjs-strapi 
    # eleventy-strapi 
    # gatsby-strapi 
    )
# Run the update.
for template in "${templates[@]}"
do
	printf "\nUpdating demo data for $template.\n"
    # Rebuild the template's `build` directory.
    poetry run doit cleanup:$template
    poetry run doit init:$template
    poetry run doit update:$template
    poetry run doit platformify:$template
    # Update the data tar.gz file.
    cp $DEMOS_HOME/$DATA_FILE $TEMPLATES_HOME/$template/build/api
    cd $TEMPLATES_HOME/$template/build/api
    rm $DATA_TAR
    yarn seed
    tar -czf $DATA_TAR $DATA_FILE public/uploads
    cp $DATA_TAR $TEMPLATES_HOME/$template/files/api
    rm $DATA_FILE && rm -rf public/uploads
    # Push the updates.
    poetry run doit branch:$template
    poetry run doit push:$template
done
