from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.amazon.com")
driver.get("https://www.snapdeal.com")

time.sleep(3)
driver.back()

time.sleep(3)
driver.forward()

time.sleep(3)
driver.refresh()

time.sleep(3)
driver.quit()
