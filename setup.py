"""
Setup file for DjangoRestFrameworkSaasy
"""
from setuptools import setup

setup(
#    cmdclass={'test': TestCommand},
    name='DjangoRestFrameworkSaasy',
    version='0.1dev',
    packages=[],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="SaaS plugin for the django rest framework",
    test_suite='rest_framework_saasy.runtests.runtests.main',
    install_requires=[
        "Django>=1.3",
        "djangorestframework>=2.3.14",
        "simplejson>=3.6.0",
    ]
)
