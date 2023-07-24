from . import BaseProject
from project.ReadmeMixin import ReadmeMixin
import json
import os


class Nuxtjs(BaseProject, ReadmeMixin):
    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):
        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TEMPLATEDIR = os.path.join(ROOTDIR, 'templates/nuxtjs')

        projectName = "nuxtjs-platformsh"
        # create-nuxt-app uses an interactive prompt to select different project options.
        # To avoid going through this prompt, we use the `--answers` option with a JSON
        # set with the default values for each step.
        # See: https://github.com/nuxt/create-nuxt-app/blob/master/packages/create-nuxt-app/lib/prompts.js
        createNuxtAppAnswers = {
            "name": projectName,
            "language": "js",
            "pm": "yarn",
            "ui": "none",
            "template": "html",
            "features": [],
            "linter": [],
            "test": "none",
            "mode": "universal",
            "target": "server",
            "devTools": [],
            "vcs": "git"
        }

        def set_default(obj):
            if isinstance(obj, set):
                return list(obj)
            raise TypeError

        actions = [
            super(Nuxtjs, self).rename_psh_readme(),
            # Create a NuxtJS app using Yarn, since there's no dedicated upstream repo for it. Yarn prevents you
            # from creating a new project in a nonempty dir, so the project is made in projectName before its
            # contents are copied into builddir.
            'cd {0} && npx create-nuxt-app --answers \"{1}\" {2}'.format(TEMPLATEDIR,
                                                                         json.dumps(createNuxtAppAnswers,
                                                                                    default=set_default).replace(
                                                                             '"', '\\"'), projectName),
            # Disable telemtery so we are not asked for it when running the application the first time
            'cd {0}/{1} && npx nuxt telemetry disable'.format(TEMPLATEDIR, projectName),
            'cd {0} && rm -rf {1}/.git'.format(TEMPLATEDIR, projectName),
            'cd {0} && cp -r {1}/{2}/* .'.format(self.builddir, TEMPLATEDIR, projectName),
            'cd {0} && rm -rf {1}'.format(TEMPLATEDIR, projectName),
            'echo "Going to delete the old readme_upstream..."',
            'cd {0} && if [ -f "README_upstream.md" ]; then echo "deleting previous README_upstream"; rm README_upstream.md;fi;'.format(
                self.builddir),
            'echo "Going to rename the new README to README_UPSTREAM"',
            super(Nuxtjs, self).rename_upstream_readme(),
            super(Nuxtjs, self).rename_psh_readme_back(),
        ]

        actions.extend(self.package_update_actions())

        return actions

    @property
    def platformify(self):
        return super(Nuxtjs, self).platformify + [
            # Add dependencies.
            'cd {0} && yarn add platformsh-config'.format(self.builddir),
        ]
