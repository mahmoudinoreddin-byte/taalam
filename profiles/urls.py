from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/personal/', views.edit_personal, name='edit_personal'),
    path('edit/professional/', views.edit_professional, name='edit_professional'),
    path('edit/business/', views.edit_business, name='edit_business'),
    path('edit/experiences/', views.manage_experiences, name='manage_experiences'),
    path('edit/experiences/delete/<int:pk>/', views.delete_experience, name='delete_experience'),
    path('edit/skills/', views.manage_skills, name='manage_skills'),
    path('edit/skills/delete/<int:pk>/', views.delete_skill, name='delete_skill'),
    path('edit/certifications/', views.manage_certifications, name='manage_certifications'),
    path('edit/certifications/delete/<int:pk>/', views.delete_certification, name='delete_certification'),
    path('edit/projects/', views.manage_projects, name='manage_projects'),
    path('edit/projects/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('edit/tools/', views.manage_tools, name='manage_tools'),
    path('edit/tools/delete/<int:pk>/', views.delete_tool, name='delete_tool'),
    path('edit/languages/', views.manage_languages, name='manage_languages'),
    path('edit/languages/delete/<int:pk>/', views.delete_language, name='delete_language'),
    path('edit/links/', views.manage_social_links, name='manage_social_links'),
    path('edit/links/delete/<int:pk>/', views.delete_social_link, name='delete_social_link'),
]
