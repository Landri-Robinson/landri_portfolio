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

gunicorn config.wsgi:application
