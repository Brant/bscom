from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist

from noodles.views import json_response
from noodles.forms import ContactForm


def contact_form(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return json_response(request, {"success": True})

        form_html = render_to_string("bsdesign/contact_form.html", {"form": form}, context_instance=RequestContext(request))
        return json_response(request, {"success": False, "form": form_html})

    form_html = render_to_string("bsdesign/contact_form.html", {"form": form}, context_instance=RequestContext(request))

    return json_response(request, {"success": True, "form": form_html})
