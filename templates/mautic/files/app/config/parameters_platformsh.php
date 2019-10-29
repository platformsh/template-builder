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

    $container->setParameter('mautic.db_driver', 'pdo_'.$credentials['scheme']);
    $container->setParameter('mautic.db_host', $credentials['host']);
    $container->setParameter('mautic.db_port', $credentials['port']);
    $container->setParameter('mautic.db_name', $credentials['path']);
    $container->setParameter('mautic.db_user', $credentials['username']);
    $container->setParameter('mautic.db_password', $credentials['password']);
    $container->setParameter('database_path', '');
}

// Set a default unique secret, based on a project-specific entropy value.
$container->setParameter('kernel.secret', $config->projectEntropy);
