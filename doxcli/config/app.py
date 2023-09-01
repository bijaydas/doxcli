import os
from datetime import datetime


"""
Configs
"""
DIR_USER_HOME = os.path.expanduser('~')
DIR_SYS_CONFIG = os.path.join(DIR_USER_HOME, '.config')
DIR_CONFIG = os.path.join(DIR_USER_HOME, '.config', 'doxcli')
DOXCLI_CONFIG_FILE = os.path.join(DIR_USER_HOME, '.config', 'doxcli', 'config.yaml')


"""
DoxCli variable path. Ex. logs and other outputs
"""
DIR_SYS_LOCAL = os.path.join(DIR_USER_HOME, '.local')
DIR_LOCAL_APP = os.path.join(DIR_USER_HOME, '.local', 'doxcli')
DIR_LOCAL_APP_LOGS = os.path.join(DIR_USER_HOME, '.local', 'doxcli', 'logs')

"""
logging config
"""
LOGGER_FORMAT = '[%(asctime)s] [%(levelname)s] %(filename)s %(funcName)s %(lineno)s  %(message)s'
LOG_FILE_NAME = datetime.now().strftime('%Y-%m-%d')


def log_file():
    return os.path.join(DIR_LOCAL_APP_LOGS, LOG_FILE_NAME + '.log')
