import os.path 
import os

builddir = '/Users/chadcarlson/Documents/projects/template-builder/templates/wordpress-composer/build'
root = '/wordpress/wp-content/'
namespace = {
    "themes": "wpackagist-theme",
    "plugins": "wpackagist-plugin"
}

defaultPackages = []

installerPaths = [x for x in os.listdir(builddir + root) if os.path.isdir(builddir + root + x)]
for path in installerPaths:
    installerPath = '{0}{1}{2}/'.format(builddir, root, path)
    [defaultPackages.append('{0}/{1}'.format(namespace[path], x)) for x in os.listdir(installerPath) if os.path.isdir(installerPath + x)]

# print(defaultPackages)

print(' '.join(defaultPackages))