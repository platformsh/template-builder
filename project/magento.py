from .remote import RemoteProject


class Magento2ce(RemoteProject):
    major_version = '2.4'
    remote = 'https://github.com/magento/magento2.git'

    @property
    def platformify(self):
        return super(Magento2ce, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drush/drush:^9.1 drupal/console drupal/redis psr/cache:^1.0'.format(self.builddir)  + self.composer_defaults(),
            'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
            'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
            'cd {0} && composer config allow-plugins.drupal/magento/magento-composer-installer true --no-plugins'.format(self.builddir),
            'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults(),
        ]