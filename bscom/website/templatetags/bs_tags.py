"""
Template tags used to render/filter various things for the wesbite
"""
import urllib
import json
import markdown2
from datetime import datetime

from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django import template
from django.db.models import Q
from django.utils.timezone import utc

from bscom.blog.models import Entry


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    """
    Markdown tag to replace depricated markdown from contrib
    """
    return mark_safe(markdown2.markdown(force_unicode(value)))


@register.simple_tag
def latest_blog_thumbnail():
    """
    Return the URL of the latest blog entry's thumbnail
    """
    entry = Entry.objects.filter(
        ~Q(thumbnail__exact=''),
        date__lte=datetime.utcnow().replace(tzinfo=utc),
        thumbnail__isnull=False,
        draft=False).latest()

    try:
        return entry.thumbnail_200.url
    except AttributeError:
        return entry.thumbnail.url


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
