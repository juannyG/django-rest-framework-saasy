"""Model for tests cases"""
from django.db import models
from rest_framework_saasy.client import ClientMixin


class ClientModel(models.Model, ClientMixin):
    """Test client model"""
    name = models.CharField(max_length=128)

    def saas_client_module(self, saas_url_kw):
        return 'tests.{0}'.format(self.name)


class TestModel(models.Model):
    uuid = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
