<?php
declare(strict_types=1);

function set_psh_file_paths() {
  $appDir = getenv('PLATFORM_APP_DIR');
  if (!$appDir) {
    return;
  }

  $config = config('system.core');
  $config->set('file_public_path', $appDir . '/web/files');
  $config->set('file_temporary_path', $appDir . '/tmp');
  $config->set('file_private_path', $appDir . '/private');
  $config->save();
}

set_psh_file_paths();
