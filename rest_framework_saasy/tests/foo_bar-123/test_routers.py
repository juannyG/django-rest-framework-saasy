"""Test client extension"""
# from rest_framework.decorators import link, action
from rest_framework.response import Response
from rest_framework_saasy.tests.test_routers import NoteViewSet as CoreNoteViewSet


class NoteViewSet(CoreNoteViewSet):
    """Client override"""
    def list(self, request, *args, **kwargs):
        return Response({'method': 'list', 'custom': True})

#    @link()
#    def test_link(self, request, *args, **kwargs):
#        return Response({'testing': 'link'})
#
#    @action()
#    def test_action(self, request, *args, **kwargs):
#        return Response({'testing': 'action'})
