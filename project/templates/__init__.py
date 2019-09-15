
from .akeneo import Akeneo
from .pimcore import Pimcore
from .drupal import Drupal7Vanilla, Drupal8, Drupal8multi, Opigno, Govcms8
from .laravel import Laravel
from .magento import Magento2ce
from .rails import Rails
from .sculpin import Sculpin
from .symfony import Symfony3, Symfony4
from .wordpress import Wordpress

__all__ = {
    Akeneo,
    Pimcore,
    Drupal7Vanilla,
    Drupal8,
    Drupal8multi,
    Opigno,
    Govcms8,
    Laravel,
    Magento2ce,
    Rails,
    Sculpin,
    Symfony3,
    Symfony4,
    Wordpress
}
