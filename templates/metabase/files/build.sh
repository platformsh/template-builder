#!/bin/bash

# Load header
. ./header.inc

# Desired version can be set as an enviromental variable
if [ -z "$METABASE_VERSION" ]; then
  METABASE_VERSION=0.40.0;
fi

METABASE_DOWNLOAD_URI="http://downloads.metabase.com/v${METABASE_VERSION}"
METABASE_DL_ARCHIVE="metabase.jar"

# Make directories
mkdir -p $METABASE_HOME bin;

# Download Metabase
echo "Downloading ${METABASE_DOWNLOAD_URI}/${METABASE_DL_ARCHIVE}"
wget --no-cookies --no-check-certificate -q -O ${METABASE_HOME}/${METABASE_JAR} ${METABASE_DOWNLOAD_URI}/${METABASE_DL_ARCHIVE}

# jq is a utility that will be used to extract memory limits from a JSON data file.
# Desired version can be set as an enviromental variable
if [ -z "$JQ_VERSION" ]; then
  JQ_VERSION=1.5
fi

# Download and put it in the bin folder
JQ_DOWNLOAD_URI="https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}"
JQ_DL_ARCHIVE="jq-linux64"

# Download jq
echo "Downloading ${JQ_DOWNLOAD_URI}/${JQ_DL_ARCHIVE}"
wget ${JQ_DOWNLOAD_URI}/${JQ_DL_ARCHIVE} --no-cookies --no-check-certificate -q -O bin/jq
chmod +x bin/jq

# discovery & pathfinder are helpful little utilities
DISCOVERY_DOWNLOAD_URI="https://github.com/daniel-platform/discovery/releases/download/v0.1-alpha/discovery-debian-stretch"
PATHFINDER_DOWNLOAD_URI="https://github.com/daniel-platform/pathfinder/releases/download/v0.1-alpha/pathfinder-debian-stretch"

# Download and put it in the bin folder
echo "Downloading ${DISCOVERY_DOWNLOAD_URI}"
wget --no-cookies --no-check-certificate -q -O bin/discovery ${DISCOVERY_DOWNLOAD_URI}
echo "Downloading ${PATHFINDER_DOWNLOAD_URI}"
wget --no-cookies --no-check-certificate -q -O bin/pathfinder ${PATHFINDER_DOWNLOAD_URI}
chmod +x bin/pathfinder bin/discovery
