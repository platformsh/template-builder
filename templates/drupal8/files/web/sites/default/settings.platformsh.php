<?php
/**
 * @file
 * Platform.sh settings.
 */

$platformsh = new \Platformsh\ConfigReader\Config();

if (!$platformsh->inRuntime()) {
  return;
}

// Configure the database.
$creds = $platformsh->credentials('database');
$databases['default']['default'] = [
  'driver' => $creds['scheme'],
  'database' => $creds['path'],
  'username' => $creds['username'],
  'password' => $creds['password'],
  'host' => $creds['host'],
  'port' => $creds['port'],
  'pdo' => [PDO::MYSQL_ATTR_COMPRESS => !empty($creds['query']['compression'])]
];


// Configure private and temporary file paths.
if (!isset($settings['file_private_path'])) {
  $settings['file_private_path'] = $platformsh->appDir . '/private';
}
if (!isset($config['system.file']['path']['temporary'])) {
  $config['system.file']['path']['temporary'] = $platformsh->appDir . '/tmp';
}

// Configure the default PhpStorage and Twig template cache directories.
if (!isset($settings['php_storage']['default'])) {
  $settings['php_storage']['default']['directory'] = $settings['file_private_path'];
}
if (!isset($settings['php_storage']['twig'])) {
  $settings['php_storage']['twig']['directory'] = $settings['file_private_path'];
}

// Set trusted hosts based on Platform.sh routes.
if (!isset($settings['trusted_host_patterns'])) {
  $routes = $platformsh->routes();
  $patterns = [];
  foreach ($routes as $url => $route) {
    $host = parse_url($url, PHP_URL_HOST);
    if ($host !== FALSE && $route['type'] == 'upstream' && $route['upstream'] == $platformsh->applicationName) {
      // Replace asterisk wildcards with a regular expression.
      $host_pattern = str_replace('\*', '[^\.]+', preg_quote($host));
      $patterns[] = '^' . $host_pattern . '$';
    }
  }
  $settings['trusted_host_patterns'] = array_unique($patterns);
}

// Import variables prefixed with 'd8settings:' into $settings
// and 'd8config:' into $config.
foreach ($platformsh->variables() as $name => $value) {
  $parts = explode(':', $name);
  list($prefix, $key) = array_pad($parts, 3, null);
  switch ($prefix) {
    // Variables that begin with `d8settings` or `drupal` get mapped
    // to the $settings array verbatim, even if the value is an array.
    // For example, a variable named d8settings:example-setting' with
    // value 'foo' becomes $settings['example-setting'] = 'foo';
    case 'd8settings':
    case 'drupal':
      $settings[$key] = $value;
      break;
    // Variables that begin with `d8config` get mapped to the $config
    // array.  Deeply nested variable names, with colon delimiters,
    // get mapped to deeply nested array elements. Array values
    // get added to the end just like a scalar. Variables without
    // both a config object name and property are skipped.
    // Example: Variable `d8config:conf_file:prop` with value `foo` becomes
    // $config['conf_file']['prop'] = 'foo';
    // Example: Variable `d8config:conf_file:prop:subprop` with value `foo` becomes
    // $config['conf_file']['prop']['subprop'] = 'foo';
    // Example: Variable `d8config:conf_file:prop:subprop` with value ['foo' => 'bar'] becomes
    // $config['conf_file']['prop']['subprop']['foo'] = 'bar';
    // Example: Variable `d8config:prop` is ignored.
    case 'd8config':
      if (count($parts) > 2) {
        $temp = &$config[$key];
        foreach (array_slice($parts, 2) as $n) {
          $prev = &$temp;
          $temp = &$temp[$n];
        }
        $prev[$n] = $value;
      }
      break;
  }
}


// Set the project-specific entropy value, used for generating one-time
// keys and such.
$settings['hash_salt'] = $settings['hash_salt'] ?? $platformsh->projectEntropy;

// Set the deployment identifier, which is used by some Drupal cache systems.
$settings['deployment_identifier'] = $settings['deployment_identifier'] ?? $platformsh->treeId;
