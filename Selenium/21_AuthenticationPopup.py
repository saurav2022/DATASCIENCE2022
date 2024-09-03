from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.close()