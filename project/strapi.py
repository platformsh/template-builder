from . import BaseProject
import os

class Strapi(BaseProject):

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):

        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TEMPLATEDIR = os.path.join(ROOTDIR, 'templates/strapi')

        # Quickstart project package name, used in the block below.
        projectName = "strapi-quickstart-platformsh"

        return [
            # Create a quickstart Strapi app using Yarn, since there's no dedicated upstream repo for it. Strapi prevents you 
            # from creating a new project in a nonempty dir, so the quickstart project is made in projectName before its
            # contents are copied into builddir. 
            'cd {0} && yarn create strapi-app {1} --quickstart --no-run'.format(TEMPLATEDIR, projectName),
            'cd {0} && cp -r {1}/{2}/* .'.format(self.builddir, TEMPLATEDIR, projectName),
            'rm -rf {0}/{1}'.format(TEMPLATEDIR, projectName),              
        ] + super(Strapi, self).update

    @property
    def platformify(self):

        return super(Strapi, self).platformify + [
            # Add dependencies. 
            'cd {0} && yarn add platformsh-config pg'.format(self.builddir),  
            'cd {0} && yarn strapi install graphql'.format(self.builddir),  
        ]

class Eleventy_strapi(BaseProject):
    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }
