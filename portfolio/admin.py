from django.contrib import admin
from .models import Project, Skill, Experience, ContactMessage, SiteProfile, SiteSettings


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About Me', {
            'fields': ['about_heading', 'about_tagline', 'about_bio'],
            'description': 'Heading and tagline appear on the About page header. Bio appears on both the About page and the homepage.',
        }),
        ('Contact Info', {
            'fields': ['contact_email', 'contact_location', 'linkedin_url'],
            'description': 'These values appear on the Contact page.',
        }),
    ]

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Resume', {
            'fields': ['resume_pdf'],
            'description': 'Upload your resume PDF. The existing file will be replaced when a new one is uploaded.',
        }),
    ]

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']
    search_fields = ['title', 'summary']
    search_fields = ['title', 'summary']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']
    exclude = ['proficiency']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'location', 'start_date', 'end_date', 'employment_type', 'is_education', 'order']
    list_editable = ['order']
    list_filter = ['is_education', 'employment_type']
    fieldsets = [
        ('Basic Info', {
            'fields': ['organization', 'location', 'start_date', 'end_date', 'order']
        }),
        ('Work Details', {
            'fields': ['title', 'employment_type', 'description'],
        }),
        ('Education Details', {
            'fields': ['is_education', 'degree_major', 'gpa_honors'],
            'description': 'Fill in degree/major and GPA or honors for education entries.',
        }),
    ]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_at', 'read']
    list_filter = ['read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']
