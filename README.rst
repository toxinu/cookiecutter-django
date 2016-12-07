Cookiecutter-django
===================

This `cookiecutter <https://github.com/audreyr/cookiecutter>`_ template is designed for a `Django`_ project which will be pip installable.

The idea is to have a very non-intrusive dependencies template.


**Features**:

 * Publishable on `PyPI <https://pypi.org/>`_ as a `Django`_ project (:code:`MANIFEST.in` included)
 * A command line interface is provided (inspired by `Sentry <https://github.com/getsentry/sentry>`_)
 * Manage `Django`_ settings with a sourced :code:`local.py` file
 * Provide a simple :code:`Makefile` with linting and tests commands
 * `Pytest`_ integration with `Django`_
 * Optionnal integrations like: `bumpversion`_, `docker-compose`_

`Pytest`_ integration is not very intrusive for people who doesn't want it.
You'll just need to remove it from :code:`setup.py` and remove `conftest.py` file.
`Django`_ internal tests runner will run perfectly.

Other integrations like `docker-compose`_ and `bumpversion`_ can be better, feedback and contributions are welcome.

There is a little helper with :code:`use_test_helpers` option which only add: `flake8`_, `libfaketime`_, `factory-boy`_ and `fake-factory`_ to :code:`dev` :code:`extra_requires` group.

.. _Django: https://docs.djangoproject.com
.. _Pytest: http://docs.pytest.org/en/latest/
.. _docker-compose: https://docs.docker.com/compose/
.. _bumpversion: https://github.com/peritus/bumpversion
.. _flake8: http://flake8.pycqa.org/en/latest/
.. _libfaketime: https://github.com/simon-weber/python-libfaketime
.. _factory-boy: https://factoryboy.readthedocs.io/en/latest/
.. _fake-factory: https://faker.readthedocs.io/en/latest/
