<?php

use \Drupal\node\Entity\Node;
use \Drupal\file\Entity\File;

// Use NASA Astronomy Picture of the Day data (https://apod.nasa.gov/apod/astropix.html),
//      generated via api.nasa.gov, to create dummy nodes.
$file = $extra[0];
$data = file_get_contents($file, FILE_USE_INCLUDE_PATH); 
$obj = json_decode($data); 
$start = 0;
$count = $extra[1];
for ($i = $start; $i < $count; $i++) {
    $title = $obj[$i]->title;
    print "        * node $i: $title\n";
    $image_url = $obj[$i]->hdurl;
    $arrayString= explode("/", $obj[$i]->hdurl );

    $image_filename = "$arrayString[6]";
    
    $image_alt = $obj[$i]->title;
    $image_title = $obj[$i]->title;
    
    $copyright = $obj[$i]->copyright ?? "Public";
    
    $date = $obj[$i]->date;
    $explanation = $obj[$i]->explanation;
    $summary = "Suspendisse eu augue in diam eleifend porta eu eget mauris.";
    $body = <<<EOD
    $explanation

    $copyright ($date)
    EOD;

    // Create file object from remote URL.
    $data = file_get_contents($image_url);
    $filename = "public://$image_filename";
    $file = file_save_data($data, $filename, 1);
    
    // Create node object with attached file.
    $node = Node::create([
        'type'        => 'article',
        'title'       => $title,
        'body'        => $body,
        'summary'     => $summary,
        'field_image' => [
            'target_id' => $file->id(),
            'alt' => $image_alt,
            'title' => $image_title
        ],
    ]);
    $node->save();
}
