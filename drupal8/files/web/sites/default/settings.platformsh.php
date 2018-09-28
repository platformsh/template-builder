<?php
/**
 * @file
 * Platform.sh settings.
 */

// Configure the database.
if (getenv('PLATFORM_RELATIONSHIPS')) {
  $relationships = json_decode(base64_decode(getenv('PLATFORM_RELATIONSHIPS')), TRUE);
  if (empty($databases['default']) && !empty($relationships)) {
    foreach ($relationships as $key => $relationship) {
      $drupal_key = ($key === 'database') ? 'default' : $key;
      foreach ($relationship as $instance) {
        if (empty($instance['scheme']) || ($instance['scheme'] !== 'mysql' && $instance['scheme'] !== 'pgsql')) {
          continue;
        }
        $database = [
          'driver' => $instance['scheme'],
          'database' => $instance['path'],
          'username' => $instance['username'],
          'password' => $instance['password'],
          'host' => $instance['host'],
          'port' => $instance['port'],
        ];

        if (!empty($instance['query']['compression'])) {
          $database['pdo'][PDO::MYSQL_ATTR_COMPRESS] = TRUE;
        }

        if (!empty($instance['query']['is_master'])) {
          $databases[$drupal_key]['default'] = $database;
        }
        else {
          $databases[$drupal_key]['replica'][] = $database;
        }
      }
    }
  }
}

if (getenv('PLATFORM_APP_DIR')) {

  // Configure private and temporary file paths.
  if (!isset($settings['file_private_path'])) {
    $settings['file_private_path'] = getenv('PLATFORM_APP_DIR') . '/private';
  }
  if (!isset($config['system.file']['path']['temporary'])) {
    $config['system.file']['path']['temporary'] = getenv('PLATFORM_APP_DIR') . '/tmp';
  }

  // Configure the default PhpStorage and Twig template cache directories.
  if (!isset($settings['php_storage']['default'])) {
    $settings['php_storage']['default']['directory'] = $settings['file_private_path'];
  }
  if (!isset($settings['php_storage']['twig'])) {
    $settings['php_storage']['twig']['directory'] = $settings['file_private_path'];
  }

}

// Set trusted hosts based on Platform.sh routes.
if (getenv('PLATFORM_ROUTES') && !isset($settings['trusted_host_patterns'])) {
  $routes = json_decode(base64_decode(getenv('PLATFORM_ROUTES')), TRUE);
  $settings['trusted_host_patterns'] = [];
  foreach ($routes as $url => $route) {
    $host = parse_url($url, PHP_URL_HOST);
    if ($host !== FALSE && $route['type'] == 'upstream' && $route['upstream'] == getenv('PLATFORM_APPLICATION_NAME')) {
      // Replace asterisk wildcards with a regular expression.
      $host_pattern = str_replace('\*', '[^\.]+', preg_quote($host));
      $settings['trusted_host_patterns'][] = '^' . $host_pattern . '$';
    }
  }
  $settings['trusted_host_patterns'] = array_unique($settings['trusted_host_patterns']);
}

// Import variables prefixed with 'd8settings:' into $settings and 'd8config:'
// into $config.
if (getenv('PLATFORM_VARIABLES')) {
  $variables = json_decode(base64_decode(getenv('PLATFORM_VARIABLES')), TRUE);
  foreach ($variables as $name => $value) {
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
}

// Set the project-specific entropy value, used for generating one-time
// keys and such.
if (getenv('PLATFORM_PROJECT_ENTROPY') && empty($settings['hash_salt'])) {
  $settings['hash_salt'] = getenv('PLATFORM_PROJECT_ENTROPY');
}

// Set the deployment identifier, which is used by some Drupal cache systems.
if (getenv('PLATFORM_TREE_ID') && empty($settings['deployment_identifier'])) {
  $settings['deployment_identifier'] = getenv('PLATFORM_TREE_ID');
}
