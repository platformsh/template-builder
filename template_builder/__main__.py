import sys
import os

from template_builder.project import BaseProject, TEMPLATEDIR
from template_builder.project.akeneo import Akeneo
from template_builder.project.backdrop import Backdrop
from template_builder.project.drupal import Drupal7_vanilla, Drupal8, Drupal8_multisite, Drupal8_opigno, Drupal8_govcms8, Drupal9
from template_builder.project.gatsby import Gatsby
from template_builder.project.laravel import Laravel
from template_builder.project.magento import Magento2ce
from template_builder.project.pimcore import Pimcore
from template_builder.project.laravel import Laravel
from template_builder.project.magento import Magento2ce
from template_builder.project.mautic import Mautic
from template_builder.project.nextjs import Nextjs
from template_builder.project.nuxtjs import Nuxtjs
from template_builder.project.rails import Rails
from template_builder.project.sculpin import Sculpin
from template_builder.project.strapi import Strapi
from template_builder.project.symfony import Symfony3, Symfony4, Symfony5
from template_builder.project.typo3 import Typo3
from template_builder.project.wordpress import Wordpress_composer, Wordpress_bedrock, Wordpress_woocommerce, Wordpress_vanilla

def project_factory(name):
    '''Instantiate a project object.  Class selection is based on the following naming convention:
    Project class matches template directory name with the first letter capitalized.
      laravel -> Laravel,
      drupal7_vanilla -> Drupal7_vanilla.

    The BaseProject class is used by default (class with the matching name is not imported)
    '''

    targetclass = name.capitalize().replace('-', '_')
    try:
        return globals()[targetclass](name)
    except KeyError:
        return BaseProject(name)

def run():
	project = project_factory(sys.argv[1])
	# print(project.init())
	print(project.update())
	# print(project.platformify())
	# print(project.branch())
	# print(project.push())
	# print(project.pull_request())
	# print(project.test())
