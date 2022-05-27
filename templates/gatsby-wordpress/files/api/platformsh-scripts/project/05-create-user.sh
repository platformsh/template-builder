#!/usr/bin/env bash

wpGrapqlUser=$(jq -r '.environment.consumer.name' < "${ENV_SETTINGS}");
wpGraphqlEmail=$(jq -r '.environment.consumer.email' < "${ENV_SETTINGS}");
wpGrahpqlUserDescription=$(jq -r '.environment.consumer.description' < "${ENV_SETTINGS}")
# wp user create <user-login> <user-email> [--role=<role>]
# create our user that will communicate via GraphQL - HAS to be an administrator in order to retrieve draft posts
# @todo error check?
wpGraphqlUserID=$(wp user create "${wpGrapqlUser}" "${wpGraphqlEmail}" --role=administrator --porcelain)
printf "    ✔ Created the account %s to use for previewing posts.\n" "${wpGrapqlUser}"
# add our description to the user so they know not to delete or remove
printf "    ✔ Adding description to user %s\n" "${wpGrapqlUser}"
wp user meta update "${wpGraphqlUserID}" description "${wpGrahpqlUserDescription}"

# save the users' ID
UPDATED_SETTINGS=$(jq --arg CONSUMER_ID "${wpGraphqlUserID}" '.environment.consumer.id = $CONSUMER_ID' "${ENV_SETTINGS}")
echo "${UPDATED_SETTINGS}" > "${ENV_SETTINGS}"
