"""Setup file for DjangoRestFrameworkSaasy"""
import os
from setuptools import setup, find_packages


def read(fname):
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ..."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='djangorestframework-saasy',
    version='0.1',
    include_package_data=True,
    packages=find_packages(),
    license="MIT",
    author="Juan Gutierrez",
    description="SaaS plugin for the django rest framework",
    long_description=read('README.md'),
    url="https://github.com/juannyg/django-rest-framework-saasy",
    test_suite='rest_framework_saasy.runtests.runtests.main',
    install_requires=[
        "Django>=1.3",
        "djangorestframework>=2.3.14",
        "simplejson>=3.6.0",
    ]
)
