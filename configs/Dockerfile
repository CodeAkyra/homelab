FROM php:8.2-apache

#INSTALL MYSQL EXTENSIONS  
RUN docker-php-ext-install mysqli pdo pdo_mysql

#ENABLE APACHE MOD_REWRITE FOR URL REWRITING
RUN a2enmod rewrite

#SET WORKING DIRECTORY
WORKDIR /var/www/html

#EXPOSE PORT 80
EXPOSE 80

#START APACHE IN FOREGROUD
CMD ["apache2-foreground"]
