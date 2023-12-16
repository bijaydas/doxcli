import csv
import os
import time

from requests import request

from doxcli.utils.general import is_config_file_available, get_config, \
    print_dict_pretty
from doxcli.exceptions.general import ConfigException
from doxcli.utils.file import parse_json_file, parse_txt_file


class GoDaddy:
    """
    GoDaddy service class for Domain functionality
    """

    """
    GoDaddy config
    """
    config = None

    """
    URL
    """
    url = None

    def __init__(self):
        self.config = get_config()['godaddy']
        self.url = "https://api.godaddy.com/v1/domains/available?domain="

    def get_headers(self):
        return {
            "Authorization": f"sso-key {self.config['api_key']}:{self.config['api_secret']}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def is_available_by_name(self, name):
        if not is_config_file_available():
            raise ConfigException("Config file not found")

        response = request(
            url=f"{self.url}{name}",
            method='GET',
            headers=self.get_headers()
        )
        result = response.json()
        keys = result.keys()

        print_dict_pretty(result, len(max(keys, key=len)))

        return 0

    def is_available_by_file(self, file_path):
        if not is_config_file_available():
            raise ConfigException("Config file not found")

        if not os.path.isfile(file_path):
            raise FileExistsError(f"{file_path} not found")

        if file_path.endswith('json'):
            domains = parse_json_file(file_path)
        else:
            domains = parse_txt_file(file_path)

        if len(domains) == 0:
            print("No data found")
            return 0

        for _domain in domains:
            domain = _domain.strip()

            response = request(
                url=f"{self.url}{domain}",
                method='GET',
                headers=self.get_headers()
            )
            result = response.json()
            keys = result.keys()

            print_dict_pretty(result, len(max(keys, key=len)))
            time.sleep(2)

        return 0
