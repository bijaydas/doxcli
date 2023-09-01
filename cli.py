#!/usr/bin/env python

import sys
import logging

import doxcli.config.app as config
from doxcli.bootstrap import Bootstrap

logging.basicConfig(filename=config.log_file(), encoding='utf8', level=logging.DEBUG, format=config.LOGGER_FORMAT)


def main():
    try:
        Bootstrap().main()
    except NotADirectoryError as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
        print(e)
    return 0


if __name__ == '__main__':
    sys.exit(main())
