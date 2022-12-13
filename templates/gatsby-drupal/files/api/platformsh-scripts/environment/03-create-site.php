<?php

use Drupal\next\Entity\NextSite;

$id = $extra[0];
$label = $extra[1];
$base_url = $extra[2];
$preview_url = $extra[3];
$preview_secret = $extra[4];

$site = NextSite::create([
    'id'                => $id,
    'label'             => $label,
    'base_url'          => $base_url,
    'preview_url'       => $preview_url,
    'preview_secret'    => $preview_secret,
]);
$site->save();
