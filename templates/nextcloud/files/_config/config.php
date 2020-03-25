<?php
$platform_sh_routes = json_decode(base64_decode($_ENV['PLATFORM_ROUTES']), true);
foreach ($platform_sh_routes as $url => $route) {
  if ($route['primary']) {
     $platform_sh_url = $url;
     $platform_sh_domain= rtrim(explode("://", $platform_sh_url)[1], '/');
  }
}

$CONFIG = array (
  'config_is_read_only' => true,
  'appstoreenabled' => false,
  'front_controller_active' => true,
  'instanceid' => $_ENV['PLATFORM_PROJECT'],
  'passwordsalt' => $_ENV['PLATFORM_PROJECT_ENTROPY']."_salt",
  'secret' => $_ENV['PLATFORM_PROJECT_ENTROPY'],
  'trusted_domains' =>
      array (
        0 => $platform_sh_domain,
      ),
  "apps_paths" => [
      [
              "path"     => "/app/src/apps",
              "url"      => "/apps",
              "writable" => false,
      ],
      [
              "path"     => "/app/apps",
              "url"      => "/user_apps",
              "writable" => true,
      ],
  ],
  //'theme' => 'platformsh',
  'mail_smtpmode' => 'smtp',
  'mail_smtphost' => $_ENV['PLATFORM_SMTP_HOST'] ?? '',
  'mail_smtpport' => 25,
  'mail_smtpauthtype' => 'PLAIN',
  'mail_sendmailmode' => 'smtp',
  'mail_from_address' => 'do-not-reply',
  'mail_domain' => 'platform.sh',
  'tempdirectory' => '/tmp/nextcloudtemp',
  'debug' => false,
  'cache_path' => '/tmp/cache',
  // FIXME get something more reasonable here
  'logfile' => '/tmp/logs/nextcloud.log',
  'dbtype' => 'mysql',
  'version' => '18.0.1',
  'overwrite.cli.url' =>$platform_sh_url,
  'dbname' => 'main',
  'dbhost' => 'database.internal',
  'dbport' => '',
//  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'user',
  'dbpassword' => '',
  'installed' => false,
  'maintenance' => false,
  'htaccess.RewriteBase' => '/',
//  'overwritewebroot' => '',
  'htaccess.IgnoreFrontController' => false,
  'check_data_directory_permissions' => false,
  'quota_include_external_storage' => true,
//  'loglevel' => 0,
  'memcache.distributed' => '\OC\Memcache\Redis',
  'redis' => [
     'host' => 'cache.internal', // can also be a unix domain socket: '/tmp/redis.sock'
     'port' => 6379,
  ],
  'filelocking.enabled' => true,
  'filelocking.ttl' => 60*60,
  'memcache.locking' => '\\OC\\Memcache\\Redis',
);

// set object-store as primary store if we have an S3 bucket set.
if (getenv('S3_BUCKET')){
  $CONFIG["objectstore"] =array(
    'class' => '\\OC\\Files\\ObjectStore\\S3',
    'arguments' => array(
      'bucket' => $_ENV['S3_BUCKET'],
      'autocreate' => true,
      'key'    => $_ENV['S3_KEY'],
      'secret' => $_ENV['S3_SECRET'],
      'hostname' => $_ENV['S3_HOSTNAME'],
      'region'=>$_ENV['S3_REGION'],
      'port' => 443,
      'use_ssl' => true,
       // required for some non Amazon S3 implementations
      'use_path_style'=>true
    ),
  );
}
