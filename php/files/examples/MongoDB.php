<?php

declare(strict_types=1);

use Platformsh\ConfigReader\Config;
use MongoDB\Client;

// Create a new config object to ease reading the Platform.sh environment variables.
// You can alternatively use getenv() yourself.
$config = new Config();

// The 'database' relationship is generally the name of primary database of an application.
// It could be anything, though, as in the case here here where it's called "mongodb".
$credentials = $config->relationships['mongodb'][0];

print "<pre>\n";
print_r($credentials);
print "</pre>\n";

try {

    $server = sprintf('%s://%s:%s@%s:%d/%s',
        $credentials['scheme'],
        $credentials['username'],
        $credentials['password'],
        $credentials['host'],
        $credentials['port'],
        $credentials['path']
    );

    $client = new Client($server);
    $collection = $client->main->starwars;

    $result = $collection->insertOne([
        'name' => 'Rey',
        'occupation' => 'Jedi',
    ]);

    $id = $result->getInsertedId();

    $document = $collection->findOne([
        '_id' => $id,
    ]);


    printf("Found %s (%s)<br />\n", $document->name, $document->occupation);

} catch (\Exception $e) {
    print $e->getMessage();
}
