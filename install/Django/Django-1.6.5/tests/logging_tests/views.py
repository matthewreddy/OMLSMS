

from django.core.exceptions import SuspiciousOperation, DisallowedHost


def suspicious(request):
    raise SuspiciousOperation('dubious')


def suspicious_spec(request):
    raise DisallowedHost('dubious')
