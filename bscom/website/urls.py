from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('bscom.website.views',
    url(r'^$', TemplateView.as_view(template_name="bsdesign/home.html"), name='home'),
    url(r'contactform/$', 'contact_form', name='bscom_contact_form'),
)
