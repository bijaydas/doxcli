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
    'bleach==6.0.0',
    'build==1.0.0',
    'certifi==2023.7.22',
    'cffi==1.15.1',
    'charset-normalizer==3.2.0',
    'cryptography==41.0.3',
    'docutils==0.20.1',
	'Faker==21.0.0',
    'idna==3.4',
    'importlib-metadata==6.8.0',
    'jaraco.classes==3.3.0',
    'jeepney==0.8.0',
    'keyring==24.2.0',
    'markdown-it-py==3.0.0',
    'mdurl==0.1.2',
    'more-itertools==10.1.0',
    'packaging==23.1',
    'pkginfo==1.9.6',
    'pycparser==2.21',
    'Pygments==2.16.1',
    'pyproject_hooks==1.0.0',
    'PyYAML==6.0.1',
    'readme-renderer==41.0',
    'requests==2.31.0',
    'requests-toolbelt==1.0.0',
    'rfc3986==2.0.0',
    'rich==13.5.2',
    'SecretStorage==3.3.3',
    'six==1.16.0',
    'tomli==2.0.1',
    'twine==4.0.2',
    'urllib3==2.0.4',
    'webencodings==0.5.1',
    'zipp==3.16.2',
]

setup_options = dict(
    name='doxcli',
    version=find_version(),
    description='Cli to create project structure',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Bijay Das',
    author_email='me@bijaydas.com',
    url='https://github.com/bijaydas/doxcli',
    scripts=['cli.py'],
    install_requires=install_requires,
    package_dir={'doxcli': 'doxcli'},
    entry_points='''
        [console_scripts]
        dox=cli:main
    ''',
    license='MIT License',
    extras_require={},
    python_requires='>=3.0',
    project_urls={
        'Source': 'https://github.com/bijaydas/doxcli',
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent"
     ],
)

setup(**setup_options)
