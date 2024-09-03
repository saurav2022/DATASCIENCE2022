from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")

# Absolute Xpath
# driver.find_element(
#     By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input"
# ).send_keys("shoes")
# driver.find_element(
#     By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button"
# ).click()

# Relative Xpath
# driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("laptop")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()


# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.XPATH, "//a[@target='_blank']").click()

# # OR AND
# driver.find_element(
#     By.XPATH, "//input[@id='small-searchterms' or @placeholder='Search store']"
# ).send_keys("Tablet")
# driver.find_element(
#     By.XPATH, "//button[@type='submit' and @class='button-1 search-box-button']"
# ).click()

# Functions - starts-with() and contains()
driver.find_element(By.XPATH, "//input[starts-with(@id, 'small')]").send_keys("Books")
driver.find_element(By.XPATH, "//*[contains(@class, 'search-box-button')]").click()

# text()
driver.find_element(By.XPATH, "//a[text()='nopCommerce']").click()
