""" This module contains the methods to conclude the execution status. """

import logging
from traceback import print_stack
from SupportLibraries.ui_helpers import UIHelpers
import FrameworkUtilities.logger_utility as log_utils
import allure


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
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + test_name)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + test_name)
                    allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)

            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + test_name)
                allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)
        except Exception as ex:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED :: ", ex)
            allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)
            print_stack()

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

        if "FAIL" in self.result_list:
            self.log.error("### " + test_step + " ### TEST FAILED")
            self.result_list.clear()
            assert True is False, "### " + test_step + " ### TEST FAILED"

        else:
            self.log.info("### " + test_step + "### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True is True, "### " + test_step + "### TEST SUCCESSFUL"
