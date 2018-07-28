"""
This module contains common reusable functions.
"""

from SupportLibraries.ui_helpers import UIHelpers


class BaseHelpers(UIHelpers):
    """
    This class includes basic reusable base_helpers.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Include your base helper methods here
