#!/bin/bash

# load mysql tzinfo (see http://dev.mysql.com/doc/refman/5.5/en/mysql-tzinfo-to-sql.html)
mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql

# create app locks directory
if [ ! -d /var/www/vagrant/app/locks ]; then
    mkdir -p /var/www/vagrant/app/locks
fi

su www-data -c "composer install -n -d /var/www/vagrant"
su www-data -c "(cd /var/www/vagrant && bower install --allow-root -f)"
su www-data -c "php /var/www/vagrant/app/console assetic:dump"
su www-data -c "php /var/www/vagrant/app/console doctrine:schema:update --force"

# create file to indicate if doctrine:fixtures:load is needed
if [ ! -d /var/www/.doctrine ]; then
    mkdir /var/www/.doctrine
fi
if [ ! -f /var/www/.doctrine/fixtures ]; then
    su www-data -c "php /var/www/vagrant/app/console doctrine:fixtures:load --no-interaction"
    touch /var/www/.doctrine/fixtures
fi