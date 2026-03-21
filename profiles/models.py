from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()

PROFICIENCY = [(i, str(i)) for i in range(1, 6)]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(unique=True, blank=True)
    # Personal
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    mbti = models.CharField(max_length=10, blank=True)
    interests = models.TextField(blank=True, help_text='Comma separated interests')
    avatar = models.ImageField(upload_to='profiles/avatars/', blank=True, null=True)
    # Status
    is_available = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    # Professional
    current_position = models.CharField(max_length=200, blank=True)
    current_company = models.CharField(max_length=200, blank=True)
    years_experience = models.PositiveIntegerField(null=True, blank=True)
    remote_preference = models.CharField(max_length=20, choices=[('remote','Remote'),('onsite','On-site'),('hybrid','Hybrid')], default='hybrid')
    expected_salary = models.CharField(max_length=100, blank=True)
    # Business
    business_name = models.CharField(max_length=200, blank=True)
    business_role = models.CharField(max_length=200, blank=True)
    business_industry = models.CharField(max_length=200, blank=True)
    business_description = models.TextField(blank=True)
    # Social links
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    website = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    calendly = models.URLField(blank=True)
    # Theme
    theme_color = models.CharField(max_length=7, default='#7c6af7')
    dark_mode = models.BooleanField(default=True)
    # Meta
    profile_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.user.username)
            slug = base
            n = 1
            while Profile.objects.filter(slug=slug).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('public_profile', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.user.username} profile'

    @property
    def interests_list(self):
        return [i.strip() for i in self.interests.split(',') if i.strip()]


class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(choices=[
        (20,'Basic'),(40,'Elementary'),(60,'Intermediate'),(80,'Advanced'),(100,'Native')
    ], default=60)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.role} at {self.company}'


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80)
    category = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [('live','Live'),('wip','In Progress'),('planned','Planned'),('completed','Completed')]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)
    emoji = models.CharField(max_length=5, default='🚀')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=300, blank=True, help_text='Comma separated')
    role = models.CharField(max_length=200, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    looking_for_collaborators = models.BooleanField(default=False)
    doc_url = models.URLField(blank=True, help_text='Link to documentation')
    doc_label = models.CharField(blank=True, max_length=100, help_text='Documentation button label')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Tool(models.Model):
    CATEGORY_CHOICES = [('design','Design'),('dev','Development'),('productivity','Productivity'),('hardware','Hardware'),('other','Other')]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tools')
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=5, default='🛠️')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    doc_url = models.URLField(blank=True, help_text='Documentation link')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin','LinkedIn'),('github','GitHub'),('behance','Behance'),
        ('dribbble','Dribbble'),('twitter','Twitter/X'),('instagram','Instagram'),
        ('youtube','YouTube'),('tiktok','TikTok'),('telegram','Telegram'),
        ('discord','Discord'),('patreon','Patreon'),('other','Other'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    label = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
