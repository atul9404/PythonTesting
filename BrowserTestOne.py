from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

#   driver = webdriver.Firefox(GeckoDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())

#   driver=webdriver.Firefox(executable_path='/home/atul/Downloads/geckodriver-v0.26.0-linux64/geckodriver.exe')

driver.get("https://www.in.locanto.asia/my/login")
applicationTitle=driver.title

print("\n"+applicationTitle)

driver.find_element_by_xpath("//input[@name='email']").send_keys("davidbird186@gmail.com")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys("Fuck@123#")

driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(5)

#str1="atul"
#print(str1)

driver.close()