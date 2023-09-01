import os
import yaml

from doxcli.config.app import DOXCLI_CONFIG_FILE


def is_config_file_available():
    return os.path.isfile(DOXCLI_CONFIG_FILE)


def get_config():
    with open(DOXCLI_CONFIG_FILE, 'r', encoding='utf8') as file:
        return yaml.safe_load(file.read())


def print_dict_pretty(_object, longest_word_length):
    print("")
    for key in _object:
        print(" | ", key, " " * (longest_word_length - len(key)), "| ",
              _object[key])
    print("")
