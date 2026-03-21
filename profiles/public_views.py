from django.shortcuts import render, get_object_or_404
from .models import Profile

def public_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug, is_public=True)
    # Increment view count (skip owner's own views)
    if not request.user.is_authenticated or request.user != profile.user:
        Profile.objects.filter(pk=profile.pk).update(profile_views=profile.profile_views + 1)
        profile.refresh_from_db()

    context = {
        'profile': profile,
        'experiences': profile.experiences.all(),
        'skills': profile.skills.all(),
        'certifications': profile.certifications.all(),
        'projects': profile.projects.all(),
        'tools': profile.tools.all(),
        'languages': profile.languages.all(),
        'social_links': profile.social_links.all(),
        'is_owner': request.user.is_authenticated and request.user == profile.user,
    }
    return render(request, 'profiles/public_profile.html', context)
