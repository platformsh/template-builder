<?php

declare(strict_types=1);

/**
 * @file
 * Set parameters from Platform.sh environment variables.
 */

$config = new Platformsh\ConfigReader\Config();

if (!$config->inRuntime()) {
    return;
}

if ($config->hasRelationship('database')) {
    $credentials = $config->credentials('database');

    $parameters = [
        "api_enabled"           => true,
        "db_driver"             => "pdo_mysql",
        "db_host"               => $credentials['host'],
        "db_port"               => $credentials['port'],
        "db_name"               => $credentials['path'],
        "db_user"               => $credentials['username'],
        "db_password"           => $credentials['password'],
        "db_table_prefix"       => "",
        "secret"                => $config->projectEntropy,
    ];
}
