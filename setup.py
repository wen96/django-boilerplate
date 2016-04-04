# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

version = __import__('my_project').__version__


setup(
    name='my-project',
    version=version,
    author=u'Rubén Pardo',
    author_email='yosoyruben@gmail.com',
    packages=find_packages(),
    url='https://github.com/wen96/django-boilerplate',
    license='MIT',
    description='Example packaging',
    long_description='Example packaging',
    include_package_data=True
)
