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
