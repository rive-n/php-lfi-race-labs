FROM debian:buster

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
	apt-get install -y nginx \ 
	php-fpm supervisor && rm -rf /var/lib/apt/lists/

# Conflict fixes
RUN mkdir -p /var/run/php

# Configs installation
COPY Nginx/default /etc/nginx/sites-enabled/default
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Task dir preps
RUN rm -rf /var/www/html/
COPY app/index.php /var/www/html/index.php

# Task rules
RUN mkdir /var/www/html/files && \
	chown www-data:www-data /var/www/html/files && \
	mkdir /var/www/html/well-known && \
	chown www-data:www-data /var/www/html/well-known
RUN chown -R root:root /var/tmp && \
    chmod -R 000 /var/tmp
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

CMD supervisord -n -c /etc/supervisor/supervisord.conf
