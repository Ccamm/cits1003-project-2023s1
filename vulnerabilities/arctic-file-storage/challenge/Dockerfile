FROM directus/directus:9.22.4

USER root
RUN apk update && apk add nginx supervisor sqlite
COPY configs/supervisord.conf /etc/supervisord.conf
COPY configs/nginx.conf /etc/nginx/http.d/default.conf
COPY directus/directus.env /directus/.env
COPY html/ /var/www/html
COPY localonly/ /var/www/localonly/
COPY --chown=node:node directus/database.sqlite /directus/database/database.sqlite
COPY --chown=node:node scripts/cleanup.sh /directus/cleanup.sh
RUN chmod +x /directus/cleanup.sh

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]