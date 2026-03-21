from django import forms
from .models import Profile, WorkExperience, Skill, Certification, Project, Tool, Language, SocialLink

INPUT = 'w-full bg-bg2 border border-border rounded-xl px-4 py-3 text-text placeholder-muted focus:outline-none focus:border-accent text-sm'
SELECT = 'w-full bg-bg2 border border-border rounded-xl px-4 py-3 text-text focus:outline-none focus:border-accent text-sm'
TEXTAREA = 'w-full bg-bg2 border border-border rounded-xl px-4 py-3 text-text placeholder-muted focus:outline-none focus:border-accent text-sm resize-none'
CHECK = 'w-4 h-4 accent-accent'

class ProfilePersonalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','tagline','bio','location','birth_year','mbti','interests','contact_email','phone','is_available','is_public','theme_color']
        widgets = {
            'tagline': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. UX Designer & Strategist'}),
            'bio': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 4, 'placeholder': 'Tell your story...'}),
            'location': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. Oran, Algeria'}),
            'birth_year': forms.NumberInput(attrs={'class': INPUT, 'placeholder': 'e.g. 1996'}),
            'mbti': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. INFJ-T'}),
            'interests': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Photography, Design, Coffee...'}),
            'theme_color': forms.TextInput(attrs={'type': 'color', 'class': 'w-12 h-10 rounded cursor-pointer border-0'}),
            'contact_email': forms.EmailInput(attrs={'class': INPUT, 'placeholder': 'contact@email.com'}),
            'phone': forms.TextInput(attrs={'class': INPUT, 'placeholder': '+213 xx xxx xxxx'}),
            'phone': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. +213 555 123456'}),
            'contact_email': forms.EmailInput(attrs={'class': INPUT, 'placeholder': 'public@email.com'}),
            'is_available': forms.CheckboxInput(attrs={'class': CHECK}),
            'is_public': forms.CheckboxInput(attrs={'class': CHECK}),
        }

class ProfileProfessionalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['current_position','current_company','years_experience','remote_preference','expected_salary']
        widgets = {
            'current_position': forms.TextInput(attrs={'class': INPUT}),
            'current_company': forms.TextInput(attrs={'class': INPUT}),
            'years_experience': forms.NumberInput(attrs={'class': INPUT}),
            'remote_preference': forms.Select(attrs={'class': SELECT}),
            'expected_salary': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. $3000-5000/month'}),
        }

class ProfileBusinessForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['business_name','business_role','business_industry','business_description']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': INPUT}),
            'business_role': forms.TextInput(attrs={'class': INPUT}),
            'business_industry': forms.TextInput(attrs={'class': INPUT}),
            'business_description': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 3}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company','role','description','start_date','end_date','is_current']
        widgets = {
            'company': forms.TextInput(attrs={'class': INPUT}),
            'role': forms.TextInput(attrs={'class': INPUT}),
            'description': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': INPUT, 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': INPUT, 'type': 'date'}),
            'is_current': forms.CheckboxInput(attrs={'class': CHECK}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name','proficiency','category']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT}),
            'proficiency': forms.NumberInput(attrs={'class': INPUT, 'min': 1, 'max': 100}),
            'category': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. Design, Dev'}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name','issuer','year','url']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT}),
            'issuer': forms.TextInput(attrs={'class': INPUT}),
            'year': forms.NumberInput(attrs={'class': INPUT}),
            'url': forms.URLInput(attrs={'class': INPUT}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Link to documentation (optional)'}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Documentation link'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','emoji','status','project_url','github_url','technologies','role','duration','looking_for_collaborators','doc_url','doc_label','thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT}),
            'description': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 3}),
            'emoji': forms.TextInput(attrs={'class': INPUT, 'placeholder': '🚀'}),
            'status': forms.Select(attrs={'class': SELECT}),
            'project_url': forms.URLInput(attrs={'class': INPUT}),
            'github_url': forms.URLInput(attrs={'class': INPUT}),
            'technologies': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'React, Figma, Python...'}),
            'role': forms.TextInput(attrs={'class': INPUT}),
            'duration': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. 3 months'}),
            'looking_for_collaborators': forms.CheckboxInput(attrs={'class': CHECK}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Link to documentation (optional)'}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'https://docs.yourproject.com'}),
            'doc_label': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. Read Documentation'}),
        }

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name','emoji','category','description','url','doc_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT}),
            'emoji': forms.TextInput(attrs={'class': INPUT, 'placeholder': '🛠️'}),
            'category': forms.Select(attrs={'class': SELECT}),
            'description': forms.TextInput(attrs={'class': INPUT}),
            'url': forms.URLInput(attrs={'class': INPUT}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Link to documentation (optional)'}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Documentation link'}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name','proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT}),
            'proficiency': forms.Select(attrs={'class': SELECT}),
        }

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform','url','label','custom_label']
        widgets = {
            'platform': forms.Select(attrs={'class': SELECT}),
            'url': forms.URLInput(attrs={'class': INPUT}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Link to documentation (optional)'}),
            'doc_url': forms.URLInput(attrs={'class': INPUT, 'placeholder': 'Documentation link'}),
            'label': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Display name or handle'}),
            'custom_label': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. My Portfolio, Dev Blog...'}),
            'custom_label': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'e.g. My Portfolio, Notion...'}),
        }
