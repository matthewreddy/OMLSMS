

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^suspicious/$', views.suspicious),
    url(r'^suspicious_spec/$', views.suspicious_spec),
)
