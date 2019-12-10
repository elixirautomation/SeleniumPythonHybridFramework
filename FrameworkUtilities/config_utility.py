"""
This module contains config utility functions.
"""

import os
import time
import logging
from traceback import print_stack
from configparser import ConfigParser
import FrameworkUtilities.logger_utility as log_utils


class ConfigUtility:
    """
    This class includes basic reusable config_helpers.
    """

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.cur_path, r"../ConfigFiles/config.ini")

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read(self.config_path)

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)

        return config

    def change_properties_file(self, section, property_name, property_value):
        """
        This method is used to change the property value
        :param section: property section in ini file
        :param property_name: property name to change
        :param property_value: property value to set
        :return: it returns boolean value for successful change property operation
        """
        flag = False
        try:
            config = self.load_properties_file()
            config[section][property_name] = property_value

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)

            time.sleep(1)
            flag = True

        except Exception as ex:
            self.log.error("Failed to change ini/properties file.", ex)

        return flag
