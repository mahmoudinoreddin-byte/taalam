from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Profile, WorkExperience, Skill, Certification, Project, Tool, Language, SocialLink
from .forms import (ProfilePersonalForm, ProfileProfessionalForm, ProfileBusinessForm,
                    WorkExperienceForm, SkillForm, CertificationForm, ProjectForm,
                    ToolForm, LanguageForm, SocialLinkForm)

def get_or_create_profile(user):
    profile, created = Profile.objects.get_or_create(user=user)
    return profile

@login_required
def dashboard(request):
    profile = get_or_create_profile(request.user)
    context = {
        'profile': profile,
        'experiences': profile.experiences.all(),
        'skills': profile.skills.all(),
        'certifications': profile.certifications.all(),
        'projects': profile.projects.all(),
        'tools': profile.tools.all(),
        'languages': profile.languages.all(),
        'social_links': profile.social_links.all(),
    }
    return render(request, 'profiles/dashboard.html', context)

# ── PERSONAL ──────────────────────────────────────────────
@login_required
def edit_personal(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ProfilePersonalForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal profile updated!')
            return redirect('dashboard')
    else:
        form = ProfilePersonalForm(instance=profile)
    return render(request, 'profiles/edit_section.html', {'form': form, 'title': 'Edit Personal Profile', 'section': 'personal'})

# ── PROFESSIONAL ──────────────────────────────────────────
@login_required
def edit_professional(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ProfileProfessionalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professional info updated!')
            return redirect('dashboard')
    else:
        form = ProfileProfessionalForm(instance=profile)
    return render(request, 'profiles/edit_section.html', {'form': form, 'title': 'Edit Professional Info', 'section': 'professional'})

# ── BUSINESS ──────────────────────────────────────────────
@login_required
def edit_business(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ProfileBusinessForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Business info updated!')
            return redirect('dashboard')
    else:
        form = ProfileBusinessForm(instance=profile)
    return render(request, 'profiles/edit_section.html', {'form': form, 'title': 'Edit Business Info', 'section': 'business'})

# ── WORK EXPERIENCE ───────────────────────────────────────
@login_required
def manage_experiences(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.profile = profile
            exp.save()
            messages.success(request, 'Experience added!')
            return redirect('manage_experiences')
    else:
        form = WorkExperienceForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.experiences.all(),
        'title': 'Work Experience', 'item_type': 'experience'
    })

@login_required
def delete_experience(request, pk):
    exp = get_object_or_404(WorkExperience, pk=pk, profile__user=request.user)
    exp.delete()
    messages.success(request, 'Experience removed.')
    return redirect('manage_experiences')

# ── SKILLS ────────────────────────────────────────────────
@login_required
def manage_skills(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = profile
            skill.save()
            messages.success(request, 'Skill added!')
            return redirect('manage_skills')
    else:
        form = SkillForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.skills.all(),
        'title': 'Skills', 'item_type': 'skill'
    })

@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, profile__user=request.user)
    skill.delete()
    return redirect('manage_skills')

# ── CERTIFICATIONS ────────────────────────────────────────
@login_required
def manage_certifications(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.profile = profile
            cert.save()
            messages.success(request, 'Certification added!')
            return redirect('manage_certifications')
    else:
        form = CertificationForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.certifications.all(),
        'title': 'Certifications', 'item_type': 'certification'
    })

@login_required
def delete_certification(request, pk):
    cert = get_object_or_404(Certification, pk=pk, profile__user=request.user)
    cert.delete()
    return redirect('manage_certifications')

# ── PROJECTS ─────────────────────────────────────────────
@login_required
def manage_projects(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.profile = profile
            proj.save()
            messages.success(request, 'Project added!')
            return redirect('manage_projects')
    else:
        form = ProjectForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.projects.all(),
        'title': 'Projects', 'item_type': 'project'
    })

@login_required
def delete_project(request, pk):
    proj = get_object_or_404(Project, pk=pk, profile__user=request.user)
    proj.delete()
    return redirect('manage_projects')

# ── TOOLS ────────────────────────────────────────────────
@login_required
def manage_tools(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.profile = profile
            tool.save()
            messages.success(request, 'Tool added!')
            return redirect('manage_tools')
    else:
        form = ToolForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.tools.all(),
        'title': 'Tools & Setup', 'item_type': 'tool'
    })

@login_required
def delete_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk, profile__user=request.user)
    tool.delete()
    return redirect('manage_tools')

# ── LANGUAGES ────────────────────────────────────────────
@login_required
def manage_languages(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            lang = form.save(commit=False)
            lang.profile = profile
            lang.save()
            messages.success(request, 'Language added!')
            return redirect('manage_languages')
    else:
        form = LanguageForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.languages.all(),
        'title': 'Languages', 'item_type': 'language'
    })

@login_required
def delete_language(request, pk):
    lang = get_object_or_404(Language, pk=pk, profile__user=request.user)
    lang.delete()
    return redirect('manage_languages')

# ── SOCIAL LINKS ─────────────────────────────────────────
@login_required
def manage_social_links(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.profile = profile
            link.save()
            messages.success(request, 'Link added!')
            return redirect('manage_social_links')
    else:
        form = SocialLinkForm()
    return render(request, 'profiles/manage_list.html', {
        'form': form, 'items': profile.social_links.all(),
        'title': 'Social Links', 'item_type': 'social_link'
    })

@login_required
def delete_social_link(request, pk):
    link = get_object_or_404(SocialLink, pk=pk, profile__user=request.user)
    link.delete()
    return redirect('manage_social_links')
