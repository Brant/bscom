"""
Portfolio Views
"""
from django.shortcuts import render_to_response
from django.template import RequestContext

from bscom.folio.models import Piece


def index(request):
    """
    Portfolio listing
    """
    
    response_data = {"pieces": Piece.objects.all() }
    return render_to_response("folio/index.html", response_data, RequestContext(request))