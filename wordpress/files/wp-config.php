<?php

if (!getenv('PLATFORM_RELATIONSHIPS')) {
  // You can create a wp-config-local.php file with local configuration.
  if ( file_exists( dirname( __FILE__ ) . '/wp-config-local.php' ) ) {
    include( dirname( __FILE__ ) . '/wp-config-local.php' );
  }
} else {
    // This is where we get the relationships of our application dynamically
    //from Platform.sh

    // set session path to /tmp in cas we are using wp-cli to avoid notices
    if (php_sapi_name() === 'cli') {
      session_save_path("/tmp");
    }

    // we might be running wp-cli
    if (isset($_SERVER['HTTP_HOST'])) {
          $site_host = $_SERVER['HTTP_HOST'];
          $site_scheme = !empty($_SERVER['https']) ? 'https' : 'http';
    }

    $relationships = json_decode(base64_decode(getenv('PLATFORM_RELATIONSHIPS')), TRUE);

    // We are using the first relationship called "database" found in your
    // relationships. Note that you can call this relationship as you wish
    // in you .platform.app.yaml file, but 'database' is a good name.
    define('DB_NAME', $relationships['database'][0]['path']);
    define('DB_USER', $relationships['database'][0]['username']);
    define('DB_PASSWORD', $relationships['database'][0]['password']);
    define('DB_HOST', $relationships['database'][0]['host']);
    define('DB_CHARSET', 'utf8');
    define('DB_COLLATE', '');

    // Check whether a route is defined for this application in the Platform.sh routes.
    // Use it as the site hostname if so (it is not ideal to trust HTTP_HOST).
    if (getenv('PLATFORM_ROUTES')) {
      $routes = json_decode(base64_decode(getenv('PLATFORM_ROUTES')), TRUE);
      foreach ($routes as $url => $route) {
        if ($route['type'] === 'upstream' && $route['upstream'] === getenv('PLATFORM_APPLICATION_NAME')) {
          // Pick the first hostname, or the first HTTPS hostname if one exists.
          $host = parse_url($url, PHP_URL_HOST);
          $scheme = parse_url($url, PHP_URL_SCHEME);
          if ($host !== false && (!isset($site_host) || ($site_scheme === 'http' && $scheme === 'https'))) {
            $site_host = $host;
            $site_scheme = $scheme ?: 'http';
          }
        }
      }
    }

    // Change site URL per environment.
    define('WP_HOME', $site_scheme . '://' . $site_host);
    define('WP_SITEURL', WP_HOME);
}

// Since you can have multiple installations in one database, you need a unique
// prefix.
$table_prefix  = 'wp_';

// Default PHP settings.
ini_set('session.gc_probability', 1);
ini_set('session.gc_divisor', 100);
ini_set('session.gc_maxlifetime', 200000);
ini_set('session.cookie_lifetime', 2000000);
ini_set('pcre.backtrack_limit', 200000);
ini_set('pcre.recursion_limit', 200000);

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
  define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
