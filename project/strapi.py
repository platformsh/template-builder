from . import BaseProject

class Strapi(BaseProject):

    # Keeps package-lock.json out of the repo as recommended. See project/nextjs.py for more info.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):

        # Quickstart project package name, used in the block below.
        projectName = "strapi-quickstart-platformsh"

        return [
            # Create a quickstart Strapi app using Yarn. There's no dedicated upstream repo, so best way to get up-to-date version.
            'cd {0} && yarn create strapi-app {1} --quickstart --no-run --build-from-source'.format(self.builddir, projectName),
            # Strapi prevents you from creating a new project in a nonempty dir. This moves the project into the builddir.
            'cd {0} && cp -r {1}/ {0} && rm -rf {1}'.format(self.builddir, projectName),           
        ] + super(Strapi, self).update

    @property
    def platformify(self):

        return super(Strapi, self).platformify + [
            # Add dependencies. 
            'cd {0} && yarn add platformsh-config pg && yarn strapi install graphql documentation'.format(self.builddir),  
        ]
