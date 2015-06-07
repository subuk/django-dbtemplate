# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requires = [
    'django',
    'pyyaml',
]

develop_requires = [
    'mixer',
]

setup(
    name='django-dbtemplate',
    version='0.1',
    packages=find_packages(exclude=['dbtemplate.tests.app']),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'develop': develop_requires,
    },
    zip_safe=False,
    test_suite='tests.main',
)
