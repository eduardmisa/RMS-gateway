# !/bin/bash

source ./0-configuration.sh

echo "===============================================================";
echo "====================== REMOVING CONTAINER =====================";
echo "======================    PLEASE WAIT.    =====================";
echo "===============================================================";

cd $DEPLOYMENT_PATH
docker-compose -f docker-compose.yml down

echo "===============================================================";
echo "====================== BUILDING CONTAINER =====================";
echo "======================    PLEASE WAIT.    =====================";
echo "===============================================================";

cd $DEPLOYMENT_PATH
docker-compose -f docker-compose.yml up -d --build

