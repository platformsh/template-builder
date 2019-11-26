
/**
 * Kibana entry file
 *
 * This is programmatically created and updated, do not modify
 *
 * context: {
  "env": "production",
  "kbnVersion": "7.2.1",
  "buildNum": 24452,
  "plugins": [
    "apm",
    "apm_oss",
    "beats_management",
    "canvas",
    "cloud",
    "code",
    "console",
    "console_extensions",
    "cross_cluster_replication",
    "dashboard_mode",
    "data",
    "elasticsearch",
    "encrypted_saved_objects",
    "graph",
    "grokdebugger",
    "index_lifecycle_management",
    "index_management",
    "infra",
    "input_control_vis",
    "inspector_views",
    "interpreter",
    "kbn_doc_views",
    "kbn_vislib_vis_types",
    "kibana",
    "kuery_autocomplete",
    "license_management",
    "logstash",
    "maps",
    "markdown_vis",
    "metric_vis",
    "metrics",
    "ml",
    "monitoring",
    "notifications",
    "oss_telemetry",
    "region_map",
    "remote_clusters",
    "reporting",
    "rollup",
    "searchprofiler",
    "security",
    "siem",
    "snapshot_restore",
    "spaces",
    "state_session_storage_redirect",
    "status_page",
    "table_vis",
    "tagcloud",
    "task_manager",
    "tile_map",
    "tilemap",
    "timelion",
    "translations",
    "ui_metric",
    "upgrade_assistant",
    "uptime",
    "vega",
    "watcher",
    "xpack_main"
  ]
}
 */

// ensure the csp nonce is set in the dll
import 'dll/set_csp_nonce';

// set the csp nonce in the primary webpack bundle too
__webpack_nonce__ = window.__kbnNonce__;

// import global polyfills
import '@babel/polyfill';
import 'custom-event-polyfill';
import 'whatwg-fetch';
import 'abortcontroller-polyfill';
import 'childnode-remove-polyfill';

import { i18n } from '@kbn/i18n';
import { CoreSystem } from '__kibanaCore__'

const injectedMetadata = JSON.parse(document.querySelector('kbn-injected-metadata').getAttribute('data'));

i18n.load(injectedMetadata.i18n.translationsUrl)
  .catch(e => e)
  .then((i18nError) => {
    const coreSystem = new CoreSystem({
      injectedMetadata,
      rootDomElement: document.body,
      browserSupportsCsp: !window.__kbnCspNotEnforced__,
      requireLegacyFiles: () => {
        require('plugins/canvas/app');
      }
    });

    coreSystem
      .setup()
      .then((coreSetup) => {
        if (i18nError) {
          coreSetup.fatalErrors.add(i18nError);
        }

        return coreSystem.start();
      });
  });
