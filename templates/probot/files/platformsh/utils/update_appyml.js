const yaml = require('js-yaml');
const fs   = require('fs');
const config = require("platformsh-config").config();

const demo = true;

try {

  // Load the user-defined `app.yml` file (renamed during build hook to probot.app.yml).
  var doc = yaml.safeLoad(fs.readFileSync('probot.app.yml', 'utf8'));

  // Load Platform.sh demo strings.
  var platformsh_demo = yaml.safeLoad(fs.readFileSync('platformsh/demo/steps.yaml', 'utf8'));

  // If no description is given in the user-defined `app.yml` file, use the Platform.sh
  //   default template description.
  if (!("description" in doc)) {
    console.log("No description defined in manifest. Using Platform.sh default description.");
    doc.description = platformsh_demo.description;
  }

  // Create an app name for development environments.
  var bot_name = "";

  if (!("name" in doc)) {

    // Probot would do this automatically for master, but this allows a environment-specific
    //  name in addition to that standard.
    var packageParsed = JSON.parse(fs.readFileSync('package.json', 'utf8'));
    bot_name = packageParsed.name;

  } else {

    // If a user does supply an app name, append environments to that.
    bot_name = doc.name;
  }

  // Append the environment name to the app name.
  if ( process.env.PLATFORM_BRANCH != "master" ) {
    bot_name += ` (${process.env.PLATFORM_BRANCH})`;
  }

  doc.name = bot_name;

  // Over-ride the `hook_attributes.url` attribute in `app.yml` to help setup the registration.
  doc.hook_attributes = { url: config.getPrimaryRoute().url };

  // Update the file.
  fs.writeFileSync('app.yml', yaml.safeDump(doc), function (err) {
    if (err) throw err;
  });

} catch (e) {
  console.log(e);
}
