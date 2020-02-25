"""
Runserver command

Override uvicorn.main cli command.
"""
import ssl
import sys
import typing

import click
from uvicorn.config import SSL_PROTOCOL_VERSION
from uvicorn.main import (HTTP_CHOICES, INTERFACE_CHOICES, LEVEL_CHOICES,
                          LIFESPAN_CHOICES, LOOP_CHOICES, WS_CHOICES, run)


@click.command(
    'runserver',
    help='Run app with uvicorn server'
)
@click.argument('app')
@click.option(
    '--host',
    type=str,
    default='127.0.0.1',
    help='Bind socket to this host.',
    show_default=True,
)
@click.option(
    '--port',
    type=int,
    default=8000,
    help='Bind socket to this port.',
    show_default=True,
)
@click.option(
    '--uds',
    type=str,
    default=None,
    help='Bind to a UNIX domain socket.'
)
@click.option(
    '--fd',
    type=int,
    default=None,
    help='Bind to socket from this file descriptor.'
)
@click.option(
    '--debug',
    is_flag=True,
    default=False,
    help='Enable debug mode.',
    hidden=True
)
@click.option(
    '--reload',
    is_flag=True,
    default=False,
    help='Enable auto-reload.'
)
@click.option(
    '--reload-dir',
    'reload_dirs',
    multiple=True,
    help='Set reload directories explicitly, instead of using "sys.path".',
)
@click.option(
    '--workers',
    default=1,
    type=int,
    help='Number of worker processes. Not valid with --reload.',
)
@click.option(
    '--loop',
    type=LOOP_CHOICES,
    default='auto',
    help='Event loop implementation.',
    show_default=True,
)
@click.option(
    '--http',
    type=HTTP_CHOICES,
    default='auto',
    help='HTTP protocol implementation.',
    show_default=True,
)
@click.option(
    '--ws',
    type=WS_CHOICES,
    default='auto',
    help='WebSocket protocol implementation.',
    show_default=True,
)
@click.option(
    '--lifespan',
    type=LIFESPAN_CHOICES,
    default='auto',
    help='Lifespan implementation.',
    show_default=True,
)
@click.option(
    '--interface',
    type=INTERFACE_CHOICES,
    default='auto',
    help='Select ASGI3, ASGI2, or WSGI as the application interface.',
    show_default=True,
)
@click.option(
    '--log-level',
    type=LEVEL_CHOICES,
    default='info',
    help='Log level.',
    show_default=True,
)
@click.option(
    '--no-access-log', is_flag=True, default=False, help='Disable access log.'
)
@click.option(
    '--proxy-headers',
    is_flag=True,
    default=False,
    help='Use X-Forwarded-Proto, X-Forwarded-For, X-Forwarded-Port to '
         'populate remote address info.',
)
@click.option(
    '--root-path',
    type=str,
    default='',
    help='Set the ASGI "root_path" for applications submounted below a given '
         'URL path.',
)
@click.option(
    '--limit-concurrency',
    type=int,
    default=None,
    help='Maximum number of concurrent connections or tasks to allow, '
         'before issuing HTTP 503 responses.',
)
@click.option(
    '--limit-max-requests',
    type=int,
    default=None,
    help='Maximum number of requests to service before terminating the '
         'process.',
)
@click.option(
    '--timeout-keep-alive',
    type=int,
    default=5,
    help='Close Keep-Alive connections if no new data is received within '
         'this timeout.',
    show_default=True,
)
@click.option(
    '--ssl-keyfile',
    type=str,
    default=None,
    help='SSL key file',
    show_default=True
)
@click.option(
    '--ssl-certfile',
    type=str,
    default=None,
    help='SSL certificate file',
    show_default=True,
)
@click.option(
    '--ssl-version',
    type=int,
    default=SSL_PROTOCOL_VERSION,
    help='SSL version to use (see stdlib ssl module\'s)',
    show_default=True,
)
@click.option(
    '--ssl-cert-reqs',
    type=int,
    default=ssl.CERT_NONE,
    help='Whether client certificate is required (see stdlib ssl module\'s)',
    show_default=True,
)
@click.option(
    '--ssl-ca-certs',
    type=str,
    default=None,
    help='CA certificates file',
    show_default=True,
)
@click.option(
    '--ssl-ciphers',
    type=str,
    default='TLSv1',
    help='Ciphers to use (see stdlib ssl module\'s)',
    show_default=True,
)
@click.option(
    '--header',
    'headers',
    multiple=True,
    help='Specify custom default HTTP response headers as a Name:Value pair',
)
def main(
        app,
        host: str,
        port: int,
        uds: str,
        fd: int,
        loop: str,
        http: str,
        ws: str,
        lifespan: str,
        interface: str,
        debug: bool,
        reload: bool,
        reload_dirs: typing.List[str],
        workers: int,
        log_level: str,
        no_access_log: bool,
        proxy_headers: bool,
        root_path: str,
        limit_concurrency: int,
        limit_max_requests: int,
        timeout_keep_alive: int,
        ssl_keyfile: str,
        ssl_certfile: str,
        ssl_version: int,
        ssl_cert_reqs: int,
        ssl_ca_certs: str,
        ssl_ciphers: str,
        headers: typing.List[str],
):
    sys.path.insert(0, '.')

    kwargs = {
        'app': app,
        'host': host,
        'port': port,
        'uds': uds,
        'fd': fd,
        'loop': loop,
        'http': http,
        'ws': ws,
        'lifespan': lifespan,
        'log_level': log_level,
        'access_log': not no_access_log,
        'interface': interface,
        'debug': debug,
        'reload': reload,
        'reload_dirs': reload_dirs if reload_dirs else None,
        'workers': workers,
        'proxy_headers': proxy_headers,
        'root_path': root_path,
        'limit_concurrency': limit_concurrency,
        'limit_max_requests': limit_max_requests,
        'timeout_keep_alive': timeout_keep_alive,
        'ssl_keyfile': ssl_keyfile,
        'ssl_certfile': ssl_certfile,
        'ssl_version': ssl_version,
        'ssl_cert_reqs': ssl_cert_reqs,
        'ssl_ca_certs': ssl_ca_certs,
        'ssl_ciphers': ssl_ciphers,
        'headers': list([header.split(':') for header in headers]),
    }
    run(**kwargs)
