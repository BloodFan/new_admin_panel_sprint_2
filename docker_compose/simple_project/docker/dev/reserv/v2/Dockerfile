FROM python:3.11-alpine3.15

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
COPY ./data $APP_HOME
COPY ./docker/dev/uwsgi/run_uwsgi.sh $APP_HOME/
COPY ./docker/dev/uwsgi/conf/uwsgi.ini $APP_HOME/
COPY ./docker/dev/app/entrypoints/entrypoint.sh $APP_HOME/

RUN apk add --update --no-cache python3-dev postgresql-dev curl nginx \
    build-base musl-dev linux-headers openssl libffi-dev uwsgi-python3 uwsgi && \
    addgroup -g $GID -S $USER && \
    adduser -S $USER -G $USER --uid "$UID" && \
    mkdir -p $APP_HOME/uwsgi_socket $APP_HOME/static $APP_HOME/media && \
    chmod -R 777 /opt && \
    chown -R $USER:$USER /opt && \
    chmod +x $APP_HOME/*.sh && \
    chown -R $USER:$USER $APP_HOME && \
    chmod -R 777 $APP_HOME && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    python manage.py collectstatic --no-input && \
    chown -R $USER:$USER /etc/nginx /var/lib/nginx/ /var/log /run/nginx/


ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000

USER $USER