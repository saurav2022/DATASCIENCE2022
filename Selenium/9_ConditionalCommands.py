from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

searchBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print(f"Display status : {searchBox.is_displayed()}")
print(f"Enabled status : {searchBox.is_enabled()}")

# is_selected() : For radio buttons and check boxes
radio_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
radio_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("\nDefault rado button status: ")
print(f"Male Selected status : {radio_male.is_selected()}")
print(f"Female Selected status : {radio_female.is_selected()}")

radio_male.click()
print("\nAfter clicking male radio button: ")
print(f"Male Selected status : {radio_male.is_selected()}")
print(f"Female Selected status : {radio_female.is_selected()}")

time.sleep(2)
radio_female.click()
print("\nAfter clicking female radio button: ")
print(f"Male Selected status : {radio_male.is_selected()}")
print(f"Female Selected status : {radio_female.is_selected()}")
