# Generic "download from remote source" script for Platform.sh.
# This script should be run during build to obtain a specific version
# of a Git repository at build time.

# The machine name of the application.  Will be used for directory names.
APP_NAME="discourse"
# The human-facing name of the application.  Will be used in printed messages.
APP_LABEL="Discourse"
# The relative directory within the $PLATFORM_APP_DIR where the appropriate version should be copied.
DESTINATION_DIR="discourse"
# The remote Git repository from which to pull.
GIT_URL="https://github.com/discourse/discourse.git"

run() {
    # Run the compilation process.
    cd $PLATFORM_CACHE_DIR || exit 1

    if [ ! -f "${PLATFORM_CACHE_DIR}/{$APP_NAME}" ]; then
        ensure_source
        checkout_version "$1"
    fi

    copy_source
}

copy_source() {
    echo "Installing ${APP_LABEL}."
    rsync -az --exclude=.git $PLATFORM_CACHE_DIR/$APP_NAME/* $PLATFORM_APP_DIR/$DESTINATION_DIR/
}

checkout_version() {
    # Check out the specific Git tag that we want to build.
    git checkout "$1"
}

ensure_source() {
    # Ensure that the extension source code is available and up to date.
    if [ -d "$APP_NAME" ]; then
        cd $APP_NAME || exit 1
        git fetch --all --prune
    else
        git clone $GIT_URL $APP_NAME
        cd $APP_NAME || exit 1
    fi
}

compile_source() {
    # Compile the extension.
    phpize
    ./configure
    make
}

ensure_environment() {
    # If not running in a Platform.sh build environment, do nothing.
    if [ -z "${PLATFORM_CACHE_DIR}" ]; then
        echo "Not running in a Platform.sh build environment.  Aborting {$APP_LABEL} installation."
        exit 0
    fi
}

ensure_arguments() {
    # If no version was specified, don't try to guess.
    if [ -z $1 ]; then
        echo "No version of {$APP_LABEL} specified.  You must specify a tagged version on the command line."
        exit 1
    fi
}

ensure_environment
ensure_arguments "$1"
run "$1"
