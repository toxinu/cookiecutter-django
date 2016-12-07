import os

from .base import *  # noqa

if os.environ.get(
        'DJANGO_SETTINGS_MODULE', '{{ cookiecutter.module_name }}.settings') == '{{ cookiecutter.module_name }}.settings':
    from .local import *  # noqa
