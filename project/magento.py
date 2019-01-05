from .remote import RemoteProject


class Magento2ce(RemoteProject):
    upstream_branch = '2.2'
    remote = 'https://github.com/magento/magento2.git'
