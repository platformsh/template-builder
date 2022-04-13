#!/usr/bin/env bash

TEMPLATE=$1
echo $TEMPLATE

# Create a build dir. 
poetry run doit cleanup:$TEMPLATE
poetry run doit init:$TEMPLATE
poetry run doit update:$TEMPLATE
poetry run doit platformify:$TEMPLATE

# Update migrations.
poetry run python migrate.py $TEMPLATE

# Update the README and header image.
poetry run python readme-builder.py $TEMPLATE

# Update the template and push it.
# poetry run doit full:$TEMPLATE