# API Gateway

# To connect containers:
Create external network named "rms_network"

snippet:
docker network create --gateway 172.18.0.1 --subnet 172.18.0.0/24 rms_network

# Centos Nginx Settings
sudo setsebool -P httpd_can_network_connect 1

semanage port -l | grep http_port_t
semanage port -a -t http_port_t  -p tcp 8090
sudo chcon -v -R --type=httpd_sys_content_t /path/to/static-deployment-files
