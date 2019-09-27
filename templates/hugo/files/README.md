# Hugo for Platform.sh

This template provides a basic Hugo skeleton.  All files are generated at build time, so at runtime only static files need to be served.

Hugo is a static site generator written in Go, using Go's native template packages for formatting.

## Services

* Go 1.13

## Post-install

The `content` directory includes two pieces of sample content, provided so that the initial install has some content to show.  Replace it with your actual content as desired.

You can also remove the `minimal` theme if you so desire and replace it with one you download or one you create yourself.

## Customizations

The following changes have been made relative from initializing a new Hugo project with `hugo new site`. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* The `minimal` theme has been included by default.  Feel free to remove it and replace with your own if you prefer.  Consult the Hugo documentation for instructions on how to add and enable themes.

## References

* [Hugo](https://gohugo.io/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
