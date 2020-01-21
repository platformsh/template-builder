# Strapi Template Notes  

## Build

This Strapi template is built using the `yarn create strapi-app tmp-app --quickstart --no-run` command to create a "Quickstart" project. This command is run during the build hook from the `files/backend/platformsh/build.sh` script.

Platform.sh-specific configuration is moved to the final build directory (`public`):

```
rm config/environments/development/database.json && mv platformsh/database.js config/environments/development/database.js
rm config/environments/development/server.json && mv platformsh/server.json config/environments/development/server.json
```

so that environment variables for `PORT` and PostgreSQL credentials can be used by Strapi.

###  `index.html`

The generated "Quickstart" project described above comes with a known issue: the `index.html` file created to direct users to create an admin user contains a bad link that links to `localhost:8000/admin` instead of just `/admin`. This is related to

* [PR 4822](https://github.com/strapi/strapi/pull/4822)
* [Issue 4791](https://github.com/strapi/strapi/issues/4791)

Currently, a working `index.html` file with a hard-coded `/admin` link is committed, and moved to `public/` within `build.sh`:

```
rm public/index.html && mv platformsh/index.html public/index.html
```

This is a temporary fix until the upstream issue has been updated for the `yarn create strapi-app` quickstart. Once available, this step can be removed. 
