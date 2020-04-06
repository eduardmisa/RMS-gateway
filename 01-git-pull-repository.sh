set password "repository_admin_password"

cd /var/www/template.templatesystem.com
spawn git pull "http://admin@gitserver:80/scm/template_app.git" master
expect "Password for"
send "$password\n"
interact