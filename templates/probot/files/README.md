# Probot GitHub Apps for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/probot/.platform.template.yaml&utm_content=probot&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a simple GitHub App using [Probot](https://github.com/probot/probot) for Node.js.  It includes a minimalist skeleton GitHub app that demonstrates a basic GitHub connection response.  It is intended for you to use as a starting point and modify for your own needs.

Note that there are several setup steps required after first deploy to connect your project to GitHub.  See the included README file for details.

Probot is a framework for building GitHub Apps in Node.js.

## Features

* Node.js 12
* Automatic TLS certificates
* npm-based build

## Post-install

1. **Register the App on GitHub**

   When the app has deployed, you will need to first register the app with GitHub by clicking the **Register GitHub App** button on the homepage. Name the application anything you like, then click the **Create GitHub App** button. This will automatically save your `WEBHOOK_SECRET`, `PRIVATE_KEY`, and `APP_ID` variables to a `.env` file in your Platform.sh environment.

   Typically, any file in your project root would be read-only at runtime, but here it is symlinked to a writable mounted file when `platformsh/setup/build.sh` is run during the build hook. Since it is writable, your temporary credentials can be written to the app at runtime and you can complete registration. These credentials will automatically be replaced by environment variables in Steps 3 and 4. After that, and since Probot uses `dotenv` to read its environment variables, these proper environment variables will always be prioritized over anything in `.env`. You can feel free to delete this file, and otherwise be unconcerned on whether its values are overwritten.

2. **Clone repository locally**

   Return to the management console for the project. Enter the master environment and copy the clone command under the `GIT` dropdown  button.

3. **Set up for production: Adding an API token**

   A great thing about GitHub Apps on Platform.sh is that you are not only able to setup a production application, but that you can also have `staging` and `development` versions of your application, themselves just as production-ready as your `master` branch, that you can test on GitHub.

   All of the credentials we have received from GitHub at this point sit in directories with write access at the moment, and they would be overwritten once we start branching and merging our apps.

   Luckily, it\'s very easy to install the Platform.sh into your application container, and set environment variables specific to each branch that will not be overwritten. All of the code to install the CLI is already in this demo, all you need to do is add an API token to the project and Platform.sh will take care of the rest.

   Follow the [instructions in our public documentation](https://docs.platform.sh/development/cli/api-tokens.html#obtaining-a-token) to create an API token.

   Once you have that token, copy it into the command below.

   ```
   platform variable:create --level project --name env:PLATFORMSH_CLI_TOKEN --sensitive true --value YOUR_API_TOKEN
   ```

   You will only need to add your API token once to a project. After it has been added, every branch will be able to add environment variables automatically with no further changes necessary.

4. **Set up for production: setting `NODE_ENV`**

   Inside the local repository, find the `.environment` file. You will see that `NODE_ENV` is currently set for `development`.

   Update that file to read `NODE_ENV="production"`. Once you have done that, commit and push the change.

   ```
   git commit -am "Set for production" && git push origin master
   ```

   Now that you have done that, you will see that as soon as the build of your commit completes, a number of other activities will open for the environment as environment variables are set that allow GitHub to recognize your app.

5. **Verify**

   When the final redeployment has completed, and all of your environment variables have been added, go back to your GitHub App's advanced settings.

   You will see that the first delivery it attempted to deliver to Platform.sh failed while you were registering.

   Expand the previous failed delivery by clicking the three dots, and then click **Redeliver** and then **Yes, repeat this delivery** to repeat the delivery. Since you have set up the app for production, it should now show a `200` successful response.

   Scroll to the bottom of the "General" settings page and click the "Active" checkbox so that GitHub can start sending more deliveries once it's installed on a repository.

6. **Test on a repository**

   Visit your application's public page (`https://github.com/apps/APPLICATION_NAME`) and click **Install**. For now, select the **Only select repositories** option and choose a repository to test the application on.

   Go to the repository you chose and open a new issue. Your app should now be listening for newly opened issues, and has delivered a response in a comment.

## Customizations

The following files have been added to a basic Probot configuration. If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.

## Setup

```sh
# Install dependencies
npm install

# Run the bot
npm start
```

## References

* [Probot](https://probot.github.io/)
