"""This module is used for main page objects."""

from SupportLibraries.base_helpers import BaseHelpers


class MainPage(BaseHelpers):
    """This class defines the method and element identifications for main page."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    user_message_input = "//input[@id='user-message']"
    show_message_button = "//button[text()='Show Message']"
    show_message_text = "//div[@id='user-message']//following::span[@id='display']"
    enter_first_value = "//input[@id='sum1']"
    enter_second_value = "//input[@id='sum2']"
    get_total_button = "//button[text()='Get Total']"
    show_total_text = "//span[@id='displayvalue']"

    def verify_main_screen_elements(self):
        """
        This function is used to verify all the elements present on the main screen
        :return: this function returns boolean status of element located
        """

        _xpath_prop = "xpath"
        locator_dict = {self.user_message_input: _xpath_prop, self.show_message_button: _xpath_prop,
                        self.enter_first_value: _xpath_prop, self.enter_second_value: _xpath_prop,
                        self.get_total_button: _xpath_prop}

        result = self.verify_elements_located(locator_dict)

        return result

    def verify_valid_user_input(self, user_input):
        """
        This function is used to verify user input and show message on the main screen
        :param user_input: it takes message input as test parameter
        :return: return boolean value based on show message text
        """

        self.enter_text_action(user_input, self.user_message_input)
        self.mouse_click_action(self.show_message_button)
        message = self.get_text_from_element(self.show_message_text)

        result = self.verify_text_match(message, user_input)

        return result

    def verify_addition_functionality(self, num1, num2, expected):
        """
        This function is used to verify addition functionality
        :param expected: expected value
        :param num1: it takes number A input as test parameter
        :param num2: it takes number B input as test parameter
        :return: returns boolean va;ue based on addition result
        """

        self.enter_text_action(num1, self.enter_first_value)
        self.enter_text_action(num2, self.enter_second_value)
        self.mouse_click_action(self.get_total_button)
        addition = str(self.get_text_from_element(self.show_total_text))
        expected = str(expected)

        result = self.verify_text_match(addition, expected)

        return result
