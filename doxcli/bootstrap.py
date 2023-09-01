import os
import argparse

import doxcli.config.app as config
from doxcli.services.godaddy.godaddy import GoDaddy


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

    def setup_args_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "service",
            help="What service would you like to run? Ex. GoDaddy, ABC, XYZ",

            # All the available services will get listed here.
            choices=["godaddy"]
        )

        parser.add_argument(
            "--name",
            help="First argument for service"
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
        service = None

        if args.service == "godaddy":
            service = GoDaddy()

            """
            Check what user wants to do with --name argument.
            
            If there is no --name then show help and exit.
            """
            if not args.name:
                parser.print_help()
                return 0

            """
            Loading functionality for GoDaddy, which is Domain search
            """
            return service.is_available(args.name)
