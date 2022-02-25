FROM debian:bullseye

# Installing deps 
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y nginx \
    php-fpm supervisor && rm -rf /var/lib/apt/lists/

RUN mkdir -p /var/run/php

# Creating right configs
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY app/www.conf /etc/php/7.4/fpm/pool.d/www.conf
COPY Nginx/site.conf /etc/nginx/sites-enabled/default

# Creating task
RUN rm -rf /var/www/html/*
COPY app/ /var/www/html

# make sure you can't write tmp / session files
RUN chown -R root:root /tmp /var/tmp && \
    chmod -R 000 /tmp /var/tmp 

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

# CMD /etc/init.d/php7.4-fpm start && \
#    nginx -g 'daemon off;'
CMD supervisord -n -c /etc/supervisor/supervisord.conf
