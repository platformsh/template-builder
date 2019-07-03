# Flask for Platform.sh

This template builds a Flask project on Platform.sh, run natively without a separate runner.

## Services

* Python 3.7
* MariaDB 10.2
* Redis 3.2

## Customizations

The following files have been added to a basic Flask configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Pip library, [`platformshconfig`](https://github.com/platformsh/config-reader-python), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A rudimentary application is included in `server.py` for demonstration purposes.  It shows the basic process of starting the server and connecting to the MariaDB database.  Modify and replace it as desired.
