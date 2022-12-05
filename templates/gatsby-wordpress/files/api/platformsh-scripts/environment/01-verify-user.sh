#!/usr/bin/env bash

# @todo verify we got something
previewUser=$(jq -r '.environment.consumer.name' < "${ENV_SETTINGS}");

# wp user get foobar &> /dev/null;

if ! $(wp user get "${previewUser}" &> /dev/null); then
	printf "* User %s doesn't exist. Creating... \n" "${previewUser}";
	. "${WP_SETUP}/project/05-create-user.sh"
fi


