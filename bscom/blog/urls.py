"""
Blog URLs
"""
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('bscom.blog.views',
     url(r'^$', 'index', name='blog_index'),
     url(r'^(?P<slug>[\w\-]+)/$', 'single', name='blog_single'),
     url(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'archive', name='blog_archive'),
     url(r'^category/(?P<category_slug>[\w\-]+)/$', 'category', name='blog_category'),
)
