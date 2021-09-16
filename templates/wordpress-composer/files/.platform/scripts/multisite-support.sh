#!/usr/bin/env bash
MLTISITEINSTLDVARNAME="MULTISITEINSTALLED"
HOOK=$1
PHPFILENAME="multisite.php"
PHPFILELOC="/tmp/"

function createPHPFile() {
	printf "<?php \n" > "${PHPFILELOC}${PHPFILENAME}"
}

function displayEnvMessage() {
    printf "Please add an environmental variable of \`%s\` to your project with a value of \`true\`\n" "$MLTISITEINSTLDVARNAME"
    printf "You can do so by either adding it to your .platform.app.yml file, adding it via the cli tool, or adding it from the console.\n"
}

function build() {
	printf "It appears you want a multisite but the multisite hasn't been set up yet. Creating the supporting files... \n"
	#now that we know we have our file there, let's copy in our multisite.php file
	printf "Copying in our %s file... \n" "${PHPFILENAME}"
	#ok, why are we copying the empty file into /tmp if we know /tmp is going to get cleared?
	#because our ini file is set to include a file. if something goes wrong during the deploy step, things will blow
	#up. at least this way, it'll append and empty file, and everything will still work :D
	createPHPFile
	#now create our symlink
	ln -s -f "${PHPFILELOC}${PHPFILENAME}" "${PLATFORM_DOCUMENT_ROOT}"/"${PHPFILENAME}"

	#now we'll add the line about prepending our script to all php calls
	printf "Adding auto_prepend_file to our php.ini file...\n"

	#this file is only called *IF* our env var isn't set, so if they dont have an ini file already, let's copy ours in
	if [[ ! -f "${PLATFORM_APP_DIR}"/php.ini ]]; then
		printf "There isnt a php.ini in app root so we'll create one...\n"
		touch "${PLATFORM_APP_DIR}/php.ini"
	fi

	echo "auto_prepend_file = ${PLATFORM_DOCUMENT_ROOT}/${PHPFILENAME}" >> "${PLATFORM_APP_DIR}"/php.ini
}

function deploy() {
    local PHPFILE="${PHPFILELOC}${PHPFILENAME}"
    # we first need to make sure we have a copy of the file in /tmp/
    #ok, there *shouldnt* already be a file there, but let's make sure
    if [[ -f "${PHPFILE}" ]]; then
    	rm -f "${PHPFILE}"
    fi

    #now add a fresh copy
    createPHPFile

		#is this a subdomain or subdirectory multisite?
		if $SUBDOMAIN_INSTALL; then
			printf "\nThis is a sub/multi-domain site...\n"
			SUBDOMAIN=true;
		fi

		#now we'll actually try to convert it
		CONVERSION=$(wp core multisite-convert ${SUBDOMAIN:+--subdomains} 2>&1)
		LASTCOMMAND=$?

		if (( 1 == $LASTCOMMAND)); then
			# send info to the deploy log
			printf "FAILED CONVERTING SITE TO MULTISITE.\nMessage:\n%s" "$CONVERSION";
			return 1;
		else
			#Does it even matter if it was already a multisite?
			if [[ $CONVERSION =~ ${PTRNALREADYINSTALLED} ]]; then
				printf "Your site is already a multisite but your %s environmental variable is missing. I'll take care of you this time, but please add it.\n" "$MLTISITEINSTLDVARNAME"
			else
				printf "Site successfully converted to multisite.\n"
			fi

			printf "Adding the %s environmental variable via putenv into our multisite file... \n" "$MLTISITEINSTLDVARNAME"
			echo "putenv(\"${MLTISITEINSTLDVARNAME}=true\");" >> "${PHPFILE}"
			chmod 0444 "${PHPFILE}"
			#add the env for them?
			displayEnvMessage
		fi

		return 0
}



# if the multisite installed env isnt set but multisite is and true, then:
# The site is already converted but the env var is missing so we need to  add it, OR
# we need to convert the install to multisite
if [[ -z ${MULTISITEINSTALLED+x} ]] && [[ -n ${MULTISITE+x} ]] && [[ "$MULTISITE" == "true" ]]; then
	RETURN=1;
	if [[ "build" == "${HOOK}" ]]; then
		build
		RETURN=$?
	elif [[ "deploy" == "${HOOK}" ]]; then
		deploy
		RETURN=$?
	fi
	exit ${RETURN}
fi
