"""ClientMixin test cases"""
from django.test import TestCase

from rest_framework_saasy.client import ClientMixin


class ClientMixinUnitTests(TestCase):
    """ClientMixin unit tests"""
    def setUp(self):
        self.client_mixin = ClientMixin()

    def test_saas_client_module(self):
        with self.assertRaises(NotImplementedError):
            self.client_mixin.saas_client_module('test_saas_url_kw')
