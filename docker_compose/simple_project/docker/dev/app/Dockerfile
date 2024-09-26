FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/opt/app

ARG GID=1000
ARG UID=1000
ARG USER=ubuntu

RUN apk add --update --no-cache python3-dev postgresql-dev curl nginx gettext && \
    addgroup -g $GID -S $USER && \
    adduser -S $USER -G $USER --uid "$UID"

WORKDIR $APP_HOME

COPY --chown=$USER:$USER ./docker/dev/app/entrypoints/entrypoint.sh /
COPY --chown=$USER:$USER ./app $APP_HOME

RUN pip install --upgrade pip setuptools && \
    pip install --editable .[dev]

RUN chmod +x /*.sh && \
    mkdir -p media && \
    chown -R $USER:$USER $APP_HOME media

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

USER $USER
