"""SaaS router test suite"""
import unittest
from rest_framework import viewsets
from rest_framework.decorators import link, action
from rest_framework.compat import patterns
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework_saasy import routers
from rest_framework_saasy import viewsets as saas_viewsets

factory = APIRequestFactory()

urlpatterns = patterns('',)

SAAS_CLIENT_MODEL = 'ClientModel'
SAAS_CLIENT_MODULE = 'test.client.module'


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
        from django.conf import settings
        settings.REST_FRAMEWORK['SAAS'] = {
            'MODEL': SAAS_CLIENT_MODEL,
            'MODULE': SAAS_CLIENT_MODULE
        }

        self.router = routers.SimpleRouter()

    def test_link_and_action_decorator(self):
        routes = self.router.get_routes(BasicViewSet)
        decorator_routes = routes[2:]
        # Make sure all these endpoints exist and none have been clobbered
        for i, endpoint in enumerate(['action1', 'action2', 'action3', 'link1', 'link2']):
            route = decorator_routes[i]
            # check url listing
            self.assertEqual(route.url,
                             '^{{prefix}}/{{lookup}}/{0}{{trailing_slash}}$'.format(endpoint))
            # check method to function mapping
            if endpoint == 'action3':
                methods_map = ['post', 'delete']
            elif endpoint.startswith('action'):
                methods_map = ['post']
            else:
                methods_map = ['get']
            for method in methods_map:
                self.assertEqual(route.mapping[method], endpoint)
