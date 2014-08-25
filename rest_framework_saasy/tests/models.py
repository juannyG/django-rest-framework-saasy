"""Model for tests cases"""
from django.db import models
from rest_framework_saasy.client import ClientMixin


class ClientModel(models.Model, ClientMixin):
    """Test client model"""
    name = models.CharField(max_length=128)

    @staticmethod
    def saas_lookup_field():
        """DRF-SaaS lookup field definition"""
        return 'name'

    def saas_client_module(self, saas_url_kw):
        return 'rest_framework_saasy.tests.{}'.format(self.name)


class RouterTestModel(models.Model):
    uuid = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
