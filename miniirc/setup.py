#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PIRCD',
    version='0.0.0',
    description='Python IRC Daemon',
    long_description=read('README.md'),
    author='Joel Kleier',
    author_email='joel@kleier.us',
    license='MIT',
    url='',
    packages=[
        'pircd',
        'tests',
    ],
    # for a list of possible classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
    ],
    install_requires=[
        'tornado',
    ],
)
