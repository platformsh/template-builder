from .remote import RemoteProject


class Magento2ce(RemoteProject):
    major_version = '2.4'
    remote = 'https://github.com/magento/magento2.git'
