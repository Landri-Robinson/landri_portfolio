from django.core.management.base import BaseCommand
from django.core.management import call_command
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Load production fixture only if the database has no projects yet'

    def handle(self, *args, **kwargs):
        if Project.objects.exists():
            self.stdout.write('Data already exists — skipping fixture load.')
            return

        call_command('loaddata', 'portfolio/fixtures/production_data.json')
        self.stdout.write(self.style.SUCCESS('Fixture loaded successfully.'))
