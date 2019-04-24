# Writable Content

Platform.sh provides a read-only file system, but writable storage is provided by defining [mounts](https://docs.platform.sh/configuration/app/storage.html#basic-mounts) in your `.platform.app.yaml` file.

The only content of your wiki (`mywiki`) that will be writable involves page content, which is controlled in `mywiki/data` and `mywiki/underlay`.

