from . import BaseProject


class Rails(BaseProject):

    @property
    def update(self):
        return super(Rails, self).update + [
            # Force a new install of Rails, over the old copy, to get any updated files.
            'cd {0} && bundle update'.format(self.builddir),
            'cd {0}/.. && BUNDLE_GEMFILE={0}/Gemfile bundle exec rails new {0} --force'.format(self.builddir),
            # Don't update the readme
            'cd {0} git checkout README.md'.format(self.builddir),
        ]

    @property
    def platformify(self):
        return super(Rails, self).platformify + [
            'cd {0} && if ! grep -q platform_sh_rails Gemfile; then bundle add unicorn pg platform_sh_rails --group "production"; fi;'.format(self.builddir),
            # Remove the Rails Ruby version lock file, as it's not needed.
            'cd {0} && rm -f .ruby-version'.format(self.builddir),
            # Remove the Ruby version from the Gemfile, as it pins to a .z release which is too strict.
            "cd {0} && sed '/^ruby /d' Gemfile > temp && mv temp Gemfile".format(self.builddir),
            # Make bootsnap use the /tmp folder
            'cd {0} && if ! grep -q platform_sh config/boot.rb; then cat ../files/_boot.rb >> config/boot.rb; fi; rm _boot.rb'.format(self.builddir),
        ]
