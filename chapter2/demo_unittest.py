import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.jd.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_css_selector("#key")
        self.search_field.clear()
        # enter the search keyword and submit
        self.search_field.send_keys("手机" + Keys.ENTER)

        # get all the anchor elements which have product names
        # display currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//*[@id='J_goodsList']/ul/li[3]/div/div[4]/a/em")
        self.assertEqual(1, len(products))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_class_name("text")
        self.search_field.clear()
        self.search_field.send_keys("python" + Keys.ENTER)
        products = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)