from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def youtube_id(url):
    """Extract YouTube video ID from any YouTube URL format."""
    if not url:
        return ''
    parsed = urlparse(url)
    if 'youtube.com' in parsed.netloc:
        qs = parse_qs(parsed.query)
        return qs.get('v', [''])[0]
    if 'youtu.be' in parsed.netloc:
        return parsed.path.lstrip('/')
    return ''

@register.filter
def is_youtube(url):
    return 'youtube.com' in url or 'youtu.be' in url

@register.filter
def is_mp4(url):
    return url.lower().endswith(('.mp4', '.webm', '.ogg', '.mov'))
