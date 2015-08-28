# -*- coding: utf-8 -*-
"""DRF SaaS ViewSetMixin"""
from functools import update_wrapper

from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from rest_framework_saasy.utils import get_cls

__all__ = ['ViewSetMixin', 'ViewSet', 'GenericViewSet']


class ViewSetMixin(viewsets.ViewSetMixin):
    """SaaS extension of rest_framework ViewSetMixin"""
    SAAS_MODULE = None

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        """While this call returns the view function, it needs to be
        reworked due to the nature of this plugin: dynamic class
        initialization.
        """
        super(ViewSetMixin, cls).as_view(actions, **initkwargs)

        def view(request, *args, **kwargs):
            """Slightly modified rest_framework wrapped view.

            @see rest_framework.viewsets.ViewSetMixin
            """
            self = get_cls(cls, kwargs, initkwargs)

            # We also store the mapping of request methods to actions,
            # so that we can later set the action attribute.
            # eg. `self.action = 'list'` on an incoming GET request.
            self.action_map = actions

            # Bind methods to actions
            # This is the bit that's different to a standard view
            for method, action in actions.items():
                handler = getattr(self, action)
                setattr(self, method, handler)

            # Patch this in as it's otherwise only present from 1.5 onwards
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get

            # And continue as usual
            return self.dispatch(request, *args, **kwargs)

        # take name and docstring from class
        update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=())

        # We need to set these on the view function, so that breadcrumb
        # generation can pick out these bits of information from a
        # resolved URL.
        view.cls = cls
        view.suffix = initkwargs.get('suffix', None)
        return csrf_exempt(view)


class ViewSet(ViewSetMixin, viewsets.ViewSet):
    pass

class GenericViewSet(ViewSetMixin, viewsets.GenericViewSet):
    pass
