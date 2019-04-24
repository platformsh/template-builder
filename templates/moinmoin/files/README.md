# Platform.sh MoinMoin (Python 2.7) minimal example

This project provides a starter kit for hosting a MoinMoin wiki on Platform.sh. It is primarily an example, although it could be used as the starting point for a real project.

MoinMoin is a wiki engine written for Python 2.7. This project is a fork of [MoinMoin 1.9](https://github.com/moinwiki/moin-1.9/tree/master/wiki) configured to run on Platform.sh. You can find more information about the MoinMoin project on [Github](https://github.com/moinwiki/moin-1.9/tree/master/wiki) or on their [website](https://moinmo.in/).

All configuration files and page content are initialized here in `wiki`, but they are moved to the mounted directory `mywiki` during deployment so that the wiki engine is writable. 

By default, the starting page is `Language Setup`. To modify this to a blank `FrontPage` instead, uncomment the line

```python
# page_front_page = u'FrontPage'
```

in `wikiconfig.py`, or replace with another name that you want for your front page.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working MoinMoin wiki project you can build on. Create an account from the `Login` tab and start editing!

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.

http://static.moinmo.in/files/moin-1.9.10.tar.gz