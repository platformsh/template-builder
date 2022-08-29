from . import BaseProject
from .remote import RemoteProject
import json
import os
from collections import OrderedDict

ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATEDIR = os.path.join(ROOTDIR, 'templates')


class Drupal7_vanilla(BaseProject):
    version = '7.67'

    @property
    def update(self):
        return super(Drupal7_vanilla, self).update + [
            "wget https://ftp.drupal.org/files/projects/drupal-{0}.tar.gz && tar xzvf drupal-{0}.tar.gz -C {1}".format(
                self.version, self.builddir),
            "rm drupal-{0}.tar.gz".format(self.version),
            "rm -rf {0}public || true".format(self.builddir),
            "mv {0}drupal-{1} {0}public".format(self.builddir, self.version),
        ]


class Drupal8(RemoteProject):
    major_version = '8.9'
    remote = 'https://github.com/drupal/recommended-project.git'


    def package_update_actions(self):
        actions = super(Drupal8, self).package_update_actions()
        return [
                   'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/console-extend-plugin true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.cweagans/composer-patches true --no-plugins '.format(
                       self.builddir),
               ] + actions

    @property
    def update(self):
        projectName = "drupal8"

        def drupal8_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds Drupal 8 for Platform.sh based the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal8, self).update + [
            (self.modify_composer, [drupal8_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Drupal8, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drush/drush:^10.6 drupal/console drupal/redis'.format(
                self.builddir) + self.composer_defaults(),
            'rsync -aP {0} {1}'.format(os.path.join(ROOTDIR, 'common/drupal8/'), self.builddir),
        ]


class Drupal9(RemoteProject):
    # This can have a common base with Drupal 8 eventually, once modules are updated.
    major_version = "9.3"
    remote = 'https://github.com/drupal/recommended-project.git'

    def package_update_actions(self):
        actions = super(Drupal9, self).package_update_actions()
        return [
                   'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.cweagans/composer-patches true --no-plugins '.format(
                       self.builddir),
               ] + actions

    @property
    def update(self):
        projectName = "drupal9"

        def drupal9_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds Drupal 9 for Platform.sh based the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal9, self).update + [
            (self.modify_composer, [drupal9_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Drupal9, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drush/drush drupal/redis'.format(
                self.builddir) + self.composer_defaults(),
            'rsync -aP {0} {1}'.format(os.path.join(ROOTDIR, 'common/drupal9/'), self.builddir),
        ]


class Drupal9_multisite(Drupal9):
    @property
    def update(self):
        projectName = "drupal9-multisite"

        def drupal9_multisite_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds Drupal 9 in the multi-site configuration for Platform.sh based the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal9_multisite, self).update + [
            (self.modify_composer, [drupal9_multisite_modify_composer])
        ]


class Drupal8_multisite(Drupal8):
    @property
    def update(self):
        projectName = "drupal8-multisite"

        def drupal8_multisite_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds Drupal 8 in the multi-site configuration for Platform.sh based the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal8_multisite, self).update + [
            (self.modify_composer, [drupal8_multisite_modify_composer])
        ]


class Drupal8_opigno(RemoteProject):
    # major_version = '2'
    major_version = '3'
    # todo: update all of the bottom to d9
    remote = 'https://bitbucket.org/opigno/opigno-composer.git'

    def package_update_actions(self):
        actions = super(Drupal8_opigno, self).package_update_actions()
        return [
                   'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/console-extend-plugin true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.wikimedia/composer-merge-plugin true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(self.builddir),
                   'cd {0} && composer config allow-plugins.cweagans/composer-patches true --no-plugins '.format(self.builddir),
               ] + actions

    @property
    def update(self):
        projectName = "opigno-composer"

        def drupal8_opigno_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds the Opigno Drupal 9 distribution using the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal8_opigno, self).update + [
            (self.modify_composer, [drupal8_opigno_modify_composer])
        ]

    @property
    def platformify(self):
        return super(Drupal8_opigno, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drupal/redis'.format(
                self.builddir) + self.composer_defaults(),
            # 'cd {0} && composer require platformsh/config-reader drush/drush:^9.1 drupal/console drupal/redis psr/cache:^1.0'.format(self.builddir)  + self.composer_defaults(),
            # 'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.drupal/console-extend-plugin true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.wikimedia/composer-merge-plugin true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(self.builddir),
            # 'cd {0} && composer config allow-plugins.cweagans/composer-patches true --no-plugins '.format(self.builddir),
            'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults(),
            'rsync -aP {0} {1}'.format(os.path.join(ROOTDIR, 'common/drupal9/'), self.builddir),
        ]


