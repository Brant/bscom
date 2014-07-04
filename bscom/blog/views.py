"""
Blog views
"""
from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from bscom.blog.models import Entry, Category
from bscom.blog.tasks import import_drafts_from_dropbox

from noodles.util import make_paginator
from noodles.views import json_response


def import_drafts(request):
    challenge = request.GET.get("challenge", None)

    if challenge:
        return HttpResponse(challenge)

    import_drafts_from_dropbox()
    return json_response(request, {"success": True})


def single(request, slug):
    """
    A blog post
    """
    try:
        entry = Entry.objects.prefetch_related('category').get(slug=slug, draft=False)
    except ObjectDoesNotExist:
        raise Http404

    response_data = {
        "entry": entry
    }

    return render_to_response("blog/single.html", response_data, RequestContext(request))


def category(request, category_slug):
    """
    All entries belonging to a given category
    """
    category = get_object_or_404(Category, slug=category_slug)
    entries = Entry.objects.filter(date__lte=datetime.now(), category=category, draft=False)
    entries = make_paginator(request, entries)

    response_data = {"entries": entries, "category": category}

    return render_to_response("blog/category.html", response_data, context_instance=RequestContext(request))


def archive(request, month, year):
    """
    A month of a year of entries

    Not paginated
    """
    entries = Entry.objects.filter(date__month=month, date__year=year, date__lte=datetime.now(), draft=False)

    try:
        archive = entries.dates('date', 'month')[0]
    except IndexError:
        return HttpResponseRedirect(reverse("blog_index"))


    response_data = {"entries": entries, "archive": archive}

    return render_to_response("blog/archive.html", response_data, context_instance=RequestContext(request))


def index(request):
    """
    Blog Index

    Must be published, according to its date
    """

    entries = Entry.objects.prefetch_related('category').filter(date__lte=datetime.now(), draft=False)
    entries = make_paginator(request, entries)

    response_data = {
        "entries": entries
    }

    return render_to_response("blog/index.html", response_data, RequestContext(request))
