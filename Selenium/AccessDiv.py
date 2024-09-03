from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# WEBDRIVER_PATH=r'<Your_webdrivers_path>'
# driver = webdriver.Chrome(WEBDRIVER_PATH)
driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")


driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div[5]/input",
).click()
