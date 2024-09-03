from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Implicit Wait
driver.implicitly_wait(15)

driver.get("https://www.google.com")
# time.sleep(5)
searchBox = driver.find_element(By.NAME, "q")
searchBox.send_keys("Selenium")

searchBox.submit()
