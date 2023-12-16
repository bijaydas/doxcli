import os
import argparse
import sys

import doxcli.config.app as config
from doxcli.services.godaddy.godaddy import GoDaddy
from doxcli.services.faker.fakes import Fakes
from . import __version__


class Bootstrap:

    def __init__(self):
        """
        User's home directory
        """
        self._dir_home = config.DIR_USER_HOME

        """
        Config options
        """
        self._dir_sys_config = config.DIR_SYS_CONFIG
        self._dir_config = config.DIR_CONFIG

        """
        Logs options
        """
        self._dir_local = config.DIR_SYS_LOCAL
        self._dir_local_doxcli = config.DIR_LOCAL_APP
        self._dir_local_doxcli_log = config.DIR_LOCAL_APP_LOGS

    def _setup_config_dir(self):
        """
        Checking if config directory is available.
        """
        if not os.path.isdir(self._dir_sys_config):
            raise NotADirectoryError('Config dir not found')

        """
        Checking if doxcli directory available.
        
        If not present then creating
        """
        if not os.path.isdir(self._dir_config):
            os.mkdir(self._dir_config)

    def _setup_log_dir(self):
        """
        Checking if log directory is available.
        """
        if not os.path.isdir(self._dir_sys_config):
            raise NotADirectoryError('Config dir not found')

        """
        Checking if doxcli directory available within .local directory.

        If not present then creating
        """
        if not os.path.isdir(self._dir_local_doxcli):
            os.mkdir(self._dir_local_doxcli)

        """
        Checking if logs directory available within .local/doxcli
        
        If not present then creating
        """
        if not os.path.isdir(self._dir_local_doxcli_log):
            os.mkdir(self._dir_local_doxcli_log)

    def setup_dirs(self):
        self._setup_config_dir()
        self._setup_log_dir()

    @staticmethod
    def setup_args_parser():
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "service",
            help="What service would you like to run? Ex. GoDaddy, ABC, XYZ",

            # All the available services will get listed here.
            choices=["godaddy", "faker"]
        )

        parser.add_argument(
            "--name",
            help="Name argument for service"
        )
        parser.add_argument(
            "-v",
            "--version",
            help="Check current version",
            action='version',
            version=__version__
        )
        parser.add_argument(
            "--file",
            help="File path argument for service"
        )

        return parser

    def main(self):
        """
        Will set up the config and local directory in ~/
        """
        self.setup_dirs()

        """
        User arguments
        """
        parser = self.setup_args_parser()
        args = parser.parse_args()

        """
        Service instance selected by user
        """

        if args.service == "godaddy":
            service = GoDaddy()

            if args.name:
                """
                Loading functionality for GoDaddy, which is Domain search
                by name.
                """
                return service.is_available_by_name(args.name)

            if args.file:
                """
                Loading functionality for GoDaddy, which is Domain search
                by file.
                """
                return service.is_available_by_file(args.file)

        if args.service == 'faker':
            service = Fakes()
            return service.call_user_func(args.name)

        """
        Check what user wants to do with --name argument.
        
        If there is no --name then show help and exit.
        """
        parser.print_help()
        return 0
