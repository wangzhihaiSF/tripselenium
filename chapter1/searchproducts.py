from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# create a new Firefox session
driver = webdriver.Chrome()

# navigate to the application home page
driver.get('https://www.baidu.com/')

# get the search textbox
input = driver.find_element_by_id("kw")
input.clear()

# enter search keyword and submit
try:
    input.send_keys('Python' + Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_all_elements_located(By.ID, "content_left"))
    print(driver.current_url)
    print(driver.get_cookies())
    print(driver.page_source)
except:
    print("something wrong")
driver.close()


