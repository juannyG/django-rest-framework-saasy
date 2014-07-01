"""
SaaS Rest Framework settings initialization
"""
from django.conf import settings
from rest_framework.settings import import_from_string


REST_SETTINGS = getattr(settings, 'REST_FRAMEWORK', None)

SAAS_SETTINGS = REST_SETTINGS.get('SAAS')

CLIENT_MODEL = import_from_string(SAAS_SETTINGS.get('CLIENT_MODEL'),
                                  'CLIENT_MODEL'
                                  )
