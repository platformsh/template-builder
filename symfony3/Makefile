

all: update platformify branch push

clean:
	rm -rf template

init: clean
	git clone git@github.com:platformsh/template-symfony3.git template
	cd template && git remote add upstream https://github.com/symfony/symfony-standard.git

update:
	cd template && git fetch --all --depth=2
	cd template && git merge --allow-unrelated-histories -X theirs --squash upstream/3.4
	cd template && composer install --no-interaction

platformify:
	rsync -aP files/ template/
	cd template && patch -p1 < ../parameters.patch

branch:
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
