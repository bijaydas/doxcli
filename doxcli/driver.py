#!/usr/bin/env python

import json
import os.path
import yaml
from pathlib import Path
import argparse

import doxcli.utils as utils
from doxcli.__init__ import __version__


class DoxCliDriver:
    # Config path without file name
    __CONFIG_PATH = None

    # Config path with file name
    __CONFIG_FILE_PATH = None

    """
    Default config path with the package. If there is no config file in user's
    home directory and user has not provided any custom config file, this file
    will be copied to /home/{USER}/.config/doxcli 
    """
    __DEFAULT_CONFIG_FILE_PATH = None

    """
    User defined config file
    """
    __USER_DEFINED_CONFIG_FILE = None

    """
    This value will be extracted from system config path
    """
    __TEMPLATES = None

    """
    Name of the config file
    """
    __CONFIG_FILE_NAME = 'config.yml'

    """
    Keys to ignore
    """
    __IGNORE_KEYS = ('is_dir', 'commands',)

    def __init__(self):
        self.__CONFIG_PATH = os.path.join(Path.home(), '.config', 'doxcli')
        self.__CONFIG_FILE_PATH = os.path.join(
            self.__CONFIG_PATH,
            self.__CONFIG_FILE_NAME
        )
        self.__DEFAULT_CONFIG_FILE_PATH = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'data',
            'config.yml',
        )

    def __validate_config_file(self):
        # TODO:
        # Validate if the config file is valid
        pass

    def __setup_new_template(self, _config_file):
        config_template = {
            'version': __version__,
        }
        if not os.path.isdir(self.__CONFIG_PATH):
            os.mkdir(self.__CONFIG_PATH)

        with open(_config_file, 'r', encoding='utf8') as dcf:
            config_template['templates'] = yaml.load(dcf, yaml.FullLoader)
            self.__TEMPLATES = config_template['templates']

            with open(
                    f'{self.__CONFIG_PATH}/{self.__CONFIG_FILE_NAME}', 'w',
                    encoding='utf8'
            ) as cf:
                cf.write(json.dumps(config_template, indent=4))

    def __load_existing_template(self, _config_file) -> None:
        with open(_config_file, 'r', encoding='utf8') as dcf:
            _template = yaml.load(dcf, yaml.FullLoader)
            self.__TEMPLATES = _template['templates']

    def __setup_config(self) -> bool:
        try:
            _config_file = self.__DEFAULT_CONFIG_FILE_PATH

            if self.__USER_DEFINED_CONFIG_FILE:
                self.__validate_config_file()

                """
                Check if any file exits, and ask if user wants to replace it?
                """
                if os.path.isfile(self.__CONFIG_FILE_PATH):
                    if utils.confirm(f'{self.__CONFIG_FILE_PATH}'
                               f' already exits, do you want to replace it?'):
                        os.remove(self.__CONFIG_FILE_PATH)
                    else:
                        """
                        User denies to delete, load the existing config file.
                        """
                        self.__load_existing_template(self.__CONFIG_FILE_PATH)
                        return True
                _config_file = self.__USER_DEFINED_CONFIG_FILE
            self.__setup_new_template(_config_file)
            return True
        except FileNotFoundError as e:
            # TODO
            # setup logger and proper error message
            print(e)
            return False
        except PermissionError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

    def mk_structure(self, template: dict, location: str):
        for key in template:

            if key == 'commands':
                utils.shell(template[key], location)
                continue

            """
            There are some system defined keys i.e is_dir or any other.
            These keys should be ignored
            """
            if key in self.__IGNORE_KEYS:
                continue

            if utils.is_file(template[key]):
                content = ""
                if utils.has_content(template[key]):
                    content = template[key]['content']
                utils.create_file(os.path.join(location, key), content)
                continue

            """
            Else make the directory and recreate the structure
            """
            _path = os.path.join(location, key)
            os.mkdir(_path)
            self.mk_structure(template[key], _path)

    def main(self) -> int:
        args = argparse.ArgumentParser(
            prog='Cli to create project templates'
        )
        args.add_argument(
            'template',
            help='Name of the project you want to create'
        )
        args.add_argument(
            'location',
            help='Where do you want to create the project?',
            default='.',
        )
        args.add_argument(
            '--config', help='New config path.',
        )

        arguments = args.parse_args()

        if not utils.is_dir_empty(arguments.location):
            raise Exception(f'{arguments.location} not empty')

        """
        Check if location directory exists
        """
        if not os.path.isdir(arguments.location):
            if utils.confirm(f'{arguments.location} does not exists, do you want to create?'):
                os.mkdir(arguments.location)
            else:
                raise FileNotFoundError(f'{arguments.location} not found')

        if arguments.config is not None:
            self.__USER_DEFINED_CONFIG_FILE = os.path.abspath(arguments.config)

        self.__setup_config()

        """
        Check if the template provided by user exits with us
        """
        if arguments.template not in self.__TEMPLATES.keys():
            raise ValueError(f'{arguments.template} is not defined')

        """
        Extracting the values
        Which template should be used
        """
        template = self.__TEMPLATES[arguments.template]

        self.mk_structure(template, arguments.location)

        # print_message('Directory created successfully!')

        return 0
