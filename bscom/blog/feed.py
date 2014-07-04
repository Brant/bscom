"""
RSS Feed for blog entries
"""
from datetime import datetime

from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from django.contrib.sites.models import Site
from bscom.website.templatetags.bs_tags import markdown

from bscom.blog.models import Entry


class ExtendedRSSFeed(feedgenerator.Rss201rev2Feed):
    """
    Create a type of RSS feed that has content:encoded elements.
    """
    def root_attributes(self):
        attrs = super(ExtendedRSSFeed, self).root_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs

    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u'content:encoded', item['content_encoded'])


class AllFeed(Feed):
    """
    RSS Feed Declaration, based on Extended Feed
    """
    feed_type = ExtendedRSSFeed

    title = "Brant Steen Web Design"
    description = "Blog entries from Brant Steen, a web designer, developer, consultant, and all around geek"
    link = "http://%s/" % (Site.objects.get_current().domain)

    def items(self):
        """
        All entries that are published before datetime.now
        """
        return Entry.objects.filter(date__lte=datetime.now(), draft=False).order_by("-date")

    def item_link(self, item):
        """
        Figure out where the link should go
            might goto an external source
        """
        if item.external_link:
            return item.external_link
        return item.get_absolute_url()

    def item_title(self, item):
        """
        Title of each item in feed
        """
        return item.title

    def item_description(self, item):
        """
        Short, base-RSS supported description
        """
        return markdown(item.blurb)

    def item_pubdate(self, item):
        """
        Publish date
        """
        return item.date

    def item_extra_kwargs(self, item):
        return {'content_encoded': self.item_content_encoded(item)}

    def item_content_encoded(self, item):
        """
        Full entry content
        """
        return markdown(item.content)
