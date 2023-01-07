#!/usr/bin/env python

import sys
from doxcli.driver import DoxCliDriver


def main():
    return DoxCliDriver().main()


if __name__ == '__main__':
    sys.exit(main())
