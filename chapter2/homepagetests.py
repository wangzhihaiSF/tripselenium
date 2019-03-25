import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://www.jd.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.ID, "key"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, "language-font"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.find_element_by_css_selector('#settleup-2014 > div.cw-icon > a')
        shopping_cart_icon.click()

        shopping_cart_status = self.driver.find_element_by_css_selector('#container > div:nth-child(1) > div.cart-empty > div > ul > li.txt').text
        self.assertEqual('购物车内暂时没有商品，登录后将显示您之前加入的商品', shopping_cart_status)

        close_button = self.driver.find_element_by_css_selector('#container > div:nth-child(1) > div.cart-empty > div > ul > li:nth-child(2) > a.ftx-05')
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)