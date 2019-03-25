from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys

element_list = []

browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_name("q")
input_third = browser.find_element_by_css_selector("#q")
input_fourth = browser.find_element_by_xpath("//*[@id='q']")

element_list.append(input_first)
element_list.append(input_second)
element_list.append(input_third)
element_list.append(input_fourth)

for i in element_list:
    print(i)

input_first.send_keys("华为手机")
wait1 = wait.WebDriverWait(browser, 5)
input_first.clear()
input_first.send_keys("华为手表" + Keys.ENTER)

wait = wait.WebDriverWait(browser, 5)
browser.close()