"""Templates Namespace Module.

This module acts as the namespace for various template-specific classes.

Within each submodule, the relevant classes should be exported via the `__all__` constant
declaration. All exported classes should them be imported into the module namespace
using the `from .submodule import *` format and exported via the `__all__` constant
declaration at the end of this file.
"""
from .akeneo import *
from .pimcore import *
from .backdrop import *
from .drupal import *
from .laravel import *
from .magento import *
from .mautic import *
from .pimcore import *
from .rails import *
from .sculpin import *
from .symfony import *
from .typo3 import *
from .wordpress import *

__all__ = (
    "Akeneo",
    "Pimcore",
    "Backdrop",
    "Drupal7_vanilla",
    "Drupal8",
    "Drupal8_multisite",
    "Drupal8_opigno",
    "Drupal8_govcms8",
    "Laravel",
    "Magento2ce",
    "Mautic",
    "Rails",
    "Sculpin",
    "Symfony3",
    "Symfony4",
    "Symfony5",
    "Typo3",
    "Wordpress",
)
