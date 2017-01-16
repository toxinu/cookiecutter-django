DJANGO_SETTINGS_MODULE ?= {{ cookiecutter.module_name }}.settings

default:
	@echo "Must call a specific subcommand"
	@exit 1

lint:
	@echo "--> Linting python"
	flake8
	@echo ""

test-python:
	@echo "--> Running Python tests"
	sh tests/runtest.sh
	@echo ""

coverage:
	@echo "--> Running Python tests"
	sh tests/runtest.sh --cov-report html --cov-report term:skip-covered --cov={{ cookiecutter.module_name }}
	@echo

test: lint test-python

locale:
	cd src/{{ cookiecutter.module_name }} && {{ cookiecutter.entrypoint_name }} django makemessages -i static -l en
	cd src/{{ cookiecutter.module_name }} && {{ cookiecutter.entrypoint_name }} django compilemessages

.PHONY: lint test test-python coverage

{%- if cookiecutter.use_docker_compose -%}
reset_redis:
	@echo "--> Dropping cache..."
	docker-compose exec redis redis-cli 'flushall'

reset_mq:
	@echo "--> Stopping broker..."
	docker-compose exec rabbitmq rabbitmqctl stop_app
	@echo "--> Reseting broker..."
	docker-compose exec rabbitmq rabbitmqctl reset
	@echo "--> Starting broker..."
	docker-compose exec rabbitmq rabbitmqctl start_app

reset_db:
	@echo "--> Dropping database..."
	docker-compose exec postgres dropdb -U {{ cookiecutter.module_name|lower }} {{ cookiecutter.module_name|lower }}
	@echo "--> Creating database..."
	docker-compose exec postgres createdb -U {{ cookiecutter.module_name|lower }} {{ cookiecutter.module_name|lower }}

load_data:
	@echo "--> Migrate..."
	DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) django-admin migrate
	@echo "--> Loading initial data..."
	DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS_MODULE) django-admin loaddata initial

reset_app: reset_redis reset_mq reset_db load_data

.PHONY: reset_mq reset_db load_data reset_app
{%- endif -%}
