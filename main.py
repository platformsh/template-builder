import sys
import os

from project import BaseProject, TEMPLATEDIR
from project.akeneo import Akeneo
from project.backdrop import Backdrop
from project.drupal import Drupal7_vanilla, Drupal8, Drupal8_multisite, Drupal8_opigno, Drupal8_govcms8, Drupal9
from project.gatsby import Gatsby
from project.laravel import Laravel
from project.magento import Magento2ce
from project.pimcore import Pimcore
from project.laravel import Laravel
from project.magento import Magento2ce
from project.mautic import Mautic
from project.nextjs import Nextjs
from project.nuxtjs import Nuxtjs
from project.rails import Rails
from project.sculpin import Sculpin
from project.strapi import Strapi
from project.symfony import Symfony3, Symfony4, Symfony5
from project.typo3 import Typo3
from project.wordpress import Wordpress_composer, Wordpress_bedrock, Wordpress_woocommerce, Wordpress_vanilla

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
	print(project.platformify())
	# print(project.branch())
	# print(project.push())
	# print(project.pull_request())
	# print(project.test())
