import os
import doxcli.config.app as config


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

    def main(self):
        self._setup_config_dir()
        self._setup_log_dir()
