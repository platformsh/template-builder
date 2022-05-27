<?php
/**
 * Use NASA Astronomy Picture of the Day data (https://apod.nasa.gov/apod/astropix.html), generated via api.nasa.gov,
 * to create dummy posts.
 */

// @todo do we need to verify the values were passed in and what was passed is of the correct type?
list(,$dataSrc,$numPosts) = $argv;
//command for creating posts
$pttrnPostCreate='wp post create --post_title="%s" --post_content="%s" --post_status=publish --porcelain';
//command for creating media
$pttrnImgCreate='wp media import "%s" --title="%s" --alt="%s" --caption="%s" --post_id=%d --featured_image';

$objDummyData = json_decode(file_get_contents($dataSrc, FILE_USE_INCLUDE_PATH), false);

for ($i=0; $i<$numPosts; ++$i) {
	$copyright = $objDummyData[$i]->copyright ?? "Public";
	$postBody=<<<ENDPOST
	{$objDummyData[$i]->explanation}

	$copyright ({$objDummyData[$i]->date})
ENDPOST;

	//first create the post

	$command = sprintf($pttrnPostCreate, $objDummyData[$i]->title, $postBody);
	exec($command,$aryOutput, $result);

	if(0 !== $result || 0 === count($aryOutput)) {
		// @todo besides skipping should we do anything else?
		continue;
	}

	$postID = reset($aryOutput);
	//print "        * Created PostID $postID. Result from wp post create command is: $result\n";
	unset($aryOutput, $result);

	//now create the image media and attach it to the post as a featured image
	$aryImage=[
		$objDummyData[$i]->url,
		$objDummyData[$i]->title,
		$objDummyData[$i]->title,
		$objDummyData[$i]->title,
		$postID
	];

	$command = vsprintf($pttrnImgCreate, $aryImage);
	exec($command, $aryOutput, $result);
	print "        * Post $postID: {$objDummyData[$i]->title}\n";
	unset($aryOutput, $result);
}
