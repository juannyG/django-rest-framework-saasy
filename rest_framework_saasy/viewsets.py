import importlib
import logging
import traceback
from functools import update_wrapper

from django.http import Http404
from django.utils.decorators import classonlymethod
from rest_framework import viewsets

from rest_framework_saasy.settings import SAAS_MODEL
from rest_framework_saasy.routers import SAAS_URL_KW

logger = logging.getLogger(__name__)

__all__ = ['ViewSetMixin']


class ViewSetMixin(viewsets.ViewSetMixin):
    """SaaS extension of rest_framework ViewSetMixin"""
    SAAS_MODULE = None

    @classonlymethod
    def get_merchant_cls(cls, saas_url_kw):
        """SaaS magic - determine custom viewset class or default"""
        merchant_cls = None
        if saas_url_kw:
            try:
                saas_client = SAAS_MODEL.objects.get(
                    **{SAAS_MODEL.saas_lookup_field: saas_url_kw}
                )
            except SAAS_MODEL.DoesNotExist:
                raise Exception("Client {0} does not exist".format(saas_url_kw))

            cls_name = cls.__name__
            cls_module = cls.__module__

            client_module = saas_client.saas_client_module(saas_url_kw)
            merchant_cls_module = '{0}.{1}'.format(client_module,
                                                   cls.SAAS_MODULE or cls_module)
            print merchant_cls_module
            try:
                merchant_cls_mod = importlib.import_module(merchant_cls_module)
                merchant_cls = getattr(merchant_cls_mod, cls_name)
            except ImportError:
                pass
            except:
                logger.error(traceback.format_exc())
                raise Http404
        return merchant_cls

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
            saas_url_kw = kwargs.get(SAAS_URL_KW)
            _cls = cls.get_merchant_cls(saas_url_kw) or cls
            self = _cls(**initkwargs)
            setattr(self, SAAS_URL_KW, saas_url_kw)

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
        return view
