__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "{{ cookiecutter.project_name|replace('_', '-') }}"
__summary__ = "{{ cookiecutter.project_short_description }}"  # noqa
__uri__ = "{{ cookiecutter.project_url }}"

__version__ = "{{ cookiecutter.version }}"

__author__ = u"{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"

__license__ = "{{ cookiecutter.license }}"
__copyright__ = "Copyright {{ cookiecutter.year }} %s" % __author__
