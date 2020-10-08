# Strapi Template Notes  

This Strapi template is built using the `yarn create strapi-app tmp-app --quickstart --no-run` command to create a "Quickstart" project. There's no tagged dedicated repository for this project, rather its created between a few [Strapi packages](https://github.com/strapi/strapi/tree/master/packages) through Yarn. So, the `create` command is actually run as a part of the `update` task for `project/strapi.py`. 

## `sharp`, `node-gyp`, and OSX Catalina

There is definite weirdness introduced in the most recent versions of `node-gyp`, which is used by the `create` yarn process on OSX 10.15.X Catalina. You will need XCode Command Line Tools, and likely the larger XCode app to run the `create` in the first place, even outside of template-builder. I have read that this process will also hang up on a local Node.js installation greater than 12, but have not verified myself. 

This doesn't cause any problems when running the development server or building when the project has already been put together. I have only encountered it when creating the app itself from upstream in the first place.

### Common output

```
error /Users/chadcarlson/Documents/repos/github.com/platformsh/something/node_modules/sharp: Command failed.
Exit code: 126
Command: (node install/libvips && node install/dll-copy && prebuild-install) || (node-gyp rebuild && node install/dll-copy)
Arguments: 
Directory: /Users/chadcarlson/Documents/repos/github.com/platformsh/something/node_modules/sharp
Output:
info sharp Detected globally-installed libvips v8.10.1
info sharp Building from source via node-gyp
/usr/local/lib/node_modules/npm/bin/node-gyp-bin/node-gyp: line 5: /usr/local/lib/node_modules/node-gyp: is a directory

 Keep trying!             

Oh, it seems that you encountered errors while installing dependencies in your project.
Don't give up, your project was created correctly.
Fix the issues mentionned in the installation errors and try to run the following command:

cd /Users/chadcarlson/Documents/repos/github.com/platformsh/something && yarn install

error Command failed.
Exit code: 1
Command: /usr/local/bin/create-strapi-app
Arguments: something --quickstart --no-run
Directory: /Users/chadcarlson/Documents/repos/github.com/platformsh
Output:

info Visit https://yarnpkg.com/en/docs/cli/create for documentation about this command.
```

### Relevant links

- [`node-gyp`](https://github.com/nodejs/node-gyp#on-macos)
- [Catalina Troubleshooting](https://github.com/nodejs/node-gyp/blob/master/macOS_Catalina.md)
- After considering the recommendations for local XCode installation above, the most common issue I came across was `node-gyp`s compilation of `sharp`, used by the Strapi quickstart process. Visit its [building from source](https://sharp.pixelplumbing.com/install#building-from-source) documentation for details. Very likely, the fix (after all of the above) is to set an environment variable to force compilation during `npm install/yarn`, instead of trying to use a global installation of `sharp`.

### Environment variables

After going through the above for XCode, you may need to set an enviroment variable to fix the problem with `sharp` on Catalina. 

```
export SHARP_IGNORE_GLOBAL_LIBVIPS=true
```
