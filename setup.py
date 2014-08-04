#!/usr/bin/env python
from setuptools import setup

from cordova import __version__

setup(
    name="python-cordova",
    version=__version__,
    description="A python interface for Apache Cordova CLI",
    author="Kristoffer Pantic",
    author_email="me@kristofferpantic.com",
    url="http://github.com/talpor/python-cordova",
    packages=['cordova'],
    download_url='https://github.com/talpor/python-cordova/tarball/0.1',
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"],
    install_requires=[
    ],
)
