"""Setup file for DjangoRestFrameworkSaasy"""
import os
from setuptools import setup, find_packages


setup(
    name='djangorestframework-saasy',
    version='0.1',
    include_package_data=True,
    packages=find_packages(),
    license="MIT",
    author="Juan Gutierrez",
    description="SaaS plugin for the django rest framework",
    url="https://github.com/juannyg/django-rest-framework-saasy",
    test_suite='rest_framework_saasy.runtests.runtests.main',
    install_requires=[
        "Django==1.6.5",
        "djangorestframework==3.11.2",
        "simplejson==3.6.0",
    ]
)
