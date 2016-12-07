lint:
	@echo "--> Linting python"
	flake8
	@echo ""

test-python:
	@echo "--> Running Python tests"
	py.test tests/ || exit 1
	@echo ""

test: lint test-python

locale:
	cd src/{{ cookiecutter.module_name }} && {{ cookiecutter.entrypoint_name }} django makemessages -i static -l en
	cd src/{{ cookiecutter.module_name }} && {{ cookiecutter.entrypoint_name }} django compilemessages

.PHONY: lint test test-python
