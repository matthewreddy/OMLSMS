

from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^shortcut/(\d+)/(.*)/$', 'django.contrib.contenttypes.views.shortcut'),
)
