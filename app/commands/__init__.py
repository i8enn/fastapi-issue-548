"""Register application command"""
import click

from app.main import create_app

from .runserver import main

CONTEXT_SETTINGS = dict(
    default_map={
        'runserver': {'app': 'app.main:app'}
    }
)


# Register main CLI endpoint
@click.group(help='FastAPI Issue 548 CLI', context_settings=CONTEXT_SETTINGS)
def cli():
    create_app()


# Register main commands
cli.add_command(main)
