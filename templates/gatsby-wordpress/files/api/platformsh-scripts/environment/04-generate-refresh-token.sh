#!/usr/bin/env bash
########################################################################################################################
# NOTE:
#
# Generates a refresh token nextjs can use to retrieve draft posts in order to generate post previews
#
# We need to get a refresh token from wp-graphql-jwt-authentication plugin and then store it as an environmental
# variable named WORDPRESS_AUTH_REFRESH_TOKEN that is loaded into the nextjs app container.
#
########################################################################################################################

previewUser=$(jq -r '.environment.consumer.name' < "${ENV_SETTINGS}");
previewAppName=$(jq -r '.environment.consumer.application_password_name' < "${ENV_SETTINGS}")
wpGraphqlURL=$(jq -r '.environment.api.url.graphql' < "${ENV_SETTINGS}")

# see if we already have an password for the given app name, if so, delete it
# We dont want to store a *password* on the file system, and we can't set or update an application password. Therefore,
# since we have to have the actual password to create the wpgraphql refresh token, we'll have to delete the old password
# and recreate it, so we can temporarily hold the password to give to wpgrapql
if $(wp user application-password exists "${previewUser}" "${previewAppName}"); then
	printf "   ✔ Removing previous application password %s...\n" "${previewAppName}"
	# in order to delete the app password so we can recreate it, we have to retrieve its uuid first
	previewAppUUID=$(wp user application-password list "${previewUser}" --name="${previewAppName}" --fields=uuid --format=csv | tail -n +2)
	# now we can delete it
	wp user application-password delete "${previewUser}" "${previewAppUUID}"
fi

printf "   ✔ Creating application password %s for user %s...\n" "${previewAppName}" "${previewUser}"

# we need to create and store an application password that we can then turn around and use with graphql to get a refresh token
previewAppPassword=$(wp user application-password create "${previewUser}" "$previewAppName" --porcelain)

printf "   ✔ Creating refreshToken for user %s...\n" "${previewUser}"

wpAuthRereshToken=$(wp graphql_auth get-graphql-token "${previewUser}" "${previewAppPassword}" --porcelain)

printf "   ✔ Saving refreshToken for user %s...\n" "${previewUser}"
UPDATED_SETTINGS=$(jq --arg WPTOKEN "${wpAuthRereshToken}" '.environment.consumer.secret = $WPTOKEN' "$ENV_SETTINGS")
echo "${UPDATED_SETTINGS}" > "$ENV_SETTINGS"
