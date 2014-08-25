"""SaaS router test suite"""
SAAS_CLIENT_MODEL = 'rest_framework_saasy.tests.models.ClientModel'

from django.conf import settings
settings.REST_FRAMEWORK['SAAS'] = {
    'MODEL': SAAS_CLIENT_MODEL,
    }


import simplejson
from django.test import TestCase
from rest_framework import serializers, viewsets
from rest_framework.decorators import link, action
from rest_framework.compat import include, patterns, url
from rest_framework.response import Response
# from rest_framework.test import APIRequestFactory
from rest_framework_saasy import routers
from mock import patch
from rest_framework_saasy import viewsets as saas_viewsets
from .models import ClientModel, RouterTestModel

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


class TestSimpleRouter(TestCase):
    """SaaSy SimpleRouter test suite"""
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
                             '^(?P<{}>.*)/'.format(routers.SAAS_URL_KW) +
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


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouterTestModel
        fields = ('url', 'uuid', 'text')


class NoteViewSet(saas_viewsets.ViewSetMixin, viewsets.ModelViewSet):
    queryset = RouterTestModel.objects.all()
    serializer_class = NoteSerializer

    @staticmethod
    def saas_module(*args, **kwargs):
        return 'test_routers'


class TestSaaSRouting(TestCase):
    """ViewSet test suite"""
    urls = 'rest_framework_saasy.tests.test_routers'

    def setUp(self):
        ClientModel.objects.create(name='foo_bar-123')
        ClientModel.objects.create(name='bar')
        RouterTestModel.objects.create(uuid='123', text='foo bar')
        self.register()

    def register(self):
        self.router = routers.SimpleRouter()
        self.router.register(r'notes', NoteViewSet)

        from rest_framework_saasy.tests import test_routers
        urls = getattr(test_routers, 'urlpatterns')
        urls += patterns('',
                         url(r'^', include(self.router.urls)),
                         )

    def test_core_fallback(self):
        expected_response = {
            "url": "http://testserver/notes/1/",
            "uuid": "123",
            "text": "foo bar"
            }

        core_response = self.client.get('/foo_bar-123/notes/1/')
        self.assertEqual(simplejson.loads(core_response.content),
                         expected_response
                         )

        core_response = self.client.get('/bar/notes/1/')
        self.assertEqual(simplejson.loads(core_response.content),
                         expected_response
                         )

    def test_client_override(self):
        custom_response = self.client.get('/foo_bar-123/notes/')
        self.assertEqual(simplejson.loads(custom_response.content), {
            "method": "list",
            "custom": True
            }
        )

    def test_nonexistent_client(self):
        self.assertRaises(Exception,
                          self.client.get,
                          '/baz/notes/'
                          )

    def test_404(self):
        response = self.client.get('/foo_bar-123/baz/')
        self.assertEqual(response.status_code, 404)

    @patch('rest_framework_saasy.viewsets.importlib.import_module')
    def test_merchant_cls_exception(self, import_module_mock):
        """If the merchant class is throwing an exception, log it, and return 404"""
        import_module_mock.side_effect = Exception('test!')
        response = self.client.get('/foo_bar-123/notes/')
        self.assertIn('Not Found', response.content)

    # Can't do this yet...
    # def test_client_link(self):
    #     client_link = self.client.get('/foo_bar-123/notes/1/test_link/')
    #     print client_link
