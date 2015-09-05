# -*- coding: utf-8 -*-
"""DRF SaaS Generics"""
from rest_framework import generics

from rest_framework_saasy.views import APIView

__all__ = ['GenericAPIView']


class GenericAPIView(APIView, generics.GenericAPIView):
    pass
