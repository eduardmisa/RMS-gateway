set password "531ed96864Z"

cd /var/www/rms-gateway.u4rdsystem.com
spawn git pull "https://eduardmisa@github.com/eduardmisa/RMS-gateway.git" master
expect "Password for"
send "$password\n"
interact