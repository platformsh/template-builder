from .remote import RemoteProject


class Magento2ce(RemoteProject):
    major_version = '2.2'
    remote = 'https://github.com/magento/magento2.git'
