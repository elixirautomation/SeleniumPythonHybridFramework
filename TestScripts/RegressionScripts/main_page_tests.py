""" This module contains the all test cases."""

import sys
import logging
import unittest
import allure
import pytest
from PageObjects.MainPageObjects.main_page import MainPage
from FrameworkUtilities.execution_status_utility import ExecutionStatus
import FrameworkUtilities.logger_utility as log_utils
from FrameworkUtilities.data_reader_utility import DataReader


@allure.story('[DEMO] - Automate  the  basic functionality')
@allure.feature('Web App Input Tests')
@pytest.mark.usefixtures("before_class")
class MainPageTests(unittest.TestCase):
    """
    This class contains the executable test cases.
    """
    data_reader = DataReader()
    log = log_utils.custom_logger(logging.INFO)

    def setUp(self):
        self.main_page = MainPage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process.
        :return: it returns nothing
        """

        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @allure.testcase("Verify Main Screen Elements Test")
    def test_verify_main_screen_elements(self):
        """
        This test is validating the main screen elements. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Verify Main Screen Elements"):
            result = self.main_page.verify_main_screen_elements()
            self.exe_status.mark_final(test_step=test_name, result=result)

    @allure.testcase("Valid User Input Test")
    def test_valid_user_input(self):
        """
        This test is validating the successful user input. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        user_input = self.data_reader.get_data(test_name, "Text_Message")

        with allure.step("Verify User Input"):
            result = self.main_page.verify_valid_user_input(user_input)
            self.exe_status.mark_final(test_step=test_name, result=result)

    @allure.testcase("Valid Addition Test")
    def test_valid_addition(self):
        """
        This test is validating the successful addition. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        num1 = self.data_reader.get_data(test_name, "Number_A")
        num2 = self.data_reader.get_data(test_name, "Number_B")
        expected_text = self.data_reader.get_data(test_name, "Expected")

        with allure.step("Verify valid addition functionality"):
            result = self.main_page.verify_addition_functionality(num1, num2, expected=expected_text)
            self.exe_status.mark_final(test_step=test_name, result=result)

    @allure.testcase("Invalid Addition Test")
    def test_invalid_addition(self):
        """
        This test is validating the unsuccessful addition. (negative scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        num1 = self.data_reader.get_data(test_name, "Number_A")
        num2 = self.data_reader.get_data(test_name, "Number_B")
        expected_text = self.data_reader.get_data(test_name, "Expected")

        with allure.step("Verify invalid addition functionality"):
            result = self.main_page.verify_addition_functionality(num1, num2, expected=expected_text)
            self.exe_status.mark_final(test_step=test_name, result=result)
