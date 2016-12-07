#!/usr/bin/env python3
import os

from setuptools import setup
from setuptools import find_packages

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(
        base_dir,
        "src",
        "{{ cookiecutter.module_name }}",
        "__about__.py")) as f:
    exec(f.read(), about)


with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

dependency_links = []

requires = [
    'click==6.6',
    'Django==1.10.4',
]


setup(
    name=about["__title__"],
    version=about["__version__"],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=long_description,
    include_package_data=True,
    description=about["__summary__"],
    author=about["__author__"],
    author_email=about["__email__"],
    url=about["__uri__"],
    install_requires=requires,
    dependency_links=dependency_links,
    license=about["__license__"],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.entrypoint_name }} = {{ cookiecutter.module_name }}.runner:main']
    },
    extras_require={
        'dev': [
            'pytest==3.0.5',
            {% if cookiecutter.use_bumpversion.lower() == 'y' %}'bumpversion==0.5.3',{% endif -%}
            {% if cookiecutter.use_docker_compose.lower() == 'y' %}'docker-compose==1.9.0',{% endif %}
        ],
        {%- if cookiecutter.use_test_helpers.lower() == 'y' %}
        'tests': [
            'flake8==3.2.1',
            'libfaketime==0.4.2',
            'factory-boy==2.7.0',
            'fake-factory==0.7.2'
        ],
        {%- endif %}
    },
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
    ]
)
