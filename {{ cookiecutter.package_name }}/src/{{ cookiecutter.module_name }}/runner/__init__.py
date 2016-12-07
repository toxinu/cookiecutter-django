import os

import click
from django.utils.module_loading import import_string

import {{ cookiecutter.module_name }}


@click.group()
@click.option(
    '--config',
    default='',
    envvar='DJANGO_SETTINGS_MODULE',
    help='Path to settings module.',
    metavar='PATH')
@click.version_option(version={{ cookiecutter.module_name }}.__version__)
@click.pass_context
def cli(ctx, config):
    """{{ cookiecutter.project_short_description }}

    Default settings module is `{{ cookiecutter.module_name }}.settings` but
    it can be overridden with `DJANGO_CONFIG_MODULE`
    or with `--config` parameter.
    """
    # Elevate --config option to DJANGO_CONFIG_MODULE env var
    if config:
        os.environ['DJANGO_SETTINGS_MODULE'] = config
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.module_name }}.settings')


list(map(lambda cmd: cli.add_command(import_string(cmd)), (
    '{{ cookiecutter.module_name }}.runner.commands.help.help',
    '{{ cookiecutter.module_name }}.runner.commands.django.django',
)))


def make_django_command(name, django_command=None, help=None):
    "A wrapper to convert a Django subcommand a Click command"
    if django_command is None:
        django_command = name

    @click.command(
        name=name,
        help=help,
        add_help_option=False,
        context_settings=dict(
            ignore_unknown_options=True,
        ))
    @click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
    @click.pass_context
    def inner(ctx, management_args):
        from {{ cookiecutter.module_name }}.runner.commands.django import django
        ctx.params['management_args'] = (django_command,) + management_args
        ctx.forward(django)

    return inner


list(map(cli.add_command, (
    make_django_command('migrate', help=(
        'Run migrations (like `{{ cookiecutter.module_name }} django migrate`).')),
    make_django_command('shell', help='Run a Python interactive interpreter.')
)))


def main():
    cli(obj={}, max_content_width=100)
