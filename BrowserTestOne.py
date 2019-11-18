from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#   driver=webdriver.Firefox(executable_path='/home/atul/Downloads/geckodriver-v0.26.0-linux64/geckodriver.exe')

driver.get("https://www.in.locanto.asia/my/login")
applicationTitle=driver.title

print("\n"+applicationTitle)

driver.find_element_by_name("email").send_keys("davidbird186@gmail.com")
driver.find_element_by_name("pwd").send_keys("Fuck@123#")
driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/form/div/div[3]/button').click()

time.sleep(5)

#str1="atul"
#print(str1)

driver.close()