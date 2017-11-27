<?php
/**
* MediaWiki Sample Platform.sh configuration
* with Memcache support
*/

if (!empty($_ENV['PLATFORM_RELATIONSHIPS'])) {
  $relationships = json_decode(base64_decode($_ENV['PLATFORM_RELATIONSHIPS']), TRUE);
  if (!empty($relationships['cache'])) {
    $wgMemCachedServers = [ $relationships['cache'][0]['host'].':' . $relationships['cache'][0]['port']];
  }
  if (!empty($relationships['database'])) {
    $wgDBserver = $relationships['database'][0]['host'];
    $wgDBport = $relationships['database'][0]['port'];
    $wgDBname = $relationships['database'][0]['path'];
    $wgDBuser = $relationships['database'][0]['username'];
    $wgDBpassword = $relationships['database'][0]['password'];
  }
  $wgSMTP = ['host'=>$_ENV['PLATFORM_SMTP_HOST'], 'IDHost'   => '', 'port' => '25', 'username' => '', 'password' => ''];
}

$wgCacheDirectory = "/app/cache";

$wgScriptPath ="/wiki";
$wgScript = "{$wgScriptPath}/";
$wgArticlePath = "/wiki/$1";
$wgUsePathInfo = true;

$wgMainCacheType = CACHE_MEMCACHED;

wfLoadSkin( 'Vector' );
$wgShowExceptionDetails = true;
$wgShowDBErrorBacktrace = true;