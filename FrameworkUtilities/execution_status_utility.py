""" This module contains the methods to conclude the execution status. """

import logging

import allure
import pytest

import FrameworkUtilities.logger_utility as log_utils
from SupportLibraries.ui_helpers import UIHelpers


class ExecutionStatus(UIHelpers):
    """ This class contains the methods to conclude the execution status. """

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.result_list = []

    def set_result(self, result, test_name):

        """
        This method is used for setting the execution result.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_name: this parameter takes the execution status description.
        :return: this method returns nothing.
        """

        try:
            if result is not None:

                if result:
                    self.result_list.append("PASS")
                    self.log.info("### STEP SUCCESSFUL :: " + test_name)
                else:
                    image = self.take_screenshots(test_name)
                    error = "### STEP FAILED :: " + test_name
                    self.result_list.append("FAIL")
                    self.log.error(error)
                    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

            else:
                image = self.take_screenshots(test_name)
                error = "### STEP FAILED :: " + test_name
                self.result_list.append("FAIL")
                self.log.error(error)
                allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

        except Exception as ex:
            image = self.take_screenshots(test_name)
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED :: {}".format(ex))
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    def mark(self, test_step, result):

        """
        This method handles intermediate assertions and saves the result for final mark.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_step: it takes the test case name value
        :return: this method returns nothing.
        """

        self.set_result(result=result, test_name=test_step)

    def mark_final(self, result, test_step):
        """
        This method handles final assertion and saves the result for final mark.
        :param test_step: it takes the test case name value
        :param result: this parameter takes the execution status value pass/fail.
        :return: this method returns nothing.
        """

        self.set_result(result, test_step)

        # noinspection PyBroadException
        try:
            if "FAIL" in self.result_list:
                self.result_list.clear()
                assert True is False

            else:
                self.result_list.clear()
                assert True is True, "### TEST SUCCESSFUL :: " + test_step

        except Exception:
            pytest.fail("### TEST FAILED :: " + test_step, pytrace=False)
