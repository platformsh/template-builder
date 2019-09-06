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
    if ($route['type'] === 'upstream' && $route['upstream'] === $appName) {
      $appUrls[$route['original_url']] = $url;
    }
  }

  // Select the first preferred route, if it exists in the app URLs.
  $preferred_routes = [
    'https://{default}/',
    'https://{default}',
    'https://www.{default}/',
    'https://www.{default}',
    'https://{all}/',
    'https://{all}',
    'https://www.{all}/',
    'https://www.{all}',
  ];
  foreach ($preferred_routes as $preferred_route) {
    if (isset($appUrls[$preferred_route])) {
      return $appUrls[$preferred_route];
    }
  }

  // Otherwise, return the first URL that matched the app.
  return reset($appUrls) ?: NULL;
}
