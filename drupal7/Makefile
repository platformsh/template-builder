

all: update platformify branch push

clean:
	rm -rf template

init: clean
	git clone git@github.com:platformsh/template-drupal7.git template

update:
	echo "Nothing to update"

platformify:
	rsync -aP files/ template/

branch:
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
