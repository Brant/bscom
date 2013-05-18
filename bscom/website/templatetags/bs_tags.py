"""
Template tags used to render/filter various things for the wesbite
"""
import urllib
import json
from datetime import datetime, time

from django import template
from django.db.models import Q

from bscom.blog.models import Entry


register = template.Library()


@register.simple_tag
def latest_blog_thumbnail():
    """
    Return the URL of the latest blog entry's thumbnail
    """
    return Entry.objects.filter(~Q(thumbnail__exact=''), date__lte=datetime.now(), thumbnail__isnull=False).latest().thumbnail.url

@register.inclusion_tag("bsdesign/tags/wtfawd_latest.html")
def wtfawd_latest_episodes():
    """
    """
    url = "http://www.wtfawd.com/api/v1/sode/?format=json&limit=3"
    file_like = urllib.urlopen(url)
    data = file_like.read()
    data = json.loads(data)
    
    for ep in data["objects"]:
        ep["date"] = datetime.strptime(ep["date"], "%Y-%m-%dT%H:%M:%S")
    
    return {"episodes": data["objects"]}