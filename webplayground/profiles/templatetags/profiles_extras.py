from django import template
from registration.models import Profile

register = template.Library()

@register.simple_tag
def get_profile_list():
    profiles = Profile.objects.all()
    return profiles