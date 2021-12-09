from .remote import RemoteProject
from .composer import ComposerProject

class Magento2ce(ComposerProject):
    major_version = '2.3'
    remote = 'https://github.com/magento/magento2.git'
