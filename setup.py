"""
Setup file for DjangoRestFrameworkSaasy
"""
from distutils.core import setup
from distutils.core import Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from os.path import splitext, basename, join as pjoin
import os


class TestCommand(Command):
    """http://da44en.wordpress.com/2002/11/22/using-distutils/"""
    user_options = []

    def initialize_options(self):
        self.root_prefix = 'rest_framework_saasy'
        self._dir = '{}/{}'.format(os.getcwd(), self.root_prefix)

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/, and runs them.
        '''
        testfiles = []
        for t in glob(pjoin(self._dir, 'tests', '*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    [self.root_prefix,
                     'tests',
                     splitext(basename(t))[0]
                     ])
                )

        tests = TestLoader().loadTestsFromNames(testfiles)
        t_runner = TextTestRunner(verbosity=1)
        t_runner.run(tests)

setup(
    cmdclass={'test': TestCommand},
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
