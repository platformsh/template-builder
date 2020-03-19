if [[ -z "${NEXTCLOUD_VERSION}" ]]; then
mkdir -p _update
cd _update
if [ ! -f "nextcloud-${NEXTCLOUD_VERSION}.zip" ]; then
wget https://download.nextcloud.com/server/releases/nextcloud-$VERSION.zip
fi
unzip nextcloud-$VERSION.zip
rm -rf ../src
mv nextcloud/ ../src/
rm -rf ../src/config
chmod +x src/occ
else
echo "Required environment variable NEXTCLOUD_VERSION have not been set. Update can not proceed." 1>&2
exit 1
fi
# we potentially want an update mechanisme for preview-generator