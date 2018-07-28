""" This module contains the singleton driver instance implementation"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from FrameworkUtilities.config_utility import ConfigUtility


class DriverFactory():
    """
    This class contains the reusable methods for getting the driver instances
    """

    def __init__(self, browser):
        self.browser = browser
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.cur_path, r"../ConfigFiles/config.ini")
        self.config = ConfigUtility(self.path)
        self.prop = self.config.load_properties_file()

    def get_driver_instance(self):
        driver = None

        if self.browser == "macos_chrome":
            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities={'platform':'Mac OS X 10.9','browserName': 'chrome', 'javascriptEnabled': True})

        elif self.browser == "macos_firefox":
            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities={'platform':'Mac OS X 10.9','browserName': 'firefox', 'javascriptEnabled': True})

        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = driver_location

            options = Options()
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-automation")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})

            driver = webdriver.Chrome(driver_location, chrome_options=options)

        else:
            driver_location = os.path.join(self.cur_path, r"../ExternalDrivers/chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = driver_location

            options = Options()
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-web-security")
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-automation")
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                      'profile': {'password_manager_enabled': False}})

            driver = webdriver.Chrome(driver_location, chrome_options=options)

        # driver.fullscreen_window()
        driver.get(self.prop.get('SELENIUM', 'BASE_URL'))
        return driver
