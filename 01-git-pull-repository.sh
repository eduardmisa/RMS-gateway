# !/bin/sh

source ./0-configuration.sh

set password "531ed96864Z"

cd $DEPLOYMENT_PATH
spawn git pull "https://eduardmisa@github.com/eduardmisa/RMS-gateway.git" master
expect "Password for"
send "$password\n"
interact