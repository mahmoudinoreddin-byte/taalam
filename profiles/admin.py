from django.contrib import admin
from .models import Profile, WorkExperience, Skill, Certification, Project, Tool, Language, SocialLink

class ExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'current_position', 'is_available', 'is_public', 'profile_views', 'created_at']
    list_filter = ['is_available', 'is_public', 'remote_preference']
    search_fields = ['user__username', 'user__email', 'current_position']
    readonly_fields = ['slug', 'profile_views', 'created_at', 'updated_at']
    inlines = [ExperienceInline, SkillInline, ProjectInline]

admin.register(WorkExperience)(admin.ModelAdmin)
admin.register(Skill)(admin.ModelAdmin)
admin.register(Certification)(admin.ModelAdmin)
admin.register(Project)(admin.ModelAdmin)
admin.register(Tool)(admin.ModelAdmin)
admin.register(Language)(admin.ModelAdmin)
admin.register(SocialLink)(admin.ModelAdmin)
