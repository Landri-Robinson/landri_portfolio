from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('chatbot', 'Chatbot'),
        ('agent', 'AI Agent'),
        ('ml', 'Machine Learning'),
        ('web', 'Web Development'),
        ('media', 'AI Media'),
        ('workflow', 'Workflow Automation'),
        ('google_ai_studio', 'Google AI Studio Media Project'),
    ]

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='agent')
    tools_used = models.TextField(help_text="Comma-separated list of tools")
    business_problem = models.TextField(default='')
    key_features = models.TextField(help_text="Describe the key features", default='')
    role = models.TextField(help_text="Your role and contribution", default='')
    challenges = models.TextField(help_text="Biggest challenge faced")
    lessons_learned = models.TextField(help_text="What you learned")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    links = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    demo_link = models.URLField(blank=True, null=True, help_text="Live demo or deployed project URL")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_tools_list(self):
        return [t.strip() for t in self.tools_used.split(',') if t.strip()]


class Skill(models.Model):
    SKILL_CATEGORY_CHOICES = [
        ('ai', 'AI & Machine Learning'),
        ('web', 'Web Development'),
        ('data', 'Data & Analytics'),
        ('tools', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=SKILL_CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Percentage 0-100")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name


class Experience(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('', '—'),
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=200, verbose_name='Job Title')
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, default='')
    start_date = models.CharField(max_length=50, blank=True, default='')
    end_date = models.CharField(max_length=50, default='Present')
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_education = models.BooleanField(default=False)
    degree_major = models.CharField(max_length=200, blank=True, default='', help_text="Degree and/or major (education only)")
    gpa_honors = models.CharField(max_length=100, blank=True, default='', help_text="GPA or honors (education only)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} at {self.organization}"


class SiteProfile(models.Model):
    about_heading = models.CharField(
        max_length=200,
        default='Focused on AI & intelligent systems',
        help_text='Heading shown in the About Me section on the homepage',
    )
    about_bio = models.TextField(
        default='My work spans chatbots, AI agents, machine learning pipelines, and full-stack web applications. I believe in using technology to solve real problems — clearly, efficiently, and creatively.',
        help_text='Main bio paragraph — shown on the About page and homepage',
    )
    about_tagline = models.CharField(
        max_length=200,
        default='Problem-solver with a passion for AI and intelligent systems.',
        help_text='Short tagline shown under the page title on the About page',
    )
    contact_email = models.EmailField(
        blank=True,
        default='',
        help_text='Email address shown on the Contact page',
    )
    contact_location = models.CharField(
        max_length=200,
        blank=True,
        default='',
        help_text='Location shown on the Contact page (e.g. Waco, Texas)',
    )
    linkedin_url = models.URLField(
        blank=True,
        default='',
        help_text='Full LinkedIn profile URL',
    )

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return 'Site Profile'


class SiteSettings(models.Model):
    resume_pdf = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        help_text='Upload your resume as a PDF file',
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
