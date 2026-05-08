import os
from django.core.management.base import BaseCommand
from django.conf import settings
from portfolio.models import Project, Skill, SiteProfile


class Command(BaseCommand):
    help = 'Export portfolio content to a text file for chatbot training'

    def handle(self, *args, **kwargs):
        lines = []

        lines += [
            '=========================================',
            'LANDRI ROBINSON — CHATBOT TRAINING CONTENT',
            '=========================================',
            '',
        ]

        # About
        profile = SiteProfile.objects.first()
        lines += ['--- ABOUT ---']
        if profile:
            lines += [
                f'Heading: {profile.about_heading}',
                f'Tagline: {profile.about_tagline}',
                f'Bio: {profile.about_bio}',
            ]
        lines.append('')

        # Skills grouped by category
        lines += ['--- SKILLS ---']
        for code, label in Skill.SKILL_CATEGORY_CHOICES:
            names = list(Skill.objects.filter(category=code).order_by('order').values_list('name', flat=True))
            if names:
                lines.append(f'{label}: {", ".join(names)}')
        lines.append('')

        # Projects
        lines += ['--- PROJECTS ---', '']
        for project in Project.objects.all():
            lines += [
                f'== {project.title} ==',
                f'Category: {project.get_category_display()}',
                f'Summary: {project.summary}',
                f'Business Problem: {project.business_problem}',
                f'Tools Used: {project.tools_used}',
                f'Key Features: {project.key_features}',
                f'Role: {project.role}',
                f'Challenges: {project.challenges}',
                f'Lessons Learned: {project.lessons_learned}',
                '',
            ]

        output_path = os.path.join(settings.BASE_DIR, 'chatbot_training_content.txt')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        self.stdout.write(self.style.SUCCESS(f'Exported to {output_path}'))
