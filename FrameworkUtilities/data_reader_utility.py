""" This module is used for developing/ accessing data reader utility. """

import os
import traceback
import pyexcel as exc


class DataReader:
    """
    This class includes basic reusable data helpers.
    """

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.file_path = os.path.join(self.cur_path, r"../TestData/TestData.xlsx")

    def load_excel_data(self):
        """
        This methods is used for loading excel file data
        :return: it returns excel records
        """
        records = None

        # noinspection PyBroadException

        try:
            if self.file_path is not None:
                records = exc.iget_records(file_name=self.file_path)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def get_data(self, tc_name, column_name):
        """
        This method is used for returning column data specific to test case name
        :param tc_name: it takes test case name as input parameter
        :param column_name: it takes the name of the column for which value has to be returned
        :return:
        """
        value = None
        excel_records = self.load_excel_data()

        # noinspection PyBroadException

        try:
            if excel_records is not None:
                for record in excel_records:
                    if record['TC_Name'] == tc_name:
                        value = record[column_name]
                        break
                    else:
                        continue

        except Exception as ex:
            traceback.print_exc(ex)

        return value



