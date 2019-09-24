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
  $platformsh = new \Platformsh\ConfigReader\Config();

  if (!$platformsh->inRuntime()) {
    return;
  }

  $appUrls = array_keys($platformsh->getUpstreamRoutes($appName));

  // Sort the URLs, preferring shorter ones with HTTPS.
  usort($appUrls, function (array $a, array $b) {
    // false sorts before true, normally, so negate the comparison.
    return [strpos($a, 'https://') !== 0, strlen($a)] <=> [strpos($a, 'https://') !== 0, strlen($b)];
  });

  // Return the first one.
  return reset($appUrls) ?: NULL;
}
