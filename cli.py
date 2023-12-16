#!/usr/bin/env python

import sys
import logging

import doxcli.config.app as config
from doxcli.bootstrap import Bootstrap
from doxcli.exceptions.general import MethodNotFoundException
from doxcli.utils.general import display_error

logging.basicConfig(
    filename=config.log_file(),
    encoding='utf8',
    level=logging.DEBUG,
    format=config.LOGGER_FORMAT
)


def main():
    try:
        return Bootstrap().main()
    except NotADirectoryError as exception:
        logging.error(exception)
    except FileExistsError as exception:
        logging.error(exception)
    except MethodNotFoundException as exception:
        display_error(exception)
        logging.error(exception)
    except Exception as exception:
        logging.error(exception)
    return 0


if __name__ == '__main__':
    sys.exit(main())
