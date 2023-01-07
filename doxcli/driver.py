#!/usr/bin/env python

import os.path
import yaml
from pathlib import Path

__VERSION__ = '1.0.0'


class DoxCliDriver:
    __CONFIG_PATH = None
    __CONFIG_FILE_PATH = None

    def __init__(self):
        self.config_setup()

    def config_setup(self):
        """
        Checking if the config directory exists and creating if not exists
        """
        self.__CONFIG_PATH = os.path.join(Path.home(), '.local', 'doxcli')
        if not os.path.isdir(self.__CONFIG_PATH):
            os.mkdir(self.__CONFIG_PATH)

        config_template = {
            'version': __VERSION__,
        }
        __CONFIG_FILE_PATH = os.path.join(self.__CONFIG_PATH, 'config.yml')
        if not os.path.isfile(__CONFIG_FILE_PATH):
            with open(__CONFIG_FILE_PATH, 'w', encoding='utf8') as cf:
                yaml.dump(config_template, cf)

    def main(self):
        return 0
