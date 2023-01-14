#!/usr/bin/env python

import json
import os


def dump(content):
    print(json.dumps(content, indent=4))


def confirm(content):
    result = input(f' {content} (y/n)\n > ').lower()
    if result == 'y':
        return True
    return False


def version_check():
    pass


def read(path):
    if not os.path.isfile(path):
        raise RuntimeError(f'{path} not found')
    return open(path, 'r').read()
