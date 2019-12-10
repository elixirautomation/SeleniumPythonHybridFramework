"""
This module contains common reusable functions.
"""

from traceback import print_stack
from configparser import ConfigParser
from SupportLibraries.ui_helpers import UIHelpers


class BaseHelpers(UIHelpers):
    """
    This class includes basic reusable base_helpers.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read('test.ini')

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config
