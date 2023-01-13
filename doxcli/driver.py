#!/usr/bin/env python

import json
import os.path
import yaml
from pathlib import Path
import argparse

__VERSION__ = '1.0.0'


class DoxCliDriver:
    __CONFIG_PATH = None
    __CONFIG_FILE_PATH = None
    __DEFAULT_CONFIG_FILE_PATH = None

    """
    This value will be extracted from system config path
    """
    __TEMPLATES = None

    def __init__(self):
        self.__CONFIG_PATH = os.path.join(Path.home(), '.local', 'doxcli')
        self.__CONFIG_FILE_PATH = os.path.join(self.__CONFIG_PATH, 'config.yml')
        self.__DEFAULT_CONFIG_FILE_PATH = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'default_config.yml'
        )
        self.__setup_config()
        self.__setup_templates()

    def __setup_templates(self) -> None:
        with open(self.__CONFIG_FILE_PATH, 'r', encoding='utf-8') as cf:
            self.__TEMPLATES = yaml.load(cf, yaml.FullLoader)['templates']

    def __setup_config(self) -> bool:
        """
        Checking if the config directory exists and creating if not exists
        """
        if os.path.isfile(self.__CONFIG_FILE_PATH):
            return True
        try:
            if not os.path.isdir(self.__CONFIG_PATH):
                os.mkdir(self.__CONFIG_PATH)

            config_template = {
                'version': __VERSION__,
            }
            with open(self.__DEFAULT_CONFIG_FILE_PATH, 'r', encoding='utf8') as dcf:
                config_template['templates'] = yaml.load(dcf, yaml.FullLoader)

                with open(self.__CONFIG_FILE_PATH, 'w', encoding='utf8') as cf:
                    cf.write(json.dumps(config_template, indent=4))
            return True
        except FileNotFoundError as e:
            # TODO
            # setup logger here
            print(e)
            return False
        except PermissionError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

    def __remove_files_key(self, object: dict):
        print(object)

    def mk_structure_v1(self, template: dict, location: str):
        for key in template.keys():
            if key == 'files':
                files = template[key]
                for file in files:
                    _file = os.path.join(location, file)
                    with open(_file, 'w', encoding='utf8') as file:
                        pass
                continue

            if isinstance(template[key], list):
                _dir = os.path.join(location, key)
                if not os.path.isdir(_dir):
                    os.mkdir(_dir)
                files = template[key]
                for file in files:
                    _file = os.path.join(_dir, file)
                    with open(_file, 'w', encoding='utf8') as f:
                        pass

            _dir = os.path.join(location, key)
            if not os.path.isdir(_dir):
                os.mkdir(_dir)

            if not os.path.isdir(_dir):
                # Blank directory so skip it
                continue

            # New directory
            if isinstance(template[key], dict):
                self.mk_structure(template[key], _dir)

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
                        print(content)
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
            'template', help='Name of the project you want to create'
        )
        args.add_argument(
            'location', help='Where do you want to create the project?'
        )

        arguments = args.parse_args()

        if arguments.template not in self.__TEMPLATES.keys():
            raise ValueError(f'{arguments.template} is not defined')

        # Extracting the values
        # Which template shouldbe used
        template = self.__TEMPLATES[arguments.template]

        # Where need to create
        location = arguments.location

        self.mk_structure(template, location)

        return 0
