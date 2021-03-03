from . import BaseProject

class Strapi(BaseProject):

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):

        # Quickstart project package name, used in the block below.
        projectName = "strapi-quickstart-platformsh"

        return [
            # Create a quickstart Strapi app using Yarn, since there's no dedicated upstream repo for it. Strapi prevents you 
            # from creating a new project in a nonempty dir, so the quickstart project is made in projectName before its
            # contents are copied into builddir. 
            'cd {0} && yarn create strapi-app {1} --quickstart --no-run'.format(self.builddir, projectName),
            'cd {0} && cp -r {1}/ {0}'.format(self.builddir, projectName),
            'cd {0} && rm -rf {1}'.format(self.builddir, projectName),              
        ] + super(Strapi, self).update

    @property
    def platformify(self):

        return super(Strapi, self).platformify + [
            # Add dependencies. 
            'cd {0} && yarn add platformsh-config pg && yarn strapi install graphql documentation'.format(self.builddir),  
        ]

class Eleventy_strapi(BaseProject):
    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }
