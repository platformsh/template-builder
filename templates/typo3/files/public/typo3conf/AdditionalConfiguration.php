<?php

/**
 * Additional configuration file.
 *
 * Place configuration here you want to be shared by Platform.sh environments and local development.
 *
 * Platform.sh-specific configuration should be added to PlatformshConfiguration.php.
 * Environment-specific configuration should be added to LocalConfiguration.php as normal.
 */

// Include the Platform.sh-specific configuration.
// This file will no-op on its own if not on Platform.sh.
$platformshFile = __DIR__ . '/PlatformshConfiguration.php';
if (file_exists($platformshFile)) {
    require_once($platformshFile);
}
