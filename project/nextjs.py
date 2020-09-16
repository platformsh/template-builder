from . import BaseProject

class Nextjs(BaseProject):
    # The BaseProject `update` task will loop through a list of `updateCommands` for 
    # a number of different language package managers and run them if their respective
    # dependency files (i.e. package.json) are present. 
    # 
    # Node.js has two popular package mangers - npm and yarn. Both use package.json to 
    # define dependencies, but resolve to different lock files (package-lock.json & yarn.lock).
    # When deployed, we'll only be using one of them, and it's generally recommended to not have
    # lock files from both package managers present in the same repo. 
    # 
    # Next.js also recommends the use of yarn over npm. 
    # 
    # Because `update` loops through `updateCommands`, simply adding an upgrade command for
    # yarn will result in that exact situation we'd like to avoid. 
    # 
    # So, `updateCommands` is redefined here for  Next.js to avoid all of that.
    updateCommands = {
        'yarn.lock': 'yarn upgrade'
    }
