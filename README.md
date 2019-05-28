# Utility scripts to manage the Platform.sh Template projects

## Dependencies

* [DoIt](http://pydoit.org/install.html)
* [Composer](https://getcomposer.org/) (for PHP projects)
* Git
* Public ssh key in github account

## How it works

This project is built using the Python DoIt library, which is required.  It consists of a series of build targets for each supported project.  Taken together, the build process can reproduce a Platform.sh-friendly version of any application or framework from its upstream source.

### Organization

Each project is its own directory under `templates`, which corresponds to a `template-*` GitHub repository of the same name in the `platformsh` organization.  We'll use a fictional application called `spiffy` for this example.  The basic outline looks like this:

```text
/
  project/
    spiffy.py
  templates/
    spiffy/
      files/
        .platform/
        .platform.app.yaml
        ...
      fix1.patch
      fix2.patch
      build/
```

Only the `files` directory and patches are checked into Git.  The `build` directory is an artifact and excluded.

The `files` directory contains all the files that should be added wholesale to the upstream source of `spiffy`.  The patches will be applied to the the source to modify it.  Patches are optional and `files` could be as simple as just the Platform.sh configuration files, or it could be the entire repository with no upstream at all.

Additionally, each project has a Python class defined in the `project` directory that controls its build process.  In most cases it only needs to specify an upstream source and possibly some custom build steps.  See the `BaseProject` and `RemoteProject` classes for further details.

### Build tasks

Each project has a series of build tasks, suffixed with the project.

* `cleanup:spiffy` - Deletes the build directory for `spiffy` to start from a clean slate.
* `init:spiffy` - Checks out the Platform.sh template and links it in Git with the project's upstream. Implies `cleanup:spiffy`.
* `update:spiffy` - Pulls down the latest code from the upstream source and merges it into the build directory, overwriting files if necessary.
* `platformify:spiffy` - Copies the `files` directory over the build directory to add the Platform.sh files, applies any patches, and potentially takes other actions as needed.  (Adding composer libraries, for instance.)  This may vary widely with the application.
* `branch:spiffy` - Prepares a branch named `update` with the changes just made by `update` and `platformify`, with all changes committed.
* `push:spiffy` - Pushes a branch to GitHub, which displays a link to create a Pull Request out of it.

* `rebuild:spiffy` - Implies `update:spiffy`, `platformify:spiffy`, and `branch:spiffy`.
* `full:spiffy` - Runs `cleanup:spiffy`, `init:spiffy`, `update:spiffy`, `platformify:spiffy`, `branch:spiffy`, `push:spiffy`.

A particular task is run across all projects in case the project is not specified.  That is, the following will clean-and-initialize all projects:

* `init` - Runs init task for all the projects.

In most cases, rebuilding a new update to a project is a matter of running:

`doit full:spiffy`

And poof, you are ready to make a PR with the updates.

## Test environments

Template projects are hooked up to Platform.sh projects, so each new PR gets built as a new, empty environment ready for testing.  In most cases simply visiting the built site and verifying that the installer can run (if available) or that the site gives the appropriate "there's nothing here yet" error is sufficient, but further testing can be done if needed.


## Contributing

If you would like to contribute to the list of Platform.sh's maintained templates, there is a simple process for ensuring that future maintenance is set up from the start through `template-builder`.

Let's use the previous example: you have created a new application that uses the framework Spiffy that you think would be a useful template. 

1. Create a repository under the [Platform.sh Github organization](https://github.com/platformsh/) for the template. Officially maintained templates begin with the `template-` prefix, so name it `template-spiffy`, and initialize it with an empty `README.md`.
2. Add the "Examples and Templates team" as `Admin` collaborators in the `platformsh/template-spiffy` repository settings.
3. Set up GitHub integration for the repository. When you submit your template for review it will helpful if there is already a live site that shows what the application would look like to customers and that it deploys properly. You can find information about how to set up a [GitHub integration](https://docs.platform.sh/administration/integrations/github.html#github) in the documentation. Create a blank project on your Platform.sh account called `template-spiffy` on the region "Europe (West 3)" (`eu-3.platform.sh`) and set up the integration.
4. Clone the [`template-builder` repository](https://github.com/platformsh/template-builder) locally. Create and checkout a new branch called `add-spiffy`.
5. Each template project is in its own directory within `templates`, which corresponds to a GitHub repository with the `template-` prefix. Create the directories `templates/spiffy` and `templates/spiffy/files/` on the `add-spiffy` branch. 
6. Add only the files for `template-spiffy` into `templates/spiffy/files`, as dependency downloads and linking to an upstream repository can be handled by the Python build process. For example, the Drupal 8 template links to its upstream [here](https://github.com/platformsh/template-builder/blob/new-template-instructions/project/drupal.py). If your application requires any patches to deploy on Platform.sh, copy them into `templates/spiffy/`. 
7. Include or update the `README.md` so that it is similar to other templates, and include any information specific to running the application on Platform.sh you think the customer should know.
8. Each template comes with a file called `.platform.templates.yaml`, which is used to define how the template repository will appear in and initialize from the management console. Take a look at how the file is written for the [Drupal 8 template](https://github.com/platformsh/template-builder/blob/new-template-instructions/templates/drupal8/files/.platform.template.yaml) as an example.

    > **Note:** To create the image URI representing the template, find a svg formatted logo for Spiffy, [create a data URL](https://dataurl.sveinbjorn.org/#dataurlmaker) of that image and paste the output into `image:`.

9. Run the following commands to update the `template-spiffy` repository:

    ```bash
    cd <path>/template-builder
    doit full:spiffy
    ```

    This will create the branch `updates` on `template-spiffy` and push your application files to it.
10. Open a pull request for `updates` on `template-spiffy`.
11. Commit and push `add-spiffy` to the `template-builder` repository and create a pull request for it.
12. Copy and paste the two PR links in the Slack `#devrel` channel so that it can be reviewed. 
