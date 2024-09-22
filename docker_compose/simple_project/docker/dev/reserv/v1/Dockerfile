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

COPY ./app/requirements.txt requirements.txt

RUN apk add --update --no-cache python3-dev postgresql-dev curl nginx \
    build-base musl-dev linux-headers openssl libffi-dev uwsgi-python3 uwsgi && \
    addgroup -g $GID -S $USER && \
    adduser -S $USER -G $USER --uid "$UID" && \
    mkdir -p /uwsgi_socket && \
    chmod -R 777 /uwsgi_socket && \
    chown -R $USER:$USER /uwsgi_socket && \
    mkdir -p /opt/app/static /opt/app/media && \
    chown -R $USER:$USER /opt/app/static /opt/app/media && \
    chmod -R 777 /opt/app/static /opt/app/media && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

COPY --chown=$USER:$USER ./docker/dev/uwsgi/run_uwsgi.sh /
COPY --chown=$USER:$USER ./docker/dev/uwsgi/conf/uwsgi.ini /
COPY --chown=$USER:$USER ./docker/dev/app/entrypoints/entrypoint.sh /
COPY ./docker/dev/nginx/conf.d /etc/nginx/conf.d
COPY ./docker/dev/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./app $APP_HOME
COPY ./data $APP_HOME

RUN chmod +x /*.sh && \
    python manage.py collectstatic --no-input && \
    chown -R $USER:$USER $APP_HOME && \
    chmod -R 777 $APP_HOME && \
    chown -R $USER:$USER /etc/nginx /var/lib/nginx/ /var/log /run/nginx/

ENTRYPOINT ["/entrypoint.sh"]

# CMD ["/run_uwsgi.sh"]

# CMD ["uwsgi", "--strict", "--ini", "uwsgi.ini"]
EXPOSE 8000

USER $USER