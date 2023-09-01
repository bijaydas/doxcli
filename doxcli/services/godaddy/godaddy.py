import os
from requests import request

from doxcli.utils.general import is_config_file_available, get_config, print_dict_pretty
from doxcli.exceptions.config import ConfigException


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

    def is_available(self, domain_name=None):
        if not is_config_file_available():
            raise ConfigException("Config file not found")

        response = request(
            url=f"{self.url}{domain_name}",
            method='GET',
            headers=self.get_headers()
        )
        result = response.json()
        keys = result.keys()

        print_dict_pretty(result, len(max(keys, key=len)))

        return 0
