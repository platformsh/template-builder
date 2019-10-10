<?php

/**
 * Platform.sh-specific configuration for TYPO3.
 *
 * You may edit this file as desired, but connection configuration
 * should be based on Platform.sh environment variables.
 */

declare(strict_types=1);

use Platformsh\ConfigReader\Config;

$platformConfig = new Config();

if (!$platformConfig->isValidPlatform()) {
    return;
}

if ($platformConfig->inBuild()) {
    return;
}

// Workaround to set the proper env variable for the main route (found in config/sites/main/config.yaml)
putenv('PLATFORM_ROUTES_MAIN=' . $platformConfig->getRoute('main')['url']);

// Configure the database based on the Platform.sh relationships.
if ($platformConfig->hasRelationship('database')) {
    $databaseConfig = $platformConfig->credentials('database');
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['driver'] = 'mysqli';
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['host'] = $databaseConfig['host'];
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['port'] = $databaseConfig['port'];
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['dbname'] = $databaseConfig['path'];
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['user'] = $databaseConfig['username'];
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['password'] = $databaseConfig['password'];
}

// Configure Redis as the cache backend if available.
if ($platformConfig->hasRelationship('rediscache')) {
    $redisConfig = $platformConfig->credentials('rediscache');
    $redisHost = $redisConfig['host'];
    $redisPort = $redisConfig['port'];
    $list = [
        'pages' => 3600 * 24 * 7,
        'pagesection' => 3600 * 24 * 7,
        'rootline' => 3600 * 24 * 7,
        'hash' => 3600 * 24 * 7,
        'extbase' => 3600 * 24 * 7,
    ];
    $counter = 1;
    foreach ($list as $key => $lifetime) {
        $GLOBALS['TYPO3_CONF_VARS']['SYS']['caching']['cacheConfigurations'][$key]['backend'] = \TYPO3\CMS\Core\Cache\Backend\RedisBackend::class;
        $GLOBALS['TYPO3_CONF_VARS']['SYS']['caching']['cacheConfigurations'][$key]['options'] = [
            'database' => $counter++,
            'hostname' => $redisHost,
            'port' => $redisPort,
            'defaultLifetime' => $lifetime
        ];
    }
}

// Add additional Platform.sh-specific configuration here, such as a search backend.
