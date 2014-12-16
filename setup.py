#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Nikolay Dolganov"
__email__ = "SirNikolasd@yandex.ru"

from setuptools import setup
from pip.req import parse_requirements
import os

CURRENT_DIR = os.path.dirname(__file__)

install_reqs = parse_requirements(os.path.join(CURRENT_DIR, 'requirements.txt'))
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Django CMS SEO Tools',
    version='1.0',
    description='SEO and Custom tools for the Django CMS',
    author='Nikolay <Werevolff> Dolganov',
    author_email='sirnikolasd@yandex.ru',
    url='https://github.com/werevolff/django_cms_seotools',
    packages=['djangocms_seotools'],
    install_requires=reqs
)