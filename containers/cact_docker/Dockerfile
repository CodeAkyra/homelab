FROM ubuntu:22.04

#SET ENVIRONMENT VARIABLES
ENV DEBIAN_FRONTEND=noninteractive

#UPDATE AND INSTALL DEPENDENCIES
RUN apt-get update && apt-get install -y \
    apache2 \
    php \
    php-mysql \
    php-snmp \
    php-ldap \
    php-gd \
    php-gmp \
    php-xml \
    php-cli \
    mysql-client \
    snmp \
    snmpd \
    rrdtool \
    curl \
    wget \
    git \
    cron \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

#ENABLE APACHE MODULE
RUN a2enmod php8.1 rewrite

#CREATE CACTI DIRECTORY
RUN mkdir -p /var/www/html/cacti
WORKDIR /var/www/html/cacti

#DOWNLOAD AND EXTRACT CACTI
RUN wget -q https://www.cacti.net/downloads/cacti-latest.tar.gz -O /tmp/cacti.tar.gz && \
    tar -xzf /tmp/cacti.tar.gz -C /var/www/html/cacti --strip-components=1 && \
    rm /tmp/cacti.tar.gz

#SET PERMISSION
RUN chown -R www-data:www-data /var/www/html/cacti && \
    chmod -R 755 /var/www/html/cacti

#CONFIGURE APACHE
RUN echo "<VirtualHost *:80>" > /etc/apache2/sites-available/cacti.conf && \
    echo "    ServerName cacti" >> /etc/apache2/sites-available/cacti.conf && \
    echo "    DocumentRoot /var/www/html/cacti" >> /etc/apache2/sites-available/cacti.conf && \
    echo "    <Directory /var/www/html/cacti>" >> /etc/apache2/sites-available/cacti.conf && \
    echo "        AllowOverride All" >> /etc/apache2/sites-available/cacti.conf && \
    echo "        Require all granted" >> /etc/apache2/sites-available/cacti.conf && \
    echo "    </Directory>" >> /etc/apache2/sites-available/cacti.conf && \
    echo "</VirtualHost>" >> /etc/apache2/sites-available/cacti.conf

RUN a2ensite cacti && a2dissite 000-default

#EXPOSE PORT 80
EXPOSE 80

#START APACHE
CMD ["apache2ctl", "-D", "FOREGROUND"]
