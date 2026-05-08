#!/usr/bin/env bash
set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Load fixture only if the database has no projects yet
python manage.py shell -c "
from portfolio.models import Project
if not Project.objects.exists():
    from django.core.management import call_command
    call_command('loaddata', 'portfolio/fixtures/production_data.json')
    print('Fixture loaded.')
else:
    print('Data already exists — skipping fixture load.')
"

# Create superuser from env vars if one does not exist yet
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
if username and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created.')
else:
    print('Superuser already exists or env vars not set.')
"

gunicorn config.wsgi:application
