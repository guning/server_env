FROM alpine:3.9

LABEL maintainer="guning <guningh@gmail.com>"

ENV NGINX_VERSION 1.14.2
ENV PHP_VERSION 7.3.2

# install dependencies
RUN apk add --no-cache --virtual .build-deps\
        openssl \
        ca-certificates \
        build-base \
    && apk add --no-cache \
        curl \
        libxml2-dev \
        bzip2-dev \
        curl-dev \
        libzip-dev \
    && echo "http://nginx.org/packages/alpine/v3.9/main" | tee -a /etc/apk/repositories \
    && curl -o /tmp/nginx_signing.rsa.pub https://nginx.org/keys/nginx_signing.rsa.pub \
    && mv /tmp/nginx_signing.rsa.pub /etc/apk/keys/ \
    && apk add --no-cache nginx \
    && cd /tmp && wget http://jp2.php.net/get/php-7.3.2.tar.gz/from/this/mirror -O php.tar.gz \
    && tar zxf php.tar.gz && cd php-7.3.2 \
    && ./configure \
        --prefix=/usr/local/php \
        --enable-cgi \
        --with-pcre-regex \
        --enable-fpm \
        --with-zlib \
        --with-bz2 \
        --with-curl \
        --enable-mbstring \
        --with-mysqli \
        --enable-pcntl \
        --with-pdo-mysql \
        --enable-sockets \
        --enable-zip \
        --with-libzip \
        --with-openssl \
    && make && make install \
    && /usr/local/php/bin/php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && /usr/local/php/bin/php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && /usr/local/php/bin/php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && /usr/local/php/bin/php -r "unlink('composer-setup.php');" \
    && cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf \
    && cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-fpm.d/www.conf \
    && ln -s /usr/local/php/sbin/php-fpm /usr/bin/php-fpm \
    && ln -s /usr/local/php/bin/php /usr/bin/php \
    && rm -rf /tmp/* \
    && apk del .build-deps
  

VOLUME ["/var/init", "/var/wwwroot", "/var/wwwlog"]
EXPOSE 80
CMD ["/bin/sh", "-c", "source /etc/profile && /var/init/init && /bin/sh"]
