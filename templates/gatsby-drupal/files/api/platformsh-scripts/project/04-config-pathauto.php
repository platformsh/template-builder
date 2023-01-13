<?php

use Drupal\pathauto\Entity\PathautoPattern;
// Reference: https://git.drupalcode.org/project/pathauto/-/blob/8.x-1.x/pathauto.install

$entity_type = $extra[0];
$bundle = $extra[1];
$entity_label = $extra[2];
$entity_pattern = $extra[3];

$pattern = PathautoPattern::create([
    'id' => $entity_type,
    'label' => $entity_label,
    'type' => 'canonical_entities:' . $entity_type,
    'pattern' => $entity_pattern,
    'weight' => -5,
]);

$pattern->addSelectionCondition([
    'id' => 'entity_bundle:' . $entity_type,
    'bundles' => [$bundle => $bundle],
    'negate' => FALSE,
    'context_mapping' => [$entity_type => $entity_type],
]);

$pattern->save();
