""" This module contains the singleton driver instance implementation"""


import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as ffOptions
from FrameworkUtilities.config_utility import ConfigUtility
from FrameworkUtilities.logger_utility import custom_logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    """
    This class contains the reusable methods for getting the driver instances
    """
    log = custom_logger(logging.INFO)
    config = ConfigUtility()

    def __init__(self, browser, platform, environment, url=""):
        self.platform = platform
        self.browser = browser
        self.environment = environment
        self.url = url
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.prop = self.config.load_properties_file()

    def get_driver_instance(self):

        if self.browser == "chrome":

            chrome_capabilities = webdriver.DesiredCapabilities.CHROME
            chrome_capabilities['platform'] = self.platform
            chrome_capabilities['browserName'] = 'chrome'
            chrome_capabilities['javascriptEnabled'] = True

            options = chromeOptions()
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

            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities=chrome_capabilities, options=options)

        elif self.browser == "firefox":

            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['platform'] = self.platform
            firefox_capabilities['browserName'] = 'firefox'
            firefox_capabilities['javascriptEnabled'] = True
            firefox_capabilities['marionette'] = True

            options = ffOptions()
            options.log.level = 'trace'

            driver = webdriver.Remote(command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                                      desired_capabilities=firefox_capabilities, options=options)

        elif self.browser == "safari":

            safari_capabilities = webdriver.DesiredCapabilities.SAFARI
            safari_capabilities['platform'] = self.platform
            safari_capabilities['browserName'] = 'safari'
            safari_capabilities['javascriptEnabled'] = True

            driver = webdriver.Remote(
                command_executor=self.prop.get('GRID', 'GRID_SERVER'),
                desired_capabilities=safari_capabilities)

        elif self.browser == "sauce":

            username = self.prop.get('CLOUD', 'sl_username')
            automate_key = self.prop.get('CLOUD', 'sl_key')
            url = "https://{}:{}@ondemand.saucelabs.com:443/wd/hub".format(username, automate_key)
            caps = {'browserName': "Safari", 'appiumVersion': "1.8.1", 'deviceName': "iPhone X Simulator",
                    'deviceOrientation': "portrait", 'platformVersion': "11.3", 'platformName': "iOS",
                    'name': "iPhone X Execution"}

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "browserstack_web":

            username = self.prop.get('CLOUD', 'bs_username')
            automate_key = self.prop.get('CLOUD', 'bs_key')
            url = "http://{}:{}@hub.browserstack.com:80/wd/hub".format(username, automate_key)

            caps = {'browser': 'Firefox', 'browser_version': '61.0', 'os': 'OS X', 'os_version': 'High Sierra',
                    'resolution': '1024x768', 'name': "Mac Safari Execution", 'browserstack.debug': True,
                    'browserstack.networkLogs': True}

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "browserstack_mobile":

            username = self.prop.get('CLOUD', 'bs_username')
            automate_key = self.prop.get('CLOUD', 'bs_key')
            url = "http://{}:{}@hub.browserstack.com:80/wd/hub".format(username, automate_key)

            caps = {'device': 'Google Pixel', 'os_version': '7.1', 'name': "Google Pixcel Execution"}

            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=caps)

        elif self.browser == "local_chrome":

            options = chromeOptions()
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

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        elif self.browser == "local_firefox":

            browser_profile = webdriver.FirefoxProfile()
            browser_profile.set_preference("dom.webnotifications.enabled", False)

            options = ffOptions()
            options.log.level = 'trace'
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True

            driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=GeckoDriverManager().install(),
                                       options=options, service_log_path='/tmp/geckodriver.log',
                                       firefox_profile=browser_profile)

        else:

            options = chromeOptions()
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

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        if "chrome" in self.browser:
            driver.fullscreen_window()

        if self.environment == "staging":
            test_data = self.prop.get('RAFT', 'staging_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'staging_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        elif self.environment == "prod":
            test_data = self.prop.get('RAFT', 'prod_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'prod_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        else:
            test_data = self.prop.get('RAFT', 'staging_test_data')
            self.config.change_properties_file('RAFT', 'base_test_data', test_data)
            self.url = self.prop.get('RAFT', 'staging_url')
            self.config.change_properties_file('RAFT', 'base_url', self.url)

        driver.get(self.url)

        return driver
