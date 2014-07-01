"""
Setup file for DjangoRestFrameworkSaasy
"""
from distutils.core import setup

setup(
    name='DjangoRestFrameworkSaasy',
    version='0.1dev',
    packages=[],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="SaaS plugin for the django rest framework",
    install_requires=[
        "Django>=1.3",
        "djangorestframework>=2.3.14",
    ]
)
