from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Min
from .models import Project, Skill, Experience, SiteProfile, SiteSettings
from .forms import ContactForm, SearchForm


def home(request):
    featured_projects = Project.objects.all()[:6]
    profile = SiteProfile.objects.first() or SiteProfile()
    return render(request, 'portfolio/home.html', {
        'featured_projects': featured_projects,
        'profile': profile,
    })


def about(request):
    experiences = Experience.objects.filter(is_education=False)
    education = Experience.objects.filter(is_education=True)
    profile = SiteProfile.objects.first() or SiteProfile()
    return render(request, 'portfolio/about.html', {
        'experiences': experiences,
        'education': education,
        'profile': profile,
    })


def projects(request):
    form = SearchForm(request.GET)
    all_projects = Project.objects.all()

    query = request.GET.get('query', '')
    category = request.GET.get('category', '')

    if query:
        all_projects = all_projects.filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(tools_used__icontains=query)
        )
    if category:
        all_projects = all_projects.filter(category=category)

    categories = Project.CATEGORY_CHOICES
    return render(request, 'portfolio/projects.html', {
        'projects': all_projects,
        'form': form,
        'categories': categories,
        'selected_category': category,
        'query': query,
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    other_projects = Project.objects.exclude(pk=pk)[:3]
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'other_projects': other_projects,
    })


def skills(request):
    ai_skills = Skill.objects.filter(category='ai')
    web_skills = Skill.objects.filter(category='web')
    data_skills = Skill.objects.filter(category='data')
    tool_skills = Skill.objects.filter(category='tools')
    soft_skills = Skill.objects.filter(category='soft')
    return render(request, 'portfolio/skills.html', {
        'ai_skills': ai_skills,
        'web_skills': web_skills,
        'data_skills': data_skills,
        'tool_skills': tool_skills,
        'soft_skills': soft_skills,
    })


def resume(request):
    experiences = Experience.objects.filter(is_education=False)
    education = Experience.objects.filter(is_education=True)
    skills = Skill.objects.all()

    exp_min = experiences.aggregate(Min('order'))['order__min']
    edu_min = education.aggregate(Min('order'))['order__min']

    if exp_min is None:
        experience_first = False
    elif edu_min is None:
        experience_first = True
    else:
        experience_first = exp_min <= edu_min

    site_settings = SiteSettings.objects.first()
    return render(request, 'portfolio/resume.html', {
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'experience_first': experience_first,
        'site_settings': site_settings,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    profile = SiteProfile.objects.first() or SiteProfile()
    return render(request, 'portfolio/contact.html', {'form': form, 'profile': profile})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/dashboard.html', {'projects': projects})
