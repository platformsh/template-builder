#!/usr/bin/env bash
########################################################################################################################
# NOTE:
#
# On a new install sets permalink structure to the value stored in settings.default.json at .project.permalink.structure
# Default is "Day and name" structure (e.g. https://site.com/2022/05/25/sample-post/)
#
########################################################################################################################
permaKey=$(jq -r '.project.permalink.option_key' < "${ENV_SETTINGS}");
permaStructure=$(jq -r '.project.permalink.structure' < "${ENV_SETTINGS}");

wp option update "${permaKey}" "${permaStructure}" && wp rewrite flush

