<?php

use Drupal\consumers\Entity\Consumer;

// CONSUMER_UUID=$(drush scr $DRUPAL_SETUP/environment/02-create-consumer.php "$CONSUMER_USER_UID" "$CONSUMER_ID" "$CONSUMER_LABEL" "$CONSUMER_DESC" "$CONSUMER_SITE" "$CONSUMER_SECRET")


$user_id = $extra[0];
$id = $extra[1];
$label = $extra[2];
$description = $extra[3];
$site = $extra[4];
$secret = $extra[5];

$site = Consumer::create([
    'id'                => $id,
    'label'             => $label,
    'description'       => $description,
    'user_id'           => $user_id,
    'roles'             => $site,
    'secret'            => $secret,
]);

$site->save();
echo $site->uuid();
