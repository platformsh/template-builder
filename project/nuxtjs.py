from . import BaseProject
import json, os

class Nuxtjs(BaseProject):

    # Keeps package-lock.json out of repo. See notes.md (Yarn - Overwriting updateCommands) for more details.
    updateCommands = {
        'package.json': 'yarn upgrade'
    }

    @property
    def update(self):

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
            "features": [],
            "linter": [],
            "test": "none",
            "mode": "universal",
            "target": "server",
            "devTools": [],
            "vcs": "git"
        }

        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tmpdir = os.path.join(ROOTDIR, 'templates/nuxtjs')

        def set_default(obj):
            if isinstance(obj, set):
                return list(obj)
            raise TypeError

        return [
            # Create a NuxtJS app using Yarn, since there's no dedicated upstream repo for it. Yarn prevents you
            # from creating a new project in a nonempty dir, so the project is made in projectName before its
            # contents are copied into builddir.
            'cd {0} && npx create-nuxt-app --answers \"{1}\" {2}'.format(tmpdir, json.dumps(createNuxtAppAnswers, default=set_default).replace('"', '\\"'), projectName),
            # Disable telemtery so we are not asked for it when running the application the first time
            'cd {0}/{1} && npx nuxt telemetry disable'.format(tmpdir, projectName),
            'cd {0} && rm -rf {1}/.git'.format(tmpdir, projectName),
            'cd {0} && cp -r {1}/{2}/ {2}'.format(self.builddir, tmpdir, projectName),
            'rm -rf {0}'.format(tmpdir),
        ] + super(Nuxtjs, self).update

    @property
    def platformify(self):

        return super(Nuxtjs, self).platformify + [
            # Add dependencies.
            'cd {0} && yarn add platformsh-config'.format(self.builddir),
        ]