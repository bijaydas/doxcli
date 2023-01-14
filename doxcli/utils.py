#!/usr/bin/env python

import json


def dump(content):
    print(json.dumps(content, indent=4))


def confirm(content):
    result = input(f' {content} (y/n)\n > ').lower()
    if result == 'y':
        return True
    return False
