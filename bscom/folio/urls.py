"""
Portfolio URLs
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('bscom.folio.views',
     url(r'^$', 'index', name='folio_index'),
)

