from django.core.management.base import BaseCommand
from portfolio.models import Project, Skill


class Command(BaseCommand):
    help = 'Create Skill entries for every tool listed in existing projects'

    def handle(self, *args, **options):
        created_count = 0
        for project in Project.objects.all():
            for tool in project.get_tools_list():
                _, created = Skill.objects.get_or_create(
                    name__iexact=tool,
                    defaults={'name': tool, 'category': 'tools', 'proficiency': 80},
                )
                if created:
                    created_count += 1
                    self.stdout.write(f'  Created skill: {tool}')
        self.stdout.write(self.style.SUCCESS(f'Done — {created_count} new skill(s) created.'))
