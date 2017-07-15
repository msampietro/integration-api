FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip python-dev sqlite3 libsqlite3-dev uwsgi-plugin-python \
    nginx supervisor
COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY integration-api /var/www/integration-api

RUN mkdir -p /var/log/nginx/integration-api /var/log/uwsgi/integration-api /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
	&& alias python=python3 \
    &&  pip3 install -r /var/www/integration-api/requirements.txt \
    && chown -R www-data:www-data /var/www/integration-api \
    && chown -R www-data:www-data /var/log

CMD ["/usr/bin/supervisord"]
