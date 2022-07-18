import os
from . import BaseProject
# from .remote import RemoteProject
import json
from collections import OrderedDict

class Akeneo(BaseProject):
    # major_version = 'v6'
    # remote = 'https://github.com/akeneo/pim-community-standard.git'

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade',
        'composer.json': 'composer update -W --ignore-platform-req=ext-apcu --ignore-platform-req=ext-imagick',
    }

    @property
    def update(self):

        def akeneo_modify_composer(composer):
            """
            This change makes the template loadable via Composer.
            """

            composer['name']= "platformsh/{0}".format(projectName)
            composer['description']= "Akeneo PIM Community Standard Edition for deployment on Platform.sh"

            return composer


        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TEMPLATEDIR = os.path.join(ROOTDIR, 'templates/akeneo')

        # Quickstart project package name, used in the block below.
        projectName = "pim-community-standard"

        return super(Akeneo, self).update + [
            'cd {0} && composer create-project akeneo/pim-community-standard {1} "6.0.*@stable" --ignore-platform-req=ext-apcu --ignore-platform-req=ext-imagick'.format(TEMPLATEDIR, projectName),
            'cd {0} && cp -r {1}/{2}/* .'.format(self.builddir, TEMPLATEDIR, projectName),
            'rm -rf {0}/{1}'.format(TEMPLATEDIR, projectName),
            (self.modify_composer, [akeneo_modify_composer]) 
        ]

    @property
    def platformify(self):
        return super(Akeneo, self).platformify + [
                'cd {0} && composer require platformsh/config-reader'.format(self.builddir) + self.composer_defaults(),
                'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
                'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
                'cd {0} && composer config allow-plugins.symfony/flex true --no-plugins'.format(self.builddir),
                'cd {0} && composer update -W --ignore-platform-req=ext-apcu --ignore-platform-req=ext-imagick'.format(self.builddir),
                ]
