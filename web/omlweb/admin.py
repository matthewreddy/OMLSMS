"""Register certain users with administrative permissions (defined by Django)."""

from django.contrib import admin
from omlweb.models import UserProfile, Dentist

admin.site.register(UserProfile)
admin.site.register(Dentist)
