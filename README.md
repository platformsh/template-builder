# Utility scripts to manage the Platform.sh Template projects.

## Dependencies:
* [hub command-line wrapper](https://hub.github.com/)
* [doit](http://pydoit.org/install.html)
* Public ssh key in github account

## How to run:
```
$ cd template-builder
# init all projects
$ doit all_init
# init one project (see list of projects in ALL_PROJECTS variable)
$ doit drupal8_init
# pull any updates from upstream, apply custom platform changes, and checkout a new branch
$ doit drupal8
# if making a change with nothing from upstream, checkout a new branch to add your changes
$ doit drupal8_branch
# and create a PR (will hang if not logged into hub)
$ doit drupal8_push
```
