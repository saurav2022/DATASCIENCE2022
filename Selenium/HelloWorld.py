from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WEBDRIVER_PATH=r'<Your_webdrivers_path>'
# driver = webdriver.Chrome(WEBDRIVER_PATH)
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")
title = driver.title
print(f"Title of the website is : {title}")

uName = driver.find_element("name", "username")
uName.send_keys("tomsmith")
uPwd = driver.find_element("name", "password")
uPwd.send_keys("SuperSecretPassword!")
uPwd.send_keys(Keys.RETURN)

# driver.quit()
