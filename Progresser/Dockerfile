FROM debian:buster

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y nginx php-fpm supervisor && \
    rm -rf /var/lib/apt/lists/


# Conflict Fix
RUN mkdir -p /var/run/php

# Confings installations
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY Nginx/default /etc/nginx/sites-enabled/default
COPY app/www.conf /etc/php/7.4/fpm/pool.d/www.conf

# Task dir preps
RUN rm -rf /var/www/html/
COPY app/ /var/www/html/

# Creating links
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Starting supervisor(d)
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
