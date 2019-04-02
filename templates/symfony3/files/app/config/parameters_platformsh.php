<?php

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

    $container->setParameter('database_driver', 'pdo_'.$credentials['scheme']);
    $container->setParameter('database_host', $credentials['host']);
    $container->setParameter('database_port', $credentials['port']);
    $container->setParameter('database_name', $credentials['path']);
    $container->setParameter('database_user', $credentials['username']);
    $container->setParameter('database_password', $credentials['password']);
    $container->setParameter('database_path', '');
}

// Set a default unique secret, based on a project-specific entropy value.
$container->setParameter('kernel.secret', $config->projectEntropy);
