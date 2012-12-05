from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from bscom.blog.feed import AllFeed

from tastypie.api import Api
from bscom.restful.resources import BlogEntryNoContentResource, PortfolioImageResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(BlogEntryNoContentResource())
v1_api.register(PortfolioImageResource())

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'bsdesign.views.home', name='home'),
    (r'^feed/$', AllFeed()),
    url(r'^$', TemplateView.as_view(template_name="bsdesign/home.html"), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="bsdesign/about.html"), name="about"),
    url(r'^podcast/$', TemplateView.as_view(template_name="bsdesign/wtfawd.html"), name="podcast"),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include("bscom.blog.urls")),
    (r'^portfolio/', include("bscom.folio.urls")),
     
    (r'^', include("noodles.urls")),
     
    (r'^api/', include(v1_api.urls)),
    
    (r'^favicon\.png$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL + 'img/favicon.png'}),
    (r'^apple-touch-icon\.png$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL + 'img/apple-touch-icon.png'}),
)



if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^admin-media/(.*)', 'django.views.static.serve', {'document_root' : '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/Django-1.3.1-py2.7.egg/django/contrib/admin/media/', 'show_indexes' : False})
    )
