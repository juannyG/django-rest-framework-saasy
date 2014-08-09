"""Model for tests cases"""
from django.db import models
SAAS_CLIENT_URL_PARAM = 'name'


class ClientModel(models.Model):
    """Test client model"""
    name = models.CharField(max_length=128)

    class Meta:
        """SaaS URL parameter defintion"""
        saas_url_param = SAAS_CLIENT_URL_PARAM
        saas_lookup_field = SAAS_CLIENT_URL_PARAM


class RouterTestModel(models.Model):
    uuid = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
