""" This module contains the all test cases."""

import sys
import time
import allure
import pytest
from FrameworkUtilities.data_reader_utility import DataReader
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from PageObjects.MainPageObjects.main_page import MainPage
from SupportLibraries.ui_helpers import UIHelpers

data_reader = DataReader()


@allure.story('[DEMO] - Automate  the  basic functionality')
@allure.feature('Web App Input Tests')
@pytest.mark.usefixtures("get_driver", "initialize")
class TestMainPage:
    """
    This class contains the executable test cases.
    """

    @pytest.fixture(scope='function')
    def initialize(self, rp_logger):
        self.main_page = MainPage(self.driver)
        self.exe_status = ExecutionStatus(self.driver)
        self.ui_helpers = UIHelpers(self.driver)

        def cleanup():
            image = self.ui_helpers.take_screenshots(file_name_initials="report_portal")
            with open(image, "rb") as image_file:
                file_data = image_file.read()
            rp_logger.info("Screenshots", attachment={"name": "report_portal" + "." + str(round(time.time() * 1000)) + ".png",
                                           "data": file_data,
                                           "mime": "image/png"})
            self.driver.delete_all_cookies()
            rp_logger.info('Cleaning cookies.')

        yield
        cleanup()

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process.
        :return: it returns nothing
        """
        test_name = request.function.__name__
        if data_reader.get_data(test_name, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @pytest.mark.smoke
    @allure.testcase("Verify Main Screen Elements Test")
    def test_verify_main_screen_elements(self, rp_logger):
        """
        This test is validating the main screen elements. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("Verify Main Screen Elements"):
            result = self.main_page.verify_main_screen_elements()
            self.exe_status.mark_final(test_step=test_name, result=result, logger=rp_logger)

    @pytest.mark.regression
    @allure.testcase("Valid User Input Test")
    def test_valid_user_input(self, rp_logger):
        """
        This test is validating the successful user input. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        user_input = data_reader.get_data(test_name, "Text_Message")

        with allure.step("Verify User Input"):
            result = self.main_page.verify_valid_user_input(user_input)
            self.exe_status.mark_final(test_step=test_name, result=result, logger=rp_logger)

    @pytest.mark.smoke
    @allure.testcase("Valid Addition Test")
    def test_valid_addition(self, rp_logger):
        """
        This test is validating the successful addition. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        num1 = data_reader.get_data(test_name, "Number_A")
        num2 = data_reader.get_data(test_name, "Number_B")
        expected_text = data_reader.get_data(test_name, "Expected")

        with allure.step("Verify valid addition functionality"):
            result = self.main_page.verify_addition_functionality(num1, num2, expected=expected_text)
            self.exe_status.mark_final(test_step=test_name, result=result, logger=rp_logger)

    @pytest.mark.regression
    @allure.testcase("Invalid Addition Test")
    def test_invalid_addition(self, rp_logger):
        """
        This test is validating the unsuccessful addition. (negative scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        num1 = data_reader.get_data(test_name, "Number_A")
        num2 = data_reader.get_data(test_name, "Number_B")
        expected_text = data_reader.get_data(test_name, "Expected")

        with allure.step("Verify invalid addition functionality"):
            result = self.main_page.verify_addition_functionality(num1, num2, expected=expected_text)
            self.exe_status.mark_final(test_step=test_name, result=result, logger=rp_logger)
