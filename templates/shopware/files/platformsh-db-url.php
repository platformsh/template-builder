<?php
declare(strict_types=1);

namespace Platformsh\ShopwareBridge;

use Platformsh\ConfigReader\Config;

/**
 * @var Composer\Autoload\ClassLoader
 */
$loader = require_once(__DIR__.'/app/autoload.php');

$config = new Config();

// This will throw an exception if the relationship is not defined, which is good.
$config->registerFormatter('doctrine', __NAMESPACE__ . '\doctrineFormatter');
return $config->formattedCredentials('database', 'doctrine');
