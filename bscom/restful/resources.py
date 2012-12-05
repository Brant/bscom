"""
API Resources for the Brant Steen website
"""

from datetime import datetime

from tastypie.resources import ModelResource

from bscom.blog.models import Entry
from bscom.folio.models import Piece


class BlogEntryNoContentResource(ModelResource):
    """
    Rest API resource for blog entries
    """
    class Meta:
        queryset = Entry.objects.filter(date__lte=datetime.now()).order_by("-date")
        allowed_methods = ['get']
        excludes = ["content"]
        
class PortfolioImageResource(ModelResource):
    """
    """
    class Meta:
        queryset = Piece.objects.filter(date__lte=datetime.now()).order_by("-date")
        allowed_methods = ['get']
        #excludes = ["content"]
        fields = ["thumbnail"]