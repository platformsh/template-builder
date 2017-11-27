all: update platformify branch push

clean:
	rm -rf template

init: clean
	# getting a shallow clone of a specific version
	git clone -b '1.29.2' --single-branch --depth 1 git@github.com:wikimedia/mediawiki.git template/web
	
update:
	cd template && git fetch --all --depth=1

platformify:
	#Removing all git artificats
	cd template && ( find . -type d -name ".git" && find . -name ".gitignore" && find . -name ".gitmodules" ) | xargs rm -rf
	#Create new git Repo and add enerything
	cd template && git init
	cd template && git add . && git commit -m'Import from github upstream'
	#Remove the stuff that shoulndn't be in production
	rm -rf template/web/cache
	rm -rf template/web/images
	rm -rf template/web/mw-config
	#Copy over Platform.sh configuration
	rsync -aP files/ template/
	#	patch  template/web/.gitignore <patches/0001-Apply-default-platform.sh-configuration.patch
	#The follofinw patch allows us to run the installation script although LocalSettings.php already exists
	patch template/web/includes/installer/CliInstaller.php < patches/0001-ignore-localsettings.patch
	cd template/web && composer update --no-dev
	#Unhelpfully composer based Skins end up in web/skins rather than vendor/ removing those
	cd template/web && (find . -type d -name ".git") | xargs rm -rf
	cd template && git add . && git commit -am'Apply default platform.sh configuration'

branch:
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
