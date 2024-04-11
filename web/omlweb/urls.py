from django.urls import include, re_path
from omlweb.views import home, summary, billing, results, billPDF, \
                            resultsPDF, invalidSterilizer

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout

urlpatterns = [
    re_path(r'^$', home),
    
    re_path(r'^login/$', login, {'template_name': 'login.html'}),
    re_path(r'^logout/$', logout, {'next_page': '/login'}),
    
    re_path(r'^summary/$', summary),
    re_path(r'^billing/$', billing),
    re_path(r'^results/$', results),

    re_path(r'^billing/print_bill/(\d{3,5})$', billPDF),
    re_path(r'^results/print_results/(\d{3,5})$', resultsPDF),
    
    re_path(r'^invalid/sterilizer_id/(\d{3,5})$', invalidSterilizer),

    # Uncomment the admin/doc line below to enable admin documentation:
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    re_path(r'^admin/', include(admin.site.urls)),
]