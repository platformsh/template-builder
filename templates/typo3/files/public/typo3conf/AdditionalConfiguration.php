<?php

$platformshFile = __DIR__ . '/PlatformshConfiguration.php';

if (file_exists($platformshFile)) {
    require_once($platformshFile);
} else {
    // For local development.  Modify these values as desired.

    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['driver'] = 'mysqli';
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['host'] = '127.0.0.1';
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['dbname'] = 'platform_dev_box';
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['user'] = 'root';
    $GLOBALS['TYPO3_CONF_VARS']['DB']['Connections']['Default']['password'] = false;
}
