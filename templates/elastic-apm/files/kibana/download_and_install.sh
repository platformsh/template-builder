wget --quiet https://artifacts.elastic.co/downloads/kibana/kibana-$KIBANA_VERSION-$KIBANA_PLATFORM.tar.gz
shasum -a 512 kibana-$KIBANA_VERSION-$KIBANA_PLATFORM.tar.gz
tar -xzf kibana-$KIBANA_VERSION-$KIBANA_PLATFORM.tar.gz
rm kibana-$KIBANA_VERSION-$KIBANA_PLATFORM/config/kibana.yml
mv kibana-$KIBANA_VERSION-$KIBANA_PLATFORM kibana
mv _config/kibana.yml kibana/config/kibana.yml
rm kibana-$KIBANA_VERSION-$KIBANA_PLATFORM.tar.gz
