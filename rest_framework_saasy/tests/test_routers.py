"""SaaS router test suite"""
import unittest
from django.conf import settings
settings.REST_FRAMEWORK['SAAS'] = {
    'MODEL': 'test',
    'MODULE': 'test_module'
}

from rest_framework import viewsets
from rest_framework.decorators import link, action
from rest_framework.compat import patterns
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework_saasy import routers
from rest_framework_saasy import viewsets as saas_viewsets

factory = APIRequestFactory()

urlpatterns = patterns('',)


class BasicViewSet(saas_viewsets.ViewSetMixin, viewsets.ViewSet):
    """ViewSet for tests"""
    def list(self, request, *args, **kwargs):
        return Response({'method': 'list'})

    @action()
    def action1(self, request, *args, **kwargs):
        return Response({'method': 'action1'})

    @action()
    def action2(self, request, *args, **kwargs):
        return Response({'method': 'action2'})

    @action(methods=['post', 'delete'])
    def action3(self, request, *args, **kwargs):
        return Response({'method': 'action2'})

    @link()
    def link1(self, request, *args, **kwargs):
        return Response({'method': 'link1'})

    @link()
    def link2(self, request, *args, **kwargs):
        return Response({'method': 'link2'})


class TestSimpleRouter(unittest.TestCase):
    """Placeholder"""
    def setUp(self):
        self.router = routers.SimpleRouter()

    def test_x(self):
        """Placeholder"""
        self.assertEqual(1, 1)
