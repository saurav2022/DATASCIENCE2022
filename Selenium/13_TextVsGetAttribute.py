from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://admin-demo.nopcommerce.com/login")

emailBox = driver.find_element(By.XPATH, "//input[@id='Email']")
emailBox.clear()
emailBox.send_keys("john.doe@xmail.com")
print(f"Result of text : {emailBox.text}")
print(f"Result of get_attribute : {emailBox.get_attribute('value')}")

sbmt = driver.find_element(By.XPATH, "//button[@type='submit']")
print(f"Result of text : {sbmt.text}")
print(f"Result of get_attribute('type') : {sbmt.get_attribute('type')}")
print(f"Result of get_attribute('value') : {sbmt.get_attribute('value')}")
