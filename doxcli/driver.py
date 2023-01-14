#!/usr/bin/env python

import json
import os.path
import yaml
from pathlib import Path
import argparse

from doxcli.utils import confirm

__VERSION__ = '1.0.0'


class DoxCliDriver:
    # Config path without file name
    __CONFIG_PATH = None

    # Config path with file name
    __CONFIG_FILE_PATH = None

    """
    Default config path with the package. If there is no config file in user's
    home directory and user has not provided any custom config file, this file
    will be copied to /home/{USER}/.local/doxcli 
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

    def __init__(self):
        self.__CONFIG_PATH = os.path.join(Path.home(), '.local', 'doxcli')
        self.__CONFIG_FILE_PATH = os.path.join(
            self.__CONFIG_PATH,
            self.__CONFIG_FILE_NAME
        )
        self.__DEFAULT_CONFIG_FILE_PATH = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'default_config.yml'
        )

    def __validate_config_file(self):
        # TODO:
        # Validate if the config file is valid
        pass

    def __setup_new_template(self, _config_file):
        config_template = {
            'version': __VERSION__,
        }
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
                    if confirm(f'{self.__CONFIG_FILE_PATH}'
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
        for key in template.keys():
            if key == 'is_dir':
                continue
            """
            If there is no key in the object or
            there are keys in the object but not 'is_dir' key.
            """
            if template[key] is None or 'is_dir' not in template[key]:
                _path = os.path.join(location, key)
                content = """"""
                if not os.path.isfile(_path):
                    with open(_path, 'w', encoding='utf-8') as f:
                        if isinstance(template[key], dict) and 'content' in template[key]:
                            content = template[key]['content']
                        f.write(content)
                # No need to execute further
                continue

            # Create the directory with same name and recall the method
            if 'is_dir' in template[key]:
                _path = os.path.join(location, key)
                if not os.path.isdir(_path):
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
            '--location',
            help='Where do you want to create the project?',
            default='.',
        )
        args.add_argument(
            '--config', help='New config path.',
        )

        arguments = args.parse_args()

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

        return 0
