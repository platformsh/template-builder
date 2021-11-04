from .remote import RemoteProject


class Pimcore(RemoteProject):
    major_version = 'v2.7'
    remote = 'https://github.com/pimcore/skeleton.git'

    @property
    def platformify(self):
        parent_actions = super(Pimcore, self).platformify
        return parent_actions.extend([
            'cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm  --no-scripts'.format(self.builddir) + ' '.join(self.composer_defaults()),
        ])
