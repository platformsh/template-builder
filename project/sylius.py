from .remote import RemoteProject

class Sylius(RemoteProject):
    major_version = '1.11'
    remote = 'https://github.com/Sylius/Sylius-Standard.git'

    # @property
    # def platformify(self):
    #     return super(Sylius, self).platformify + [
    #         # 'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults()
    #         'cd {0} && composer require platformsh/config-reader drush/drush drupal/console drupal/redis'.format(self.builddir)  + self.composer_defaults(),
    #         # 'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults()
    #     ]