# -*- coding: utf-8 -*-
"""DRF SaaS GenericAPIView"""
from rest_framework import generics

from rest_framework_saasy import views as saas_views

__all__ = ['GenericAPIView']


class GenericAPIView(saas_views.APIView, generics.GenericAPIView):
    pass
