import os


def configuration(f):
    import click
    from functools import update_wrapper

    @click.pass_context
    def inner(ctx, *args, **kwargs):
        # HACK: We can't call `configure()` from within tests
        # since we don't load config files from disk, so we
        # need a way to bypass this initialization step
        if os.environ.get('_{{ cookiecutter.module_name|upper }}_SKIP_CONFIGURATION') != '1':
            from {{ cookiecutter.module_name }}.runner import configure
            configure()
        return ctx.invoke(f, *args, **kwargs)
    return update_wrapper(inner, f)
