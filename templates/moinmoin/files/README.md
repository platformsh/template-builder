# Platform.sh MoinMoin (Python 2.7) minimal example

This project provides a starter kit for hosting a MoinMoin wiki on Platform.sh. It is primarily an example, although it could be used as the starting point for a real project.

MoinMoin is a wiki engine written for Python 2.7. This project uses [MoinMoin 1.9.10](https://github.com/moinwiki/moin-1.9) and has been configured to run on Platform.sh. You can find more information about the MoinMoin project on [Github](https://github.com/moinwiki/moin-1.9) or on their [website](https://moinmo.in/).


## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.
 
2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it! You now have a working MoinMoin wiki project you can build on. 

By default, the front page of the wiki covers language setup, but that can be modified with an editable page by commenting out the line

```python
# page_front_page = u'FrontPage'
```

in `wikiconfig_local.py`. If you would like to change additional settings on the wiki, consult [`wikiconfig.py`](https://github.com/moinwiki/moin-1.9/blob/master/wikiconfig.py) and [`wikiserverconfig.py`](https://github.com/moinwiki/moin-1.9/blob/master/wikiserverconfig.py) on GitHub and include the modified lines in `wikiconfig_local.py` and `wikiserverconfig_local.py` respectively. 

Create an account from the `Login` tab and start editing!

## Using as a reference

You can also use this repository as a reference for your own projects, and borrow whatever code is needed. The most important parts are the `.platform.app.yaml` file and the `.platform` directory.
