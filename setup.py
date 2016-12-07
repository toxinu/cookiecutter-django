#!/usr/bin/env python3
import os

from setuptools import setup

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()


setup(
    name="cookiecutter-django",
    version="0.1.0",
    long_description=long_description,
    description="Cookiecutter template for a Django installable project",
    author=u"Geoffrey Lehée",
    author_email="contact@toxi.nu",
    url="https://github.com/toxinu/cookiecutter-django",
    keywords=["cookiecutter", "template", "package", "django"],
    license='BSD',
    extras_require={
        'dev': ['bumpversion==0.5.3']
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
    ]
)
