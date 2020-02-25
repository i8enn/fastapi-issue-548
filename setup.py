import sys
from setuptools import setup, find_packages

is_wheel = 'bdist_wheel' in sys.argv

excluded = []


def exclude_package(pkg):
    for exclude in excluded:
        if pkg.startswith(exclude):
            return True
    return False


def create_package_list(base_package):
    return ([base_package] +
            [base_package + '.' + pkg
             for pkg
             in find_packages(base_package)
             if not exclude_package(pkg)])


setup(
    # Metadata
    name='fastapi_issue_548',
    version='0.1.0',
    author='Ivan Galin',
    description='FastAPI application for reproduce bug',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only'
        'Programming Language :: Python :: 3.7',
        'Framework :: FastAPI'
    ],
    packages=['app'],
    entry_points={
        'console_scripts': [
            'fastapi-issue-548=app.commands:cli'
        ],
    },
)
