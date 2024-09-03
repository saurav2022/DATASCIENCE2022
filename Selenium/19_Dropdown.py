from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

# drpCountryEle = driver.find_element(By.XPATH, "//select[@id='country']")
# drpCountry = Select(drpCountryEle)

drpCountry = Select(driver.find_element(By.XPATH, "//select[@id='country']"))

# Select value from dropdown
# drpCountry.select_by_visible_text("Australia")
# time.sleep(2)
# drpCountry.select_by_value("usa")
# time.sleep(2)
# drpCountry.select_by_index(3)


# Extract all dropdown values
allOptions = drpCountry.options
print(f"Total number of options : {len(allOptions)}")

for option in allOptions:
    print(option.text)
