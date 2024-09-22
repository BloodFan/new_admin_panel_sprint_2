FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UWSGI_PROCESSES=1 \
    UWSGI_THREADS=16 \
    UWSGI_HARAKIRI=240 \
    DJANGO_SETTINGS_MODULE='example.settings' \
    APP_HOME=/opt/app

WORKDIR $APP_HOME

ARG GID=1000
ARG UID=1000
ARG USER=ubuntu

COPY ./app $APP_HOME
# COPY ./data $APP_HOME

RUN apk add --update --no-cache python3-dev postgresql-dev curl nginx \
    build-base musl-dev linux-headers openssl libffi-dev uwsgi-python3 libc-dev pcre-dev && \
    addgroup -g $GID -S $USER && \
    adduser -S $USER -G $USER --uid "$UID" && \
    mkdir -p /uwsgi_socket $APP_HOME/static $APP_HOME/media && \
    chmod -R 777 /uwsgi_socket $APP_HOME/static $APP_HOME/media && \
    chown -R $USER:$USER /uwsgi_socket $APP_HOME

ENV UWSGI_PROFILE=core

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    python manage.py collectstatic --no-input && \
    chown -R $USER:$USER /etc/nginx /var/lib/nginx/ /var/log /run/nginx/

COPY ["./docker/dev/uwsgi/run_uwsgi.sh", "./docker/dev/uwsgi/conf/uwsgi.ini", "./docker/dev/app/entrypoints/entrypoint.sh", "/"]

RUN chmod +x /*.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

USER $USER