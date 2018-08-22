FROM alpine:3.7

ENV GOSU_VERSION 1.7

RUN set -x \
        && addgroup -S mysql && adduser -D -S -h /var/cache/mysql -s /sbin/nologin -G mysql mysql \
        && apk add --no-cache mysql \
              mysql-client \
              openrc \
        && rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /run/mysqld \
        && chown -R mysql:mysql /var/lib/mysql /run/mysqld \
        && chmod 777 /run/mysqld \
        && cp -f /usr/share/mysql/mysql.server /etc/init.d/mysqld \
        && rc-update add mysqld

VOLUME ["/var/lib/mysql", "/var/init"]

EXPOSE 3306
CMD ["/bin/sh", "-c", "/var/init/init && /bin/sh"]
