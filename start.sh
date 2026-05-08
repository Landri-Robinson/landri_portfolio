#!/usr/bin/env bash
set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py load_initial_data
python manage.py ensure_superuser

gunicorn config.wsgi:application
