# Customised Locators
# 	CSS Selectors
# 		Tag & ID
# 		Tag & Class
# 		Tag & Attribute
# 		Tag, Class & Attribute
# 	XPath

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
driver.maximize_window()

# Tag & Id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(
#     "justin.trudeau@gmail.com"
# )
driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("MyVeryStrongPwd")

# Tag & Class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Gabriel Attal")
# driver.find_element(By.CSS_SELECTOR, "input._55r1").send_keys("Pedro Sanchez")

# Tag & Attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid = 'royal_email']").send_keys(
#     "Alexander De Croo"
# )
# driver.find_element(
#     By.CSS_SELECTOR, "input[placeholder = 'Email address or phone number']"
# ).send_keys("Narendra Modi")

# Tag, Class and Attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[autofocus='1']").send_keys(
    "Mette Frederiksen"
)
