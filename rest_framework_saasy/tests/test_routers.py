"""SaaS router test suite"""
SAAS_CLIENT_MODEL = 'rest_framework_saasy.tests.test_routers.ClientModel'
SAAS_CLIENT_MODULE = 'rest_framework_saasy.tests.client'
SAAS_CLIENT_URL_PARAM = 'name'

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('saas_url_param',)

from django.conf import settings
from django.db import models
settings.REST_FRAMEWORK['SAAS'] = {
    'MODEL': SAAS_CLIENT_MODEL,
    'MODULE': SAAS_CLIENT_MODULE
    }


class ClientModel(models.Model):
    """Test client model"""
    name = models.CharField(max_length=128)

    class Meta:
        """SaaS URL parameter defintion"""
        saas_url_param = SAAS_CLIENT_URL_PARAM

import unittest
from rest_framework import viewsets
from rest_framework.decorators import link, action
from rest_framework.compat import patterns
from rest_framework.response import Response
# from rest_framework.test import APIRequestFactory
from rest_framework_saasy import routers
from rest_framework_saasy import viewsets as saas_viewsets

# factory = APIRequestFactory()

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

    def test_link_and_action_decorator(self):
        """Test client link & action decorator routing"""
        endpoints = ['action1', 'action2', 'action3', 'link1', 'link2']
        routes = self.router.get_routes(BasicViewSet)
        decorator_routes = routes[9:]

        # Make sure all these endpoints exist and none have been clobbered
        for i, endpoint in enumerate(endpoints):
            client_route = decorator_routes[i]
            # check url listing
            self.assertEqual(client_route.url,
                             '^(?P<{}>\\w+)/'.format(SAAS_CLIENT_URL_PARAM) +
                             '{prefix}/' +
                             '{lookup}/' +
                             '{}{{trailing_slash}}$'.format(endpoint)
                             )
            # check method to function mapping
            if endpoint == 'action3':
                methods_map = ['post', 'delete']
            elif endpoint.startswith('action'):
                methods_map = ['post']
            else:
                methods_map = ['get']
            for method in methods_map:
                self.assertEqual(client_route.mapping[method], endpoint)
