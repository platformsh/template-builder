<?php

use Drupal\next\Entity\NextEntityTypeConfig;

$id = $extra[0];
$site_resolver = $extra[1];
$site = $extra[2];

$entity_type_config = NextEntityTypeConfig::create([
    'id'                => $id,
    'site_resolver'     => $site_resolver,
    'configuration' => [
        'sites' => [
          $site => $site,
        ],
      ],

]);
$entity_type_config->save();
