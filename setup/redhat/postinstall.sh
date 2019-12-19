#!/bin/sh

set -e

COFFICE_CONFIGURATION_DIR=/etc/coffice
COFFICE_CONFIGURATION_FILE=$COFFICE_CONFIGURATION_DIR/coffice.conf
COFFICE_DATA_DIR=/var/lib/coffice
COFFICE_GROUP="coffice"
COFFICE_LOG_DIR=/var/log/coffice
COFFICE_LOG_FILE=$COFFICE_LOG_DIR/coffice-server.log
COFFICE_USER="coffice"

if ! getent passwd | grep -q "^coffice:"; then
    groupadd $COFFICE_GROUP
    adduser --system --no-create-home $COFFICE_USER -g $COFFICE_GROUP
fi
# Register "$COFFICE_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $COFFICE_USER" 2> /dev/null || true
# Configuration file
mkdir -p $COFFICE_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $COFFICE_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $COFFICE_USER
db_password = False
addons_path = /usr/lib/python3.7/site-packages/coffice/addons
" > $COFFICE_CONFIGURATION_FILE
    chown $COFFICE_USER:$COFFICE_GROUP $COFFICE_CONFIGURATION_FILE
    chmod 0640 $COFFICE_CONFIGURATION_FILE
fi
# Log
mkdir -p $COFFICE_LOG_DIR
chown $COFFICE_USER:$COFFICE_GROUP $COFFICE_LOG_DIR
chmod 0750 $COFFICE_LOG_DIR
# Data dir
mkdir -p $COFFICE_DATA_DIR
chown $COFFICE_USER:$COFFICE_GROUP $COFFICE_DATA_DIR

INIT_FILE=/lib/systemd/system/coffice.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=COffice Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=coffice
Group=coffice
ExecStart=/usr/bin/coffice --config $COFFICE_CONFIGURATION_FILE --logfile $COFFICE_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
