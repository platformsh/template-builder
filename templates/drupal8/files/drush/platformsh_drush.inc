<?php
/**
 * @file
 * Platform.sh utilities for integrating with Drush.
 */

/**
 * Returns a site URL to use with Drush, if possible.
 *
 * @return string|NULL
 */
function _platformsh_drush_site_url() {
  if (!getenv('PLATFORM_ROUTES') || !getenv('PLATFORM_APPLICATION_NAME')) {
    return NULL;
  }

  $routes = json_decode(base64_decode(getenv('PLATFORM_ROUTES')), TRUE);
  $appName = getenv('PLATFORM_APPLICATION_NAME');

  // Filter the list of routes to find those matching the current app.
  $appUrls = [];
  foreach ($routes as $url => $route) {
    if ($route['type'] === 'upstream' && strpos($route['upstream'], $appName . ':') === 0) {
      // If this route is the primary one, use its URL directly.
      if (!empty($route['primary'])) {
        return $url;
      }

      // Otherwise, add it to the list.
      $appUrls[] = $url;
    }
  }

  // Sort the URLs, preferring shorter ones with HTTPS.
  usort($appUrls, function ($a, $b) {
    $result = 0;
    foreach ([$a, $b] as $key => $url) {
      if (strpos($url, 'https://') === 0) {
        $result += $key === 0 ? -2 : 2;
      }
    }
    $result += strlen($a) <= strlen($b) ? -1 : 1;

    return $result;
  });
  
  // Return the first one.
  return reset($appUrls) ?: NULL;
}
