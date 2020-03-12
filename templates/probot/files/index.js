const yaml = require('js-yaml');
const fs   = require('fs');
/**
 * This is the main entrypoint to your Probot app
 * @param {import('probot').Application} app
 */
module.exports = app => {
  // Your code here
  app.log('Yay, the app was loaded!')

  var platformsh = yaml.safeLoad(fs.readFileSync('platformsh/demo/steps.yaml', 'utf8'));

  app.on('issues.opened', async context => {
    const issueComment = context.issue({ body: platformsh.issue_opened })
    return context.github.issues.createComment(issueComment)
  })

  // For more information on building apps:
  // https://probot.github.io/docs/

  // To get your app running against GitHub, see:
  // https://probot.github.io/docs/development/
}
