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
    # poetry run doit cleanup:$template
    # poetry run doit init:$template
    # poetry run doit update:$template
    # poetry run doit platformify:$template
    # Update the data tar.gz file.
    # mkdir $TEMPLATES_HOME/$template/build/api/deploy
    # cp $DEMOS_HOME/$DATA_FILE $TEMPLATES_HOME/$template/build/api/deploy
    cd $TEMPLATES_HOME/$template/build/api
    # # Remove previous tar.gz file.
    # rm $DATA_TAR
    # # Setup data to zip.
    # yarn seed
    # Create the file.
    # tar -czf $DATA_TAR deploy public/uploads
    # # Put it where it will be committed.
    # cp $DATA_TAR $TEMPLATES_HOME/$template/files/api
    # # Cleanup.
    # rm -rf deploy && rm -rf public/uploads
    # # Push the updates.
    cd $UPDATER_HOME
    poetry run doit branch:$template
    poetry run doit push:$template
done
