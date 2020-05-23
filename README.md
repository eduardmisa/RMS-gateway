# API Gateway

# To connect containers:
Create external network named "rms_network"

snippet:
docker network create --gateway 172.18.0.1 --subnet 172.18.0.0/24 rms_network

# Centos Nginx Settings
sudo setsebool -P httpd_unified 1