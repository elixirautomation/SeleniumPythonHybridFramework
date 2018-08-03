import unittest
from TestScripts.MainPageScript.main_page_tests import MainPageTests

# Get all tests from classes
MainPage = unittest.TestLoader().loadTestsFromTestCase(MainPageTests)

# Create a test suite combining all test cases
regressionTest = unittest.TestSuite(MainPage)

# Test runner
unittest.TextTestRunner(verbosity=2).run(regressionTest)
