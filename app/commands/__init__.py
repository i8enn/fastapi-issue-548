"""Register application command"""
import click
import platform

from uvicorn import __version__ as uvicorn_version
from fastapi import __version__ as fastapi_version

from app.main import create_app
from app import __version__ as app_version

from .runserver import main


def get_version():
    """App version like flask"""

    # Crutch ;)  -- (Not using in real code)
    message = f'{"="*50}\n' \
              'Platform -- %(os)s\n' \
              'Python -- %(python)s\n' \
              'FastAPI -- %(fastapi)s\n' \
              'Uvicorn -- %(uvicorn)s\n' \
              'App version -- %(app_version)s\n'\
              f'{"="*50}' \
              % {
                  'os': platform.platform(),
                  'python': platform.python_version(),
                  'fastapi': fastapi_version,
                  'uvicorn': uvicorn_version,
                  'app_version': app_version
              }
    return message


CONTEXT_SETTINGS = dict(
    default_map={
        'runserver': {'app': 'app.main:app'}
    }
)


# Register main CLI endpoint
@click.version_option(version=get_version(), message='%(version)s')
@click.group(help='FastAPI Issue 548 CLI', context_settings=CONTEXT_SETTINGS)
def cli():
    create_app()


# Register main commands
cli.add_command(main)
