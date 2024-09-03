from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/input").send_keys("Subir")

driver.switch_to.default_content()  # Go back to the main page
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("abcd@example.com")
