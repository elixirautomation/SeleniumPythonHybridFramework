"""
This module contains most of the reusable functions to support test cases.
"""

import os
import time
import logging
import random
import string
from traceback import print_stack
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import FrameworkUtilities.logger_utility as log_utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIHelpers:
    """
    UI Helpers class to contains all ui helper methods.
    """

    def __init__(self, driver):
        self.driver = driver

    log = log_utils.custom_logger(logging.INFO)

    def get_title(self):

        """
        This method is used for getting the page title.
        :return: this method returns nothing.
        """
        page_title = ""
        try:
            page_title = self.driver.title
            if page_title is None:
                self.log.error("Page title value is empty.")
        except:
            self.log.error("Exception occurred while retrieving the page title.")

        return page_title

    def get_locator_type(self, locator_type):

        """
        This method is used for getting locator type for element
        :param locator_type: it takes the locator type parameter ex- xpath, id
        :return: it returns the element identification based on locator type
        """

        try:
            locator_type = locator_type.lower()

            if locator_type == "id":
                return By.ID
            elif locator_type == "xpath":
                return By.XPATH
            elif locator_type == "name":
                return By.NAME
            elif locator_type == "class":
                return By.CLASS_NAME
            elif locator_type == "link":
                return By.LINK_TEXT
            elif locator_type == "partiallink":
                return By.PARTIAL_LINK_TEXT
        except:
            self.log.error("Locator Type '" + locator_type + "' is not listed.")

    def wait_for_element_to_be_present(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This function is used for explicit waits till element present
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element located or not
        """

        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            return False

    def wait_for_element_to_be_clickable(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This function is used for explicit waits till element clickable
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element located or not
        """

        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.element_to_be_clickable((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            self.log.error("Exception occurred while waiting for element to be clickable.")
            return False

    def wait_for_element_to_be_displayed(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This function is used for explicit waits till element displayed
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element located or not
        """

        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.visibility_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            self.log.error("Exception occurred while waiting for element to be visible.")
            return False

    def wait_for_element_to_be_invisible(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This function is used for explicit waits till element displayed
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element located or not
        """

        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.invisibility_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            return False

    def is_element_present(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to return the boolean value for element present
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element present or not
        """

        flag = False
        try:
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element present with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                flag = True
            else:
                self.log.error(
                    "Element not present with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during element identification.")

        return flag

    def verify_element_not_present(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to return the boolean value for element present
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element present or not
        """

        flag = False
        try:
            if self.wait_for_element_to_be_invisible(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element invisible with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                flag = True
            else:
                self.log.error(
                    "Element is visible with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during element to be invisible.")

        return flag

    def is_element_displayed(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to return the boolean value for element displayed
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element displayed or not
        """

        try:
            if self.wait_for_element_to_be_displayed(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return True
            else:
                self.log.error(
                    "Element not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return False
        except:
            self.log.error("Exception occurred during element identification.")
            return False

    def is_element_clickable(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to return the boolean value for element clickable
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element clickable or not
        """

        try:
            if self.wait_for_element_to_be_clickable(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element is clickable with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return True
            else:
                self.log.error(
                    "Element is not clickable with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return False
        except:
            self.log.error("Exception occurred during element identification.")
            return False

    def is_element_checked(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to return the boolean value for element checked/ selected
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to the element present or not
        """

        flag = False
        try:
            if self.is_element_present(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                if element.is_selected():
                    self.log.info(
                        "Element is selected/ checked with locator_properties: " +
                        locator_properties + " and locator_type: " + locator_type)
                    flag = True
                else:
                    self.log.error(
                        "Element is not selected/ checked with locator_properties: " +
                        locator_properties + " and locator_type: " + locator_type)
        except:
            flag = False

        return flag

    def verify_elements_located(self, locator_dict, max_timeout=10):

        """
        This method is used to return the boolean value according to element presents on page
        :param locator_dict: this parameter takes the list of locator value and it's type
        :param max_timeout: this is the maximum time to wait for particular element
        :return: it returns the boolean value according to element presents on page
        """

        flag = False
        result = []
        try:

            for locator_prop in locator_dict.keys():
                prop_type = locator_dict[locator_prop]
                if self.wait_for_element_to_be_present(locator_prop, prop_type, max_timeout):
                    self.log.info(
                        "Element found with locator_properties: " + locator_prop +
                        " and locator_type: " + locator_dict[locator_prop])
                    flag = True
                else:
                    self.log.error(
                        "Element not found with locator_properties: " + locator_prop +
                        " and locator_type: " + locator_dict[locator_prop])
                    flag = False
                result.append(flag)

        except Exception as ex:
            self.log.error("Exception occurred during element identification: ", ex)

        if False in result:
            return False
        else:
            return True

    def get_element(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to get the element according to the locator type and property
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the element value
        """

        element = None
        try:
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                element = self.driver.find_element(locator_type, locator_properties)
                self.log.info(
                    "Element found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error(
                    "Element not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during element identification.")
        return element

    def get_element_list(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to get the element list according to the locator type and property
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the element values as a list
        """

        element = None
        try:
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                element = self.driver.find_elements(locator_type, locator_properties)
                self.log.info(
                    "Elements found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error(
                    "Elements not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during getting elements.")
        return element

    def get_text_from_element(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to get the element's inner text value according to the locator type and property
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the element inner text value
        """

        result_text = ""
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            result_text = element.text
            if len(result_text) == 0:
                result_text = element.get_attribute("innerText")
            elif len(result_text) != 0:
                self.log.info("The text is: '" + result_text + "'")
                result_text = result_text.strip()
        except:
            self.log.error("Exception occurred during text retrieval.")
            print_stack()
        return result_text

    def get_attribute_value_from_element(self, attribute_name, locator_properties, locator_type="xpath",
                                         max_time_out=10):

        """
        This method is used to get the element's attribute value according to the locator type and property
        :param attribute_name: it takes the attribute name as parameter
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns the element attribute value
        """

        attribute_value = ""
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            attribute_value = element.get_attribute(attribute_name)
            if attribute_value is not None:
                self.log.info(attribute_name.upper() + " value is: " + attribute_value)
            else:
                self.log.error(attribute_name.upper() + " value is empty.")
        except:
            self.log.error("Exception occurred during attribute value retrieval.")
        return attribute_value

    def mouse_click_action(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to perform mouse click action according to the locator type and property
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns nothing
        """

        try:
            if self.is_element_clickable(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                element.click()
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error("Unable to click on the element with locator_properties: "
                               + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during mouse click action.")

    def scroll_into_element(self, locator_properties, locator_type="xpath", max_time_out=10):
        """
        This method is used to scroll to invisible element in a dropdown
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns nothing
        """

        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                self.log.info("Clicked on the element with locator_properties: " + locator_properties +
                              " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during scrolling to element.")

    def mouse_click_action_on_element_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        """
        This method is used to perform mouse click action according to the locator type and property
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns nothing
        """

        try:
            if self.is_element_present(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                element.click()
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error("Unable to click on the element with locator_properties: "
                               + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during mouse click action.")

    def move_to_element_and_click(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used when element is not receiving the direct click
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns nothing
        """

        try:
            if self.is_element_clickable(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error("Unable to click on the element with locator_properties: "
                               + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during mouse click action.")

    def enter_text_action(self, text_value, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used to enter the value in text input field
        :param text_value: it takes input string as parameter
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it returns nothing
        :return:
        """

        element = None

        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            element.clear()
            element.send_keys(text_value)
            self.log.info(
                "Sent data to the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Unable to send data on the element with locator_properties: "
                           + locator_properties + " and locator_type: " + locator_type)

        return element

    def verify_text_contains(self, actual_text, expected_text):

        """
        This method verifies that actual text in the expected string 
        :param actual_text: it takes actual keyword/ substring
        :param expected_text: it takes the string value to search actual keyword in it
        :return: it return boolean value according to verification
        """

        if expected_text.lower() in actual_text.lower():
            self.log.info("### TEXT CONTAINS VERIFICATION PASSED !!!")
            return True
        else:
            self.log.error("### TEXT VERIFICATION FAILED:\nActual Text --> {}\nExpected Text --> {}"
                           .format(actual_text, expected_text))
            return False

    def verify_text_match(self, actual_text, expected_text):

        """
        This method verifies the exact match of actual text and expected text
        :param actual_text: it takes actual string value
        :param expected_text: it takes the expected string value to match with
        :return: it return boolean value according to verification
        """

        if expected_text.lower() == actual_text.lower():
            self.log.info("### TEXT VERIFICATION PASSED !!!")
            return True
        else:
            self.log.error("### TEXT VERIFICATION FAILED:\nActual Text --> {}\nExpected Text --> {}"
                           .format(actual_text, expected_text))
            return False

    def take_screenshots(self, file_name_initials):

        """
        This method takes screen shot for reporting
        :param file_name_initials: it takes the initials for file name
        :return: it returns the destination directory of screenshot
        """

        file_name = file_name_initials + "." + str(round(time.time() * 1000)) + ".png"
        cur_path = os.path.abspath(os.path.dirname(__file__))
        screenshot_directory = os.path.join(cur_path, r"../Logs/Screenshots/")

        destination_directory = os.path.join(screenshot_directory, file_name)

        try:
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)
            self.driver.save_screenshot(destination_directory)
            self.log.info("Screenshot saved to directory: " + destination_directory)
        except Exception as ex:
            self.log.error("### Exception occurred:: ", ex)
            print_stack()

        return destination_directory

    def page_scrolling(self, direction="up"):

        """
        This methos is used for page scrolling
        :param direction: it takes the scrolling direction value as parameter
        :return: it returns nothing
        """

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_to_created_object_frame(self, locator_properties, locator_type="xpath", max_time_out=10):

        """
        This method is used for switching to the frame where element is located
        :param locator_properties: it takes locator string as parameter
        :param locator_type: it takes locator type as parameter
        :param max_time_out: this is the maximum time to wait for particular element
        :return: it return nothing
        """

        try:
            frames = self.get_element_list("//iframe")
            for frame in frames:
                frame_name = frame.get_attribute('name')
                if frame_name is not None:
                    self.driver.switch_to.frame(frame_name)
                    result = self.is_element_present(locator_properties, locator_type, max_time_out)
                    if not result:
                        self.driver.switch_to.default_content()
                        continue

                    else:
                        self.log.info("Element found on frame: " + str(frame_name))
                        break
                else:
                    self.driver.switch_to.default_content()
                    continue

        except:
            self.log.error("Element not present on the page.")

    def switch_to_default_content(self):

        """
        This function is used to return to the default frame of the page
        :return: it returns nothing
        """

        try:
            self.driver.switch_to.default_content()
        except:
            self.log.error("Exception occurred while switching to default content..")

    def wait_for_sync(self, seconds=5):
        time.sleep(seconds)

    def press_action_key(self, key=Keys.ENTER):
        actions = ActionChains(self.driver)
        actions.key_down(key).key_up(key).perform()

    def navigate_to_url(self, url, element):
        """
        This function is used to navigate to specific url
        :return: it returns boolean value for successful navigation based on page title
        """

        flag = False
        try:
            self.driver.get(url)
            if self.is_element_displayed(element):
                flag = True
        except:
            flag = False
            self.log.error("Exception occurred while navigating to the url.")

        return flag

    @staticmethod
    def string_generator(string_size=8, chars=string.ascii_uppercase + string.digits):
        """
        This function is used to generate random string
        :return: it returns random string
        """
        return ''.join(random.choice(chars) for _ in range(string_size))

    @staticmethod
    def digit_generator(string_size=10, chars=string.digits):
        """
        This function is used to generate random digits
        :return: it returns random string
        """
        return ''.join(random.choice(chars) for _ in range(string_size))
