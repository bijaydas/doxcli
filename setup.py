#!/usr/bin/env python

import os
import re
from setuptools import setup


def read(path):
    return open(path, 'r').read()


def find_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, 'doxcli', '__init__.py')
    with open(version_file, 'r', encoding='utf8') as f:
        content = f.read().strip()
        version = re.search(r'__version__ = \'(\d+.\d+.\d+)', content, re.M)
        return version.group().split('\'')[1]


install_requires = [
    'PyYAML==6.0',
]

setup_options = dict(
    name='doxcli',
    version=find_version(),
    description='Cli to create project structure',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Bijay Das',
    author_email='imbijaydas@gmail.com',
    url='https://github.com/bijaydas/dox-cli',
    scripts=['cli.py'],
    package_data={'doxcli': ['data/*']},
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        dox=cli:main
    ''',
    license='MIT License',
    extras_require={},
    python_requires='>=3.7',
    project_urls={
        'Source': 'https://github.com/bijaydas/dox-cli',
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent"
     ],
)

setup(**setup_options)
