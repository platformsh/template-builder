import os
from . import BaseProject


# from .remote import RemoteProject

# "repositories": {
#     "Magento Repo Auth Required": {
#         "type": "composer",
#         "url": "https://repo.magento.com"
#     },
#     "ECE-Tools": {
#         "type": "git",
#         "url": "https://github.com/magento/ece-tools.git"
#     },
#     "Magento Cloud Components": {
#         "type": "git",
#         "url": "https://github.com/magento/magento-cloud-components.git"
#     },
#     "Magento Cloud Patches": {
#         "type": "git",
#         "url": "https://github.com/magento/magento-cloud-patches.git"
#     },
#     "Magento Quality Patches": {
#         "type": "git",
#         "url": "https://github.com/magento/quality-patches.git"
#     }
# },
# "extra": {
#     "magento-force": "override"
# }

#     "config": {
#     "preferred-install": "dist",
#     "sort-packages": true,
#     "allow-plugins": {
#         "composer/installers": true,
#         "laminas/laminas-dependency-plugin": true,
#         "magento/composer-dependency-version-audit-plugin": true,
#         "magento/inventory-composer-installer": true,
#         "magento/magento-composer-installer": true
#     }
# },
# "require": {
#     "magento/ece-tools": "^2002.1.6",
#     "magento/magento-cloud-components": "^1.0.7",
#     "magento/magento-cloud-patches": "^1.0.10",
#     "magento/product-community-edition": "^2.4",
#     "magento/quality-patches": "^1.0.22",
#     "wolfsellers/module-enabledisabletfa": "^1.0"
# },

class Magento2ce(BaseProject):
    # updateCommands = {
    #     'composer.json': 'composer update -W --ignore-platform-req=ext-apcu --ignore-platform-req=ext-imagick',
    # }

    # def package_update_actions(self):
    #     actions = super(Magento2ce, self).package_update_actions()
    #     return [
    #                'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(
    #                    self.builddir),
    #                'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(
    #                    self.builddir),
    #            ] + actions

    @property
    def update(self):
        def magento_modify_composer(composer):
            """
            This change makes the template loadable via Composer.
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer['description'] = "Magento 2 CE(Community Edition) for Platform.sh"

            # composer['repositories'] = {
            #     "Magento Repo Auth Required": {
            #         "type": "composer",
            #         "url": "https://repo.magento.com"
            #     },
            #     "ECE-Tools": {
            #         "type": "git",
            #         "url": "https://github.com/magento/ece-tools.git"
            #     },
            #     "Magento Cloud Components": {
            #         "type": "git",
            #         "url": "https://github.com/magento/magento-cloud-components.git"
            #     },
            #     "Magento Cloud Patches": {
            #         "type": "git",
            #         "url": "https://github.com/magento/magento-cloud-patches.git"
            #     },
            #     "Magento Quality Patches": {
            #         "type": "git",
            #         "url": "https://github.com/magento/quality-patches.git"
            #     }
            # }

            return composer

        # ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # TEMPLATEDIR = os.path.join(ROOTDIR, 'templates/magento2ce')
        #
        # # Quickstart project package name, used in the block below.
        projectName = "magento2ce"

        return super(Magento2ce, self).update + [
            # 'cd {0} && composer create-project --repository-url=https://repo.magento.com/ '
            # 'magento/project-community-edition {1} --ignore-platform-req=ext-iconv --ignore-platform-req=ext-soap '
            # '--ignore-platform-req=ext-pdo_mysql {2}'.format(TEMPLATEDIR, projectName, self.composer_defaults()),
            #
            # 'rm -rf {0}/*'.format(self.builddir),
            # 'cd {0} && git add . && git commit -m "Clear previous template."'.format(self.builddir),
            #
            # 'cd {0} && cp -r {1}/{2}/* .'.format(self.builddir, TEMPLATEDIR, projectName),
            # 'rm -rf {0}/{1}'.format(TEMPLATEDIR, projectName),
            (self.modify_composer, [magento_modify_composer])
        ]

    @property
    def platformify(self):
        extraIgnores = '--ignore-platform-req=ext-iconv --ignore-platform-req=ext-soap ' \
                       '--ignore-platform-req=ext-pdo_mysql '

        return super(Magento2ce, self).platformify + [
            # 'cd {0} && composer require magento/ece-tools magento/magento-cloud-components '
            # 'magento/quality-patches -W '.format(self.builddir)  + self.composer_defaults() + extraIgnores,
            'cd {0} && composer update -W {1}'.format(self.builddir, self.composer_defaults() + extraIgnores),
        ]
