from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

print(f"Current url : {driver.current_url}")

driver.get("https://reliance.com/")
time.sleep(15)
print(f"Current url : {driver.current_url}")

driver.close()  # It will close the first(parent) browser window.
# driver.quit() # Kill Chrome process i.e. all browser windows will be closed simultaneously.
