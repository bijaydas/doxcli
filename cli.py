#!/usr/bin/env python

import sys
from doxcli.driver import DoxCliDriver
from doxcli.utils import print_error


def main():
    try:
        return DoxCliDriver().main()
    except FileNotFoundError as e:
        print_error(e)
    except Exception as e:
        print_error(e)


if __name__ == '__main__':
    sys.exit(main())
