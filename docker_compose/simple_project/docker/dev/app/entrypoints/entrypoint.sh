#!/bin/sh

# python manage.py makemigrations
python manage.py migrate

nginx -g 'daemon on;'

set -e

uwsgi --ini /uwsgi.ini
