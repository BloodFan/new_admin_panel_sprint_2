#!/bin/sh

set -e # забить на ошибку

uwsgi --strict --ini /uwsgi.ini
