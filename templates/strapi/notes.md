# Strapi Template Notes  

## Build

This Strapi template is built using the `yarn create strapi-app tmp-app --quickstart --no-run` command to create a "Quickstart" project during the build hook. 

Platform.sh-specific configuration is moved during the build hook to overrided the Quickstart defaults. 

```
# Override with Platform.sh-specific configuration.
cp platformsh/database.js config/database.js
cp platformsh/server.js config/server.js
```
