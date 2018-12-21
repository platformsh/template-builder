from .remote import RemoteProject


class Magento2ce(RemoteProject):
    update_branch = '2.2'
    remote = 'https://github.com/magento/magento2.git'
