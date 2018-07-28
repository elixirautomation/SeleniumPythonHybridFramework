import unittest
from TestScripts.MainPageScript.main_page_tests import LoginTests

# Get all tests from classes
loginTests = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

# Create a test suite combining all test cases
regressionTest = unittest.TestSuite(loginTests)

# Test runner
unittest.TextTestRunner(verbosity=2).run(regressionTest)
