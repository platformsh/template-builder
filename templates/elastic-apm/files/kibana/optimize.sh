rm -rf _kibana_optimize/
cd kibana
./bin/kibana --verbose --optimize -c config/kibana.yml
cp -r kibana/optimize/bundles _kibana_optimize