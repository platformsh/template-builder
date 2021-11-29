KIBANA_VERSION=$(cat kibana_version)

wget --quiet -c https://artifacts.elastic.co/downloads/kibana/kibana-$KIBANA_VERSION-$KIBANA_PLATFORM.tar.gz -O - | tar -xz
rm kibana-$KIBANA_VERSION-$KIBANA_PLATFORM/config/kibana.yml
mv kibana-$KIBANA_VERSION-$KIBANA_PLATFORM kibana
mv _config/kibana.yml kibana/config/kibana.yml
