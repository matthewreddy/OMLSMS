

from django.conf.urls import patterns, include

from . import  widgetadmin


urlpatterns = patterns('',
    (r'^', include(widgetadmin.site.urls)),
)
