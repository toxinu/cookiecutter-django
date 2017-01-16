#!/bin/bash
{%- if cookiecutter.use_test_helpers.lower() == 'y' -%}
eval $(python-libfaketime)
py.test . $* || exit 1
{%- else -%}
{{ cookiecutter.entrypoint_name }} test $* || exit 1
{%- endif -%}
