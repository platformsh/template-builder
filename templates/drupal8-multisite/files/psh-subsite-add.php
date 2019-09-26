<?php
declare(strict_types=1);

use Symfony\Component\Yaml\Yaml;

/**
 * Simple automation script to make adding new subsites easier.
 *
 * This script is a simple utility to automate the process of adding a new subsite
 * to a Drupal multi-site instance on Platform.sh.  It requires that the site be
 * using subdomains, and that it follows the naming conventions specified in
 * the README.md file.  Please be aware of the following additional caveats:
 *
 * - The .platform.app.yaml and services.yaml files will be YAML-parsed and
 *   rewritten by this script.  That means they will lose all comments and
 *   non-significant line breaks.  Order should be retained.
 * - It assumes the service names and file structure of the original template.
 *   If you have customized those (renamed a service, for instance) then this
 *   script will need to be updated.
 *
 * Usage: Run:
 *
 *   php psh-subsite-add.php SUBSITE_ID
 *
 * Where SUBSITE_ID is the name of the subdomain you wish to add.
 */


// Load up Drupal's autoloader so we have access to free-standing classes,
// like the YAML parser.
require 'vendor/autoload.php';

const SERVICES_FILE = '.platform/services.yaml';
const APP_FILE = '.platform.app.yaml';


function main(array $argv) {

  if (empty($argv[1])) {
    die("You must provide a valid name for the new subsite.\n\nExample: php psh-subsite-add.php stuff\n\n");
  }

  $subsiteName = $argv[1];

  if (file_exists("web/sites/{$subsiteName}")) {
    die (sprintf("A subsite by that name already exists: %s\n\n", $subsiteName));
  }

  addSiteDirectory($subsiteName);
  addRoute($subsiteName);
  addDatabase($subsiteName);
  addRelationship($subsiteName);
}

function addSiteDirectory(string $subsiteName) {
  recurse_copy('web/sites/default', "web/sites/{$subsiteName}");
}

function recurse_copy(string $src, string $dst) {
  $dir = opendir($src);
  @mkdir($dst);
  while(false !== ( $file = readdir($dir)) ) {
    if (( $file != '.' ) && ( $file != '..' )) {
      if ( is_dir($src . '/' . $file) ) {
        recurse_copy($src . '/' . $file,$dst . '/' . $file);
      }
      else {
        copy($src . '/' . $file,$dst . '/' . $file);
      }
    }
  }
  closedir($dir);
}

function addRoute(string $subsiteName) {

  $route = <<<END
"https://{$subsiteName}.{default}/":
    type: upstream
    upstream: "app:http"
    cache:
        enabled: true
        # Base the cache on the session cookie and custom Drupal cookies. Ignore all other cookies.
        cookies: ['/^SS?ESS/', '/^Drupal.visitor/']
END;

  $fp = fopen(".platform/routes.yaml", 'a');
  fwrite($fp, PHP_EOL . PHP_EOL . $route);
  fclose($fp);
}

function addDatabase(string $subsiteName) {

  $yaml = Yaml::parseFile(SERVICES_FILE);

  $yaml['db']['configuration']['schemas'][] = $subsiteName;
  $yaml['db']['configuration']['endpoints'][$subsiteName] = [
    'default_schema' => $subsiteName,
    'privileges' => [$subsiteName => 'admin']
  ];

  file_put_contents(SERVICES_FILE, Yaml::dump($yaml, 10, 4, Yaml::DUMP_MULTI_LINE_LITERAL_BLOCK));
}

function addRelationship(string $subsiteName) {

  $yaml = Yaml::parseFile(APP_FILE);

  $yaml['relationships'][$subsiteName] = "db:{$subsiteName}";

  file_put_contents(APP_FILE, Yaml::dump($yaml, 10, 4, Yaml::DUMP_MULTI_LINE_LITERAL_BLOCK));
}


main($argv);
