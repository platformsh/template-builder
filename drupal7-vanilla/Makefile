

all: update platformify branch push

clean:
	rm -rf template

init: clean
	git clone git@github.com:platformsh/template-drupal7-vanilla.git template

update:
	cd template && git checkout master
	wget -qO- https://ftp.drupal.org/files/projects/drupal-7.56.tar.gz | tar xzv --transform 's/^drupal-7.56/docroot/' -C template/

platformify:
	rsync -aP files/ template/
	cd template && patch -p1 < ../allow-settings-files.patch

branch:
	cd template && git branch -D update
	cd template && git checkout -b update
	cd template && git add -A && git commit -m "Update to latest upstream"

push:
	cd template && git checkout update && git push -u origin update
	cd template && hub pull-request -m "Update to latest upstream" -b master -h update
