import unittest


# get all tests from SearchProductTest and HomePageTest class
from chapter2.demo_unittest import SearchTests
from chapter2.homepagetests import HomePageTest

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)