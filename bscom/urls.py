"""
Main URL configuraitons for bscom
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from noodles.urls import favicon_patterns

from tastypie.api import Api

from bscom.blog.feed import AllFeed
from bscom.restful.resources import BlogEntryNoContentResource, PortfolioImageResource


admin.autodiscover()


v1_api = Api(api_name="v1")
v1_api.register(BlogEntryNoContentResource())
v1_api.register(PortfolioImageResource())


urlpatterns = patterns('',
    (r'^feed/$', AllFeed()),
    url(r'^$', TemplateView.as_view(template_name="bsdesign/home.html"), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="bsdesign/about.html"), name="about"),
    url(r'^podcast/$', TemplateView.as_view(template_name="bsdesign/wtfawd.html"), name="podcast"),

    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include("bscom.blog.urls")),
    (r'^portfolio/', include("bscom.folio.urls")),

    (r'^', include("noodles.urls")),

    (r'^api/', include(v1_api.urls)),

)


if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += favicon_patterns
