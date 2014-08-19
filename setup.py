"""Setup file for DjangoRestFrameworkSaasy"""
from setuptools import setup, find_packages
setup(
    name='DjangoRestFrameworkSaasy',
    version='0.1',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    author="Juan Gutierrez",
    description="SaaS plugin for the django rest framework",
    url="https://github.com/juannyg/django-rest-framework-saasy",
    test_suite='rest_framework_saasy.runtests.runtests.main',
    install_requires=[
        "Django>=1.3",
        "djangorestframework>=2.3.14",
        "simplejson>=3.6.0",
    ]
)
