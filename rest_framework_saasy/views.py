# -*- coding: utf-8 -*-
"""DRF SaaS APIView"""
from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView as BaseAPIView

from rest_framework_saasy.utils import get_cls

__all__ = ['APIView', 'GenericAPIView']


class APIView(BaseAPIView):
    @classonlymethod
    def as_view(cls, **initkwargs):
        """While this call returns the view function, it needs to be
        reworked due to the nature of this plugin: dynamic class
        initialization.

        @see rest_framework.views.APIView
        """
        super(BaseAPIView, cls).as_view(**initkwargs)
        def view(request, *args, **kwargs):
            """Slightly modified Django wrapped view.

            @see django.views.generic.base.View
            """
            self = get_cls(cls, kwargs, initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.dispatch(request, *args, **kwargs)

        view.cls = cls
        return csrf_exempt(view)


class GenericAPIView(APIView, generics.GenericAPIView):
    pass
