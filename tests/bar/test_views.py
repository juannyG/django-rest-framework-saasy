"""Test client extension"""
from rest_framework.response import Response

from tests.test_views import BasicView as BaseAPIView


class BasicView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        return Response('client_get')
