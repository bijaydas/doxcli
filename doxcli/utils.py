#!/usr/bin/env python

import json


def dump(content):
    print(json.dumps(content, indent=4))
