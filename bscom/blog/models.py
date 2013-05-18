from django.db import models

from taggit.managers import TaggableManager

from noodles.models import TitleDateSlug


class Entry(TitleDateSlug):
    """
    A blog entry
    
    Inherits title, date, and slug from TitleDateSlug
    Uses taggit taggable manager for tagging
    """
    tags = TaggableManager(blank=True)
    
    category = models.ForeignKey('Category')
    thumbnail = models.ImageField(null=True, blank=True, upload_to="blog/img/thumbnails", help_text="150x150 px")
    
    content = models.TextField()
    blurb = models.TextField()
    
    @models.permalink
    def get_absolute_url(self):
        """
        permalink
        """
        return ("blog_single", [str(self.slug)])
    
    class Meta:
        """ Django Metadata """
        ordering = ["-date"]
        verbose_name_plural = "Entries"
        get_latest_by = "date"
    

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
        
        