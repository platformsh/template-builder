reset_config () {
    # Copy over basic configuration
    cp -R _config/* src/config/
    # remove any existing data in the mount
    rm -rf src/data/*
    # Cleanup the database
    mysql -h database.internal < nukedb.sql
}

install () {
    # Initial installation
    ./occ  maintenance:install --database "mysql" --database-host "database.internal" --database-name "main" --database-user "user" --database-pass "" --admin-user $ADMIN_USER --admin-pass $ADMIN_PASSWORD --data-dir="/app/src/data"
    # Mark installation as done
    rm src/config/CAN_INSTALL
    # Copy over the base config (as nextcloud would have overwritten it)
    cp -f _config/config.php src/config/config.php
    # Change the config to say it is installed
    sed -i "s/  'installed' => false,/  'installed' => true,/g" src/config/config.php
    ./occ upgrade
}

add_user (){
    ./occ group:add users
    # Create a user
    OC_PASS=$NEXTCLOUD_PASSWORD php src/occ user:add $NEXTCLOUD_USER  -g users --password-from-env
    # set their email
    ./occ user:setting $NEXTCLOUD_USER settings email $NEXTCLOUD_USER
    # Set the quota for the user
    curl -u"$ADMIN_USER:$ADMIN_PASSWORD" -X PUT http://localhost/ocs/v1.php/users/$NEXTCLOUD_USER -d key="quota" -d value=$NEXTCLOUD_QUOTA
}

# This is run within the deployment hook if the configuration is not yet done.
# If environment variable set create the admin account.
if [[ -z "${ADMIN_USER}" ]]; then
    ADMIN_USER='admin'
    ADMIN_PASSWORD=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-12})
    echo -e "No ADMIN_USER set, generating admin account and password.\nTo login to your instance:\nUser: ${GREEN}${ADMIN_USER}${NC}\nPassword: ${RED}${ADMIN_PASSWORD}${NC}\n"
    echo -e  "${RED}You should change your password after installation and add an email to your account${NC}"
fi

reset_config
install
# Set cron to run as cron
./occ background:cron
