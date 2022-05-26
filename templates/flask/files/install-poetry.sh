#!/usr/bin/env bash

# Install poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py >> install-poetry.py
python install-poetry.py --version $POETRY_VERSION
# Source the Poetry command.
. $PLATFORM_APP_DIR/.poetry/env
# Add Poetry to .bash_profile, so available during SSH.
echo ". $PLATFORM_APP_DIR/.poetry/env" >> ~/.bash_profile
