from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='portfolio.Project')
def sync_skills_from_project(sender, instance, **kwargs):
    from .models import Skill
    for tool in instance.get_tools_list():
        Skill.objects.get_or_create(
            name__iexact=tool,
            defaults={'name': tool, 'category': 'tools', 'proficiency': 80},
        )
