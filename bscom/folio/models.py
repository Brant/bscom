"""
Portfolio Models
"""
from django.db import models

from noodles.models import TitleDateSlug

from taggit.managers import TaggableManager


class Piece(TitleDateSlug):
    """
    A portfolio piece
    
    title/date/slug
    
    date is approximate date that item was "added to folio" 
    """
    thumbnail = models.ImageField(upload_to="folio/img/thumbnails", help_text="250x150 px")
    blurb = models.TextField()
    link = models.URLField(null=True, blank=True, help_text="Link to client site")
    confidential = models.BooleanField(default=False)
    
    tags = TaggableManager()
    
    class Meta:
        """ Django Metadata """
        ordering = ["-date"]
        verbose_name = "Portfolio Piece"
        verbose_name_plural = "Porfolio Pieces"
        get_latest_by = "date"
