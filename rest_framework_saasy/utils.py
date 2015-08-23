# -*- coding: utf-8 -*-
"""DRF SaaS utilities"""
import importlib
import logging
import traceback

from django.http import Http404

from rest_framework_saasy.routers import SAAS_URL_KW
from rest_framework_saasy.settings import SAAS_MODEL, SAAS_LOOKUP_FIELD

__all__ = ['get_cls']


def get_cls(cls, kwargs, initkwargs):
    """SaaS magic - determine custom viewset class or default"""
    saas_url_kw = kwargs.get(SAAS_URL_KW)
    merchant_cls = None
    if saas_url_kw:
        try:
            saas_client = SAAS_MODEL.objects.get(
                **{SAAS_LOOKUP_FIELD: saas_url_kw}
            )
        except SAAS_MODEL.DoesNotExist:
            raise Exception("Client {0} does not exist".format(saas_url_kw))

        cls_name = cls.__name__
        cls_module = cls.__module__

        client_module = saas_client.saas_client_module(saas_url_kw)
        merchant_cls_module = '{0}.{1}'.format(client_module,
                                               cls.SAAS_MODULE or cls_module)

        try:
            merchant_cls_mod = importlib.import_module(merchant_cls_module)
            merchant_cls = getattr(merchant_cls_mod, cls_name)
        except ImportError:
            pass
        except:
            logger = logging.getLogger(__name__)
            logger.error(traceback.format_exc())
            raise Http404

    _cls = merchant_cls or cls
    self = _cls(**initkwargs)
    setattr(self, SAAS_URL_KW, saas_url_kw)
    return self
