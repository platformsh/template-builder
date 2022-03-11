from . import BaseProject
from .remote import RemoteProject
import os
import json
from os.path import exists

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


class Nextjs_strapi(RemoteProject):

    upstream_branch = "master"
    remote = 'https://github.com/strapi/foodadvisor.git'

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):
        actions = super(Nextjs_strapi, self).update

        def strapi_fix_demo_schema():
            # Strapi will produce an error when a collection name in the database is too long, which happens to be 
            #   the case in the demo data provided with Foodadvisor. This block updates the collection name in the 
            #   schema file, which will be updated automatically in the database when the change is detected.
            # Issue: https://github.com/strapi/strapi/issues/12101
            # Workaround source: https://github.com/iFixit/react-commerce/commit/a0dc38ddc3c09f7908b7230f66296f006ebf4800
            schema_file = "{0}api/src/components/blocks/related-restaurants.json".format(self.builddir)
            if exists(schema_file):
                updated_collection_name = "components_rest_related_rest"
                with open(schema_file, "r") as file:
                    data = json.load(file)
                    file.close()
                data['collectionName'] = updated_collection_name
                with open(schema_file, "w") as file:
                    json.dump(data, file, indent=4)
                    file.close()

        actions.insert(4, (strapi_fix_demo_schema, []))

        return [
            # Preserve the upstream README.
            'cd {0} && mv README.md README_upstream.md'.format(self.builddir),
            # Add the missing local server directory to .gitignore.
            'cd {0}/api && printf "\nhttp:/*\n" >> .gitignore'.format(self.builddir), 
        ] + actions

    @property
    def platformify(self):
        return super(Nextjs_strapi, self).platformify + [
            # Force add the demo data, since tars are ignored by default. 
            'cd {0} && git add -f api/foodadvisor.tar.gz'.format(self.builddir),
            # For now, remove plugins, since submodules fail.
            'cd {0} && rm -rf api/src/plugins'.format(self.builddir), 
            # Add the mysql package.
            'cd {0}/api && yarn add mysql'.format(self.builddir), 
            # Upgrade dependencies once more. 
            'cd {0}/api && yarn upgrade'.format(self.builddir), 

        ]