class Drupal8_govcms8(RemoteProject):
    major_version = '2.12'
    remote = 'https://github.com/govCMS/GovCMS.git'

    def package_update_actions(self):
        actions = super(Drupal8_govcms8, self).package_update_actions()
        return [
                   'cd {0} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.composer/installers true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(
                       self.builddir),
                   'cd {0} && composer config allow-plugins.cweagans/composer-patches true --no-plugins '.format(
                       self.builddir),
               ] + actions

    @property
    def update(self):
        projectName = "govcms9"

        def drupal8_govcms8_modify_composer(composer):
            """
            This change makes the template loadable via Composer (see https://github.com/platformsh-templates/drupal9/pull/33).
            """

            composer['name'] = "platformsh/{0}".format(projectName)
            composer[
                'description'] = "This template builds the Australian government's GovCMS Drupal 9 distribution using the \"Drupal Recommended\" Composer project."

            return composer

        return super(Drupal8_govcms8, self).update + [
            (self.modify_composer, [drupal8_govcms8_modify_composer])
        ]

    @property
    def update(self):
        return super(Drupal8_govcms8, self).update + [
            'cd {0} && rm -rf .circleci'.format(self.builddir),
            'cd {0} && rm -rf .github'.format(self.builddir),
            'cd {0} && rm -rf .tugboat'.format(self.builddir),
            'cd {0} && composer remove php {1}'.format(self.builddir, self.composer_defaults().replace('--prefer-dist', '')),
            # 'cd {0} && rm -rf web/profiles/govcms'.format(self.builddir),
        ]

    @property
    def platformify(self):
        return super(Drupal8_govcms8, self).platformify + [
            # GovCMS comes with a pre-made lock file that pins symfony/filesystem at v4, but
            # drupal/console only works with the 3.x version, and therefore will fail.
            # It should work to remove the lock file first, but for some reason that is still failing.
            # For now, just skip installing console on GovCMS. I don't know if anyone uses it anyway.
            #    'cd {0} && composer require platformsh/config-reader drush/drush drupal/redis'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && composer require platformsh/config-reader drush/drush:^10 drupal/redis'.format(
                self.builddir) + self.composer_defaults(),
            'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults(),
            'cd {0} && rm -rf web/profiles/govcms'.format(self.builddir),
            'rsync -aP {0} {1}'.format(os.path.join(ROOTDIR, 'common/drupal9/'), self.builddir),
        ]


class Contentacms(BaseProject):

    @property
    def update(self):
        ROOTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        TEMPLATEDIR = os.path.join(ROOTDIR, 'templates/contentacms')

        # Quickstart project package name, used in the block below.
        projectName = "contentacms-platformsh"

        return [
                   # Create a quickstart ContentaCMS app using Composer.
                   'cd {0} && composer create-project contentacms/contenta-jsonapi-project {1} --stability dev --no-interaction --remove-vcs --no-progress --prefer-dist --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config -g allow-plugins.composer/installers true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.dealerdirect/phpcodesniffer-composer-installer true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.cweagans/composer-patches true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.drupal/core-project-message true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.cweagans/composer-patches true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.drupal/core-vendor-hardening true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.drupal/core-composer-scaffold true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0}/{1} && composer config allow-plugins.oomphinc/composer-installers-extender true --no-plugins'.format(
                       TEMPLATEDIR, projectName),
                   'cd {0} && cp -r {1}/{2}/* .'.format(self.builddir, TEMPLATEDIR, projectName),
                   'rm -rf {0}/{1}'.format(TEMPLATEDIR, projectName),
               ] + super(Contentacms, self).update

    @property
    def platformify(self):
        return super(Contentacms, self).platformify + [
            'cd {0} && composer require platformsh/config-reader drush/drush drupal/redis drush/drush:^10'.format(
                self.builddir) + self.composer_defaults(),
            'cd {0} && composer update -W'.format(self.builddir) + self.composer_defaults(),
        ]
