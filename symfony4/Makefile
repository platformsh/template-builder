

all: update platformify branch push

clean:
	rm -rf template

init: clean
	git clone git@github.com:platformsh/template-symfony4.git template
	cd template && git remote add upstream https://github.com/symfony/skeleton.git

update:
	cd template && git fetch --all --depth=2
	cd template && git merge --allow-unrelated-histories -X theirs --squash upstream/4.0
	cd template && composer install --no-interaction

platformify:
	rsync -aP files/ template/
	composer require platformsh/symfonyflex-bridge

branch:
	if git show-ref --verify --quiet "refs/heads/${1:?update}"; then cd template && git branch -D update; fi;
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
