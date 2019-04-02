import unittest
from TestScripts.RegressionScripts.main_page_tests import MainPageTests

# Get all tests from classes
mainPageTests = unittest.TestLoader().loadTestsFromTestCase(MainPageTests)

# Create a test suite combining all test cases
regressionSuite = unittest.TestSuite()
regressionSuite.addTests([mainPageTests])

# Test runner
unittest.TextTestRunner(verbosity=2).run(regressionSuite)
