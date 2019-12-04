<?php
declare(strict_types=1);

namespace Platformsh\ShopwareBridge;

use Platformsh\ConfigReader\Config;

mapPlatformShEnvironment();

function mapPlatformShEnvironment() : void
{
    $config = new Config();

    if (!$config->inRuntime()) {
        if ($config->inBuild()) {
            // In the build hook we still need to set a fake Doctrine URL in order to
            // work around bugs in Doctrine.
            setDefaultDoctrineUrl();
        }
        return;
    }

    $config->registerFormatter('doctrine', __NAMESPACE__ . '\doctrineFormatter');

    // Set the application secret if it's not already set.
    // We force re-setting the APP_SECRET to ensure it's set in all of PHP's various
    // environment places.
    if (isset($config->projectEntropy)) {
        $secret = getenv('APP_SECRET') ?: $config->projectEntropy;
        setEnvVar('APP_SECRET', $secret);
    }

    // Default to production. You can override this value by setting
    // `env:SHOPWARE_ENV` as a project variable, or by adding it to the
    // .platform.app.yaml variables block.
    $appEnv = getenv('SHOPWARE_ENV') ?: 'prod';
    setEnvVar('SHOPWARE_ENV', $appEnv);

    // Map services as feasible.
    mapPlatformShDatabase('database', $config);

    // Set the URL based on the route.  This is a required route ID.
    setEnvVar('SHOP_URL', $config->getRoute('shopware')['url']);
}

/**
 * Sets an environment variable in all the myriad places PHP can store it.
 *
 * @param string $name
 *   The name of the variable to set.
 * @param null|string $value
 *   The value to set.  Null to unset it.
 */
function setEnvVar(string $name, ?string $value) : void
{
    if (!putenv("$name=$value")) {
        throw new \RuntimeException('Failed to create environment variable: ' . $name);
    }
    $order = ini_get('variables_order');
    if (stripos($order, 'e') !== false) {
        $_ENV[$name] = $value;
    }
    if (stripos($order, 's') !== false) {
        if (strpos($name, 'HTTP_') !== false) {
            throw new \RuntimeException('Refusing to add ambiguous environment variable ' . $name . ' to $_SERVER');
        }
        $_SERVER[$name] = $value;
    }
}

/**
 * Maps the specified relationship to the DATABASE_URL environment variable, if available.
 *
 * @param string $relationshipName
 *   The database relationship name.
 * @param Config $config
 *   The config object.
 */
function mapPlatformShDatabase(string $relationshipName, Config $config) : void
{
    if (!$config->hasRelationship($relationshipName)) {
        return;
    }
    setEnvVar('DATABASE_URL', $config->formattedCredentials($relationshipName, 'doctrine'));
}

/**
 * Sets a default Doctrine URL.
 *
 * Doctrine needs a well-formed URL string with a database version even in the build hook.
 * It doesn't use it, but it fails if it's not there.  This default meets the minimum
 * requirements of the format without actually allowing a connection.
 */
function setDefaultDoctrineUrl() : void
{
    // Hack the Doctrine URL to be syntactically valid in a build hook, even
    // though it shouldn't be used.
    $dbUrl = sprintf(
        '%s://%s:%s@%s:%s/%s?charset=utf8mb4&serverVersion=%s',
        'mysql',
        '',
        '',
        'localhost',
        3306,
        '',
        'mariadb-10.2.12'
    );
    setEnvVar('DATABASE_URL', $dbUrl);
}

function doctrineFormatter(array $credentials) : string
{
    $dbUrl = sprintf(
        '%s://%s:%s@%s:%d/%s',
        $credentials['scheme'],
        $credentials['username'],
        $credentials['password'],
        $credentials['host'],
        $credentials['port'],
        $credentials['path']
    );
    switch ($credentials['scheme']) {
        case 'mysql':
            $type = $credentials['type'] ?? DEFAULT_MYSQL_ENDPOINT_TYPE;
            $versionPosition = strpos($type, ":");
            // If a version is found, use it, otherwise, default to mariadb 10.2.
            $dbVersion = (false !== $versionPosition) ? substr($type, $versionPosition + 1) : '10.2';
            // Doctrine needs the mariadb-prefix if it's an instance of MariaDB server
            if ($dbVersion !== '5.5') {
                $dbVersion = sprintf('mariadb-%s', $dbVersion);
            }
            // if MariaDB is in version 10.2, doctrine needs to know it's superior to patch version 6 to work properly
            if ($dbVersion === 'mariadb-10.2') {
                $dbVersion .= '.12';
            }
            $dbUrl .= sprintf('?charset=utf8mb4&serverVersion=%s', $dbVersion);
            break;
        case 'pgsql':
            $type = $credentials['type'] ?? DEFAULT_POSTGRESQL_ENDPOINT_TYPE;
            $versionPosition = strpos($type, ":");
            $dbVersion = (false !== $versionPosition) ? substr($type, $versionPosition + 1) : '11';
            $dbUrl .= sprintf('?serverVersion=%s', $dbVersion);
            break;
    }
    return $dbUrl;
}
