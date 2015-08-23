# -*- coding: utf-8 -*-
"""SaaS View test suite"""
from django.test import TestCase

from rest_framework_saasy import views as saas_views


class BasicView(saas_views.APIView):
    """View for tests"""
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class TestSaaSView(TestCase):
    pass
