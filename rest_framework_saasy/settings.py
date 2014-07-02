"""
SaaS Rest Framework settings initialization
"""
from django.conf import settings
from rest_framework.settings import import_from_string


REST_SETTINGS = getattr(settings, 'REST_FRAMEWORK', {})

SAAS_SETTINGS = REST_SETTINGS.get('SAAS')

CLIENT_MODEL = import_from_string(SAAS_SETTINGS.get('MODEL'),
                                  'MODEL'
                                  )

MODULE_PREFIX = SAAS_SETTINGS.get('MODULE_PREFIX')
CLIENT_MODULE_PATH = SAAS_SETTINGS.get('MODULE')
