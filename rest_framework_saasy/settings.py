"""
SaaS Rest Framework settings initialization
"""
from django.conf import settings
from rest_framework.settings import import_from_string


REST_SETTINGS = getattr(settings, 'REST_FRAMEWORK', {})

SAAS_SETTINGS = REST_SETTINGS.get('SAAS', {})

SAAS_MODEL = import_from_string(SAAS_SETTINGS.get('MODEL'),
                                'MODEL'
                                ) if SAAS_SETTINGS.get('MODEL') else None
