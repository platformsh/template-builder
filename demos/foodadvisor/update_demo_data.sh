#!/usr/bin/env bash

DEMOS_HOME=demos/foodadvisor
DATA_FILE=foodadvisor.sql
TEMPLATES_HOME=templates
DATA_TAR=foodadvisor.tar.gz

templates=( 
    nextjs-strapi 
    # eleventy-strapi 
    # gatsby-strapi 
    )
for template in "${templates[@]}"
do
	printf "\nUpdating demo data for $template.\n"
    poetry run doit rebuild:$template
    cp $DEMOS_HOME/$DATA_FILE $TEMPLATES_HOME/$template/build/api
    cd $TEMPLATES_HOME/$template/build/api
    rm $DATA_TAR
    yarn --frozen-lockfile
    yarn seed
    tar -czf $DATA_TAR $DATA_FILE public/uploads
    rm $DATA_FILE && rm -rf public/uploads
    cp $DATA_TAR $TEMPLATES_HOME/$template/files/api
    
done

