from datetime import datetime
from django.db import models
from django.utils.timezone import utc

from taggit.managers import TaggableManager

from noodles.models import TitleDateSlug, DefinedWidthsAssetsFromImagesMixin


class Entry(DefinedWidthsAssetsFromImagesMixin, TitleDateSlug):
    """
    A blog entry

    Inherits title, date, and slug from TitleDateSlug
    Uses taggit taggable manager for tagging
    """
    tags = TaggableManager(blank=True)

    category = models.ForeignKey('Category', null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="blog/img/thumbnails", help_text="Should be a square (e.g. 300x300)")

    content = models.TextField(null=True, blank=True)
    blurb = models.TextField(null=True, blank=True)

    draft = models.BooleanField(default=False, help_text="While in draft status, the entry will never show up on a live site")
    draft_file = models.CharField(max_length=1000, null=True, blank=True)
    date_modified = models.DateTimeField(null=True, blank=True, auto_now=True)

    external_link = models.CharField(max_length=200, null=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        """ permalink """
        return ("blog_single", [str(self.slug)])

    class Meta:
        """ Django Metadata """
        ordering = ["-date"]
        verbose_name_plural = "Entries"
        get_latest_by = "date"

    def get_dimensions(self):
        """ asset widths """
        return [100, 200, 300, 500]


class Category(TitleDateSlug):
    """
    A category for blog entries

    Inherits title, date, and slug from TitleDateSlug
    Date can be ignored
    """
    default_thumbnail = models.ImageField(null=True, blank=True, upload_to="blog/img/thumbnails/default", help_text="150x150px")

    @models.permalink
    def get_absolute_url(self):
        """
        permalink
        """
        return ("blog_category", [str(self.slug)])

    class Meta:
        """ Django Metadata """
        ordering = ["title"]
        verbose_name_plural = "Categories"
