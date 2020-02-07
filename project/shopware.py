from .remote import RemoteProject


class Shopware(RemoteProject):
    upstream_branch = 'master'
    remote = 'https://github.com/shopware/composer-project.git'

    @property
    def platformify(self):
        def shopware_modify_composer(composer):
            # The default scripts require env files to already be created, which... is silly.
            composer['scripts'] = {}

            # Add the environment variable pre-set code.
            composer['autoload']['files'] = ['platformsh-env.php']

            return composer

        return super(Shopware, self).platformify + [
            (self.modify_composer, [shopware_modify_composer]),
            # 'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader'.format(self.builddir),
        ]

class Shopware6(RemoteProject):
    major_version = 'v6.1'
    remote = 'https://github.com/shopware/production.git'

    @property
    def platformify(self):
        def shopware_modify_composer(composer):
            # The default scripts require env files to already be created, which... is silly.
            #composer['scripts'] = {}

            # Add the environment variable pre-set code.
            composer['autoload']['files'] = ['platformsh-env.php']

            return composer

        return super(Shopware6, self).platformify + [
            (self.modify_composer, [shopware_modify_composer]),
            #'cd {0} && composer require platformsh/symfonyflex-bridge ^2.1 --ignore-platform-reqs'.format(
            # self.builddir),
            # 'cd {0} && composer config platform.php 7.3'.format(self.builddir),
            'cd {0} && composer require platformsh/config-reader'.format(self.builddir),
        ]

