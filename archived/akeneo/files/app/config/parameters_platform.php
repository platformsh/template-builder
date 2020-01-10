<?php

/**
 * @file
 * Set parameters from Platform.sh environment variables.
 */
$platformsh = new \Platformsh\ConfigReader\Config();

// Configure the database.
if ($platformsh->hasRelationship('database')) {
    $database_credentials = $platformsh->credentials('database');
    $container->setParameter('database_driver', 'pdo_'.$database_credentials['scheme']);
    $container->setParameter('database_host', $database_credentials['host']);
    $container->setParameter('database_port', $database_credentials['port']);
    $container->setParameter('database_name', $database_credentials['path']);
    $container->setParameter('database_user', $database_credentials['username']);
    $container->setParameter('database_password', $database_credentials['password']);
    $container->setParameter('database_path', '');
}

// Configure elasticsearch.
if ($platformsh->hasRelationship('elasticsearch')) {
    $elasticsearch_credentials = $platformsh->credentials('elasticsearch');
    $container->setParameter('index_hosts', $elasticsearch_credentials['host'].': '.$elasticsearch_credentials['port']);
}

// Set a default unique secret, based on a project-specific entropy value.
if (getenv('PLATFORM_PROJECT_ENTROPY')) {
    $container->setParameter('kernel.secret', getenv('PLATFORM_PROJECT_ENTROPY'));
}
