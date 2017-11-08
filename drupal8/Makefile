

all: update platformify branch push

reset:
	rm -rf template

init: reset
	git clone git@github.com:platformsh/template-drupal8.git template
	cd template && git remote add upstream https://github.com/drupal-composer/drupal-project.git

update:
	cd template && git fetch --all --depth=2
	cd template && git merge --allow-unrelated-histories -X theirs --squash upstream/8.x
	cd template && composer install

platformify:
	rsync -aP files/ template/
	#if [ -e patch.patch ] \
    #then \
    #  patch -p1 source/platformsh.patch
    #fi

branch:
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
