import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def pytest_configure(config):
    import warnings
    warnings.filterwarnings('error', '', Warning, r'^(?!(|{{ cookiecutter.module_name }}))')  # noqa
