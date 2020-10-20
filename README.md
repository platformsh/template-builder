# Utility scripts to manage the Platform.sh Template projects

## Introduction

Platform.sh maintains a set of deployable templates on https://github.com/platformsh-templates/. This utility eases the job of keeping them up-do-date.

In this document we use the fictional term "spiffy" as an example of a template name (ie drupal7, django3).

In this README we first focus on the workflow to update an existing template, then we describe how to create a new one.

> **Note:**
>
> For additional information about how specific similar templates are defined, see [notes.md](/notes.md).

## Dependencies

* [DoIt](http://pydoit.org/install.html)
* [Composer](https://getcomposer.org/) (for PHP projects)
* Git
* Public ssh key in github account

### Setup

1. First install the dependencies:
```
pipenv install
```
2. You will need to have your user added to the `platformsh-templates` github organisation in order to be able to push to these repositories.

## How it works

Each template is composed of three things:

* A repo to be kept up-to-date on https://github.com/platformsh-templates for example https://github.com/platformsh-templates/rails
* A python class that has the specific logic on how to update it. For example `project/rails.py`
* A template directory, for example `templates/rails` that contains the extra files we would add.

> Be aware that currently the build itself will happen in a `build` subdirectory of, for example `templates/rails`. So once you run any of the commands expect the output to be in `templates/rails/build`.

This project is built using the Python DoIt library, which is required.  It consists of a series of build targets for each supported project.  Taken together, the build process can reproduce a Platform.sh-friendly version of any application or framework from its upstream source.

### Organization

Each project is its own directory under `templates`, which corresponds to a GitHub repository of the same name in the `platformsh-templates` organization.  We'll use a fictional application called `spiffy` for this example.  The basic outline looks like this:

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
      .platform.template.yaml
      build/
```

Only the `files` directory, patches, and `.platform.template.yaml` are checked into Git.  The `build` directory is an artifact and excluded.

The `files` directory contains all the files that should be added wholesale to the upstream source of `spiffy`.  The patches will be applied to the the source to modify it.  Patches are optional and `files` could be as simple as just the Platform.sh configuration files, or it could be the entire repository with no upstream at all.

Additionally, each project may have a Python class defined in the `project` directory that controls its build process.  In most cases it only needs to specify an upstream source and possibly some custom build steps.  Projects with no upstream will often have no custom class at all.  See the `BaseProject` and `RemoteProject` classes for further details.

### Build tasks

Each project has a series of build tasks, suffixed with the project name.

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

## Conventions

Templates should all follow some standard conventions for consistency and easier documentability, even though technically the Platform.sh code doesn't care.  There may be case-by-case exceptions to these guidelines but the following should be followed unless there is a good reason otherwise.

* In single-application examples, the application name is always `app`.
* Service names should be named for the *use case* they are primarily for.  For example, the primary database for an application is a service named `db` (regardless if it's MySQL, MariaDB, PostgreSQL, or MongoDB).  The main cache service should be named `cache`.  The main search service is named `search`.  Etc.
* Relationship names should be named for the service type and use case.  Thus, a Redis service named `cache` will have a relationship name of `rediscache`.  A Solr service named `search` will have a relationship named `solrsearch`.  Etc.
* As an exception to the previous point, the relationship for the primary database is called simply `database` regardless of its type.  This is largely for historical reasons, and because 99% of the time no one cares about the type at that level.
* Always use the most recent version of a language or service container that the application supports.
* Always use the most up-to-date syntax and style for YAML files.  For instance, always use the newer nested `mount` syntax, not the old inline version.
* If including both a www-prefixed domain and not in `routes.yaml`, the bare domain should redirect to the www domain, not vice versa.

## Contributing

If you would like to contribute to the list of Platform.sh's maintained templates, there is a simple process for ensuring that future maintenance is set up from the start through `template-builder`.

Let's use the previous example: you have created a new application that uses the framework Spiffy that you think would be a useful template.

1. Create a repository under the [Platform.sh Templates organization](https://github.com/platformsh-templates/) for the template.  Create a repository named `spiffy` and initialize it with an empty `README.md`.  If you don't have access, ping someone on the DevRel team to create it for you.
2. Integrations: The DevRel team will create an integration during the review process, so you don't need to worry about having one set up.
3. Clone the [`template-builder` repository](https://github.com/platformsh/template-builder) locally. Create and checkout a new branch called `add-spiffy`.
4. Each template project is in its own directory within `templates`, which corresponds to a GitHub repository with the `template-` prefix. Create the directories `templates/spiffy` and `templates/spiffy/files/` on the `add-spiffy` branch.
5. Add only the files for `spiffy` into `templates/spiffy/files`, as dependency downloads and linking to an upstream repository can be handled by the Python build process. For example, the Drupal 9 template links to its upstream [here](https://github.com/platformsh/template-builder/blob/master/project/drupal.py). If your application requires any patches to deploy on Platform.sh, copy them into `templates/spiffy/`.
6. Include or update the `README.md` so that it is similar to other templates. Address any information specific to running the application on Platform.sh you think the customer should know.
7. Each template comes with a file called `.platform.template.yaml`, which is used to define how the template repository will appear in and initialize from the management console. See the example in the [external templates](https://github.com/platformsh/templates-external/blob/master/template-definition.yaml) repo for instructions.

    > **Note:** To create the image URI representing the template, find a svg formatted logo for Spiffy, [create a data URL](https://dataurl.sveinbjorn.org/#dataurlmaker) of that image and paste the output into `image:`.

8. Run the following commands to update the `spiffy` repository:

    ```bash
    cd <path>/template-builder
    doit full:spiffy
    ```

    This will create the branch `updates` on the repository`platformsh/template-spiffy` and push your application files to it.
9. Open a pull request for `updates` on `spiffy`.
10. Commit and push `add-spiffy` to the `template-builder` repository and create a pull request for it.
11. Paste a link to the `spiffy` PR in the `add-spiffy` PR on `template-builder` so they're easier to keep track of.
12. Paste the two PR links in the Slack `#devrel` channel and include the handle `@devrel_team` so that it will be reviewed.

## License

The license for the projects built by this tool vary.

All code unique to this repository is released under the [MIT License](LICENSE.md).
