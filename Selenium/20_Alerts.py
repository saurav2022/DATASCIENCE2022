from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(2)
alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("Saurav")
time.sleep(2)
alertWindow.accept()
# alertWindow.dismiss()

# HW : https://mypage.rediff.com/login/dologin
