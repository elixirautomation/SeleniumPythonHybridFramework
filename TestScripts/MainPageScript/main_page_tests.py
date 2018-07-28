""" This module contains the all test cases."""

import os
import unittest
import pytest
import allure
from PageObjects.MainPageObjects.main_page import MainPage
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from FrameworkUtilities.data_reader_utility import DataReader


@allure.story('[DEMO] - Automate  the  basic functionality')
@allure.feature('Web App Input Tests')
@pytest.mark.usefixtures("method_level_setup")
class LoginTests(unittest.TestCase):
    """
    This class contains the executable test cases.
    """

    @pytest.fixture(autouse=True)
    def classSetup(self, method_level_setup):
        """
        This method is used for one time setup of test execution process.
        :param method_level_setup:
        :return: it returns nothing
        """

        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(self.cur_path, r"../../TestData/TestData.xlsx")
        self.exc = DataReader(self.path)
        self.main_page = MainPage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)

    @allure.testcase("Verify Main Screen Elements Test")
    def test_verify_main_screen_elements(self):
        """
        This test is validating the main screen elements. (positive scenario)
        :return: return test status
        """

        with allure.step("Verify Main Screen Elements"):
            result = self.main_page.verify_main_screen_elements()
            self.exe_status.mark_final("test_verify_main_screen_elements", result)

    @allure.testcase("Valid User Input Test")
    def test_valid_user_input(self):
        """
        This test is validating the successful user input. (positive scenario)
        :return: return test status
        """

        with allure.step("Verify User Input"):
            result = self.main_page.verify_valid_user_input(self.exc.get_data("test_valid_user_input", "Text_Message"))
            self.exe_status.mark_final("test_valid_user_input", result)

    @allure.testcase("Valid Addition Test")
    def test_valid_addition(self):
        """
        This test is validating the successful addition. (positive scenario)
        :return: return test status
        """

        with allure.step("Verify valid addition functionality"):
            result = self.main_page.verify_addition_functionality(self.exc.get_data("test_valid_addition", "Number_A"),
                                                          self.exc.get_data("test_valid_addition", "Number_B"),
                                                                  self.exc.get_data("test_valid_addition", "Expected"))

            self.exe_status.mark_final("test_valid_addition", result)

    @allure.testcase("Invalid Addition Test")
    def test_invalid_addition(self):
        """
        This test is validating the unsuccessful addition. (negative scenario)
        :return: return test status
        """

        with allure.step("Verify invalid addition functionality"):
            result = self.main_page.verify_addition_functionality(self.exc.get_data("test_invalid_addition", "Number_A"),
                                                          self.exc.get_data("test_invalid_addition", "Number_B"),
                                                                  self.exc.get_data("test_invalid_addition", "Expected"))
            self.exe_status.mark_final("test_invalid_addition", result)
