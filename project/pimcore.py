from .remote import RemoteProject


class Pimcore5(RemoteProject):
    major_version = 'v5.8.2'
    remote = 'https://github.com/pimcore/pimcore.git'

    @property
    def platformify(self):
        return ['cd {0} && rm -rf .ci .travis .gitlab-ci.yml .travis.yml .github CONTRIBUTING.md'.format(self.builddir),
                'cd {0} && COMPOSER_MEMORY_LIMIT=-1 composer create-project pimcore/skeleton tmp_build'.format(self.builddir),
                'cp -r {0}tmp_build/* {0} && rm -r {0}tmp_build'.format(self.builddir) 
                ] + super(Pimcore5, self).platformify + [
                'cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm --no-scripts'.format(self.builddir),]
