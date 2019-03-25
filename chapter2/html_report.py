import unittest
from chapter2 import HTMLTestRunner
import os
from chapter2.demo_unittest import SearchTests
from chapter2.homepagetests import HomePageTest

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(result_dir + '\SmokeTestReport1.html', 'wb')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='Test Report',
                                       description='Smoke Tests')

# run the suite using HTMLTestRunner
runner.run(smoke_tests)