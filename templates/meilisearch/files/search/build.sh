#!/usr/bin/env bash

install_meilisearch() {
    # Check Platform.sh variable, to vary installation based on local v. Platform.sh
    echo "* INSTALLING MEILISEARCH"
    # Replicates Meilisearch download (https://github.com/meilisearch/MeiliSearch/blob/master/download-latest.sh) with locked version.
    release_file="meilisearch-linux-amd64"
    curl -OL "https://github.com/meilisearch/MeiliSearch/releases/download/$MEILISEARCH_VERSION/$release_file"
    mv "$release_file" "meilisearch"
    chmod 744 "meilisearch"
}

setup_venv(){
    echo "* SETTING UP POETRY VENV"
    # Install poetry
    curl https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py >> get-poetry.py
    python get-poetry.py --version $POETRY_VERSION
    # Source the Poetry command and cleanup.
    . $PLATFORM_APP_DIR/.poetry/env && rm get-poetry.py
    # Install dependencies.
    poetry install
}

install_meilisearch
setup_venv
