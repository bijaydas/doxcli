#!/usr/bin/env python

import json
import os
import subprocess


def dump(content):
    print(json.dumps(content, indent=4))


def confirm(content):
    result = input(f' {content} (y/n)\n > ').lower()
    if result == 'y':
        return True
    return False


def print_error(content):
    print(f'ERROR: {content}')


def print_message(content):
    print(f'Success: {content}')


def version_check():
    pass


def read(path):
    if not os.path.isfile(path):
        raise RuntimeError(f'{path} not found')
    return open(path, 'r').read()


def is_file(value):
    return value is None or 'content' in value


def has_content(value):
    return value is not None and 'content' in value


def create_file(path, content=""):
    with open(path, 'w', encoding='utf8') as f:
        f.write(content)


def is_empty(value):
    if isinstance(value, dict):
        return bool(value) is False
    return False


def is_dir_empty(path):
    return len(os.listdir(path)) == 0


def shell(_commands: str = None, cwd: str = None):
    commands = list(filter(None, _commands.split('\n')))
    for command in commands:
        try:
            print(f'Executing {command}...')
            subprocess.run(command, cwd=cwd, shell=True)
        except Exception as e:
            # TODO:
            # Fix error message
            print(e)
