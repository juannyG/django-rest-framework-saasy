# -*- coding: utf-8 -*-
"""SaaS View test suite"""
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework.response import Response

from rest_framework_saasy import views as saas_views
from rest_framework_saasy import routers
from .models import ClientModel


class BasicView(saas_views.APIView):
    """View for tests"""
    SAAS_MODULE = 'test_views'
    get_response = 'get'
    post_response = 'post'

    def get(self, request, *args, **kwargs):
        return Response(self.get_response)

    def post(self, request, *args, **kwargs):
        return Response(self.post_response)


class TestSaaSView(TestCase):
    """SaaS implementation of APIView tests"""
    def setUp(self):
        self.factory = RequestFactory()
        self.view = BasicView.as_view()
        ClientModel.objects.create(name='foo_bar-123')
        ClientModel.objects.create(name='bar')

    def test_core_get(self):
        request = self.factory.get('/test')
        response = self.view(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(BasicView.get_response, response.data)

        request = self.factory.get('/foo_bar-123/test')
        response = self.view(request, **{routers.SAAS_URL_KW: 'foo_bar-123'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(BasicView.get_response, response.data)

    def test_core_post(self):
        request = self.factory.post('/test')
        response = self.view(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(BasicView.post_response, response.data)

        request = self.factory.post('/foo_bar-123/test')
        response = self.view(request, **{routers.SAAS_URL_KW: 'foo_bar-123'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(BasicView.post_response, response.data)

    def test_client_extension(self):
        request = self.factory.get('/bar/test')
        response = self.view(request, **{routers.SAAS_URL_KW: 'bar'})
        self.assertEqual(200, response.status_code)
        self.assertEqual('client_get', response.data)

        # But we didn't override the post, so...
        request = self.factory.post('/bar/test')
        response = self.view(request, **{routers.SAAS_URL_KW: 'bar'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(BasicView.post_response, response.data)
