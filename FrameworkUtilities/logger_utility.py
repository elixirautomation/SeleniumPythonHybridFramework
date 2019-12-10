""" This module contains the methods for logging. """

import os
import logging
import inspect
from datetime import datetime


def custom_logger(log_level=logging.INFO):

    """
    This is logging method.
    :param log_level: Log levels
    :return: logger
    """

    log_filename = None

    cur_path = os.path.abspath(os.path.dirname(__file__))
    log_dir = os.path.join(cur_path, r"../Logs/")

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    date_dir = os.path.join(log_dir, str(datetime.strftime(datetime.now(), '%d%m%Y')))

    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    current_time = datetime.strftime(datetime.now(), '%d%m%Y-%H%M%S')

    if log_filename is None:
        temp_file = "RAFT_" + current_time + ".log"
        log_filename = os.path.join(date_dir, temp_file)

    caller_name = inspect.stack()[1][1] + " - \tLN:" + str(inspect.stack()[1][2])
    caller_name = str(caller_name)

    logging.basicConfig(filename=log_filename, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(caller_name)

    # Set logging level for logger
    logger.setLevel(log_level)

    return logger
