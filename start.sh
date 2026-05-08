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

# Create or update superuser from env vars
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
if username and password:
    user, created = User.objects.get_or_create(username=username)
    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()
    print('Superuser created.' if created else 'Superuser updated.')
"

gunicorn config.wsgi:application
