echo "===============================================================";
echo "====================== REMOVING CONTAINER =====================";
echo "======================    PLEASE WAIT.    =====================";
echo "===============================================================";

cd /var/www/template.templatesystem.com
docker-compose -f docker-compose.yml down

echo "===============================================================";
echo "====================== BUILDING CONTAINER =====================";
echo "======================    PLEASE WAIT.    =====================";
echo "===============================================================";

cd /var/www/template.templatesystem.com
docker-compose -f docker-compose.yml up -d --build

