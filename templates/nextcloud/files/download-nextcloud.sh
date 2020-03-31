# Generic "download from remote source" script for Platform.sh.
# This script should be run during build to obtain a specific version
# of a Git repository at build time.

# The machine name of the application.  Will be used for directory names.
APP_NAME="nextcloud"
# The human-facing name of the application.  Will be used in printed messages.
APP_LABEL="Nextcloud"
# The relative directory within the $PLATFORM_APP_DIR where the appropriate version should be copied.
DESTINATION_DIR="src"

run() {
    ensure_environment
    ensure_arguments "$1"

    # Run the compilation process.
    cd $PLATFORM_CACHE_DIR || exit 1;

    DOWNLOAD_URL="https://download.nextcloud.com/server/releases/nextcloud-${1}.tar.bz2"

    ensure_download "${DOWNLOAD_URL}" "$1"
    ensure_unpack "$1"
    copy_source "$1"
}

copy_source() {
    echo "Installing ${APP_LABEL}."
    rsync -az --exclude=.git $PLATFORM_CACHE_DIR/$APP_NAME/* $PLATFORM_APP_DIR/$DESTINATION_DIR/
}

ensure_download() {
    # Ensure that the source code is available and up to date.
    if [ ! -f "${PLATFORM_CACHE_DIR}/${APP_NAME}-${2}.tar.bz2" ]; then
        echo "Downloading ${APP_LABEL} archive."
        wget "$1"
        # If the version has changed, we'll want to make sure to not confuse it with the old one.
        rm "${APP_NAME}"
    fi
}

ensure_unpack() {
    # Ensure that the source code has been decompressed.
    if [ ! -d "${PLATFORM_CACHE_DIR}/${APP_NAME}" ]; then
        echo "Unpacking ${APP_LABEL}."
        tar xjf "${APP_NAME}-${1}.tar.bz2"
    fi
}

ensure_environment() {
    # If not running in a Platform.sh build environment, do nothing.
    if [ -z "${PLATFORM_CACHE_DIR}" ]; then
        echo "Not running in a Platform.sh build environment.  Aborting ${APP_LABEL} installation."
        exit 0;
    fi
}

ensure_arguments() {
    # If no version was specified, don't try to guess.
    if [ -z $1 ]; then
        echo "No version of ${APP_LABEL} specified.  You must specify a tagged version on the command line."
        exit 1;
    fi
}

run "$1"
