from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")

# 1) Select a specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2) Select all checkboxes
# days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
# # for i in range(len(days)):
# #     days[i].click()

# for day in days:
#     day.click()

# 3) Select multiple custom checkboxes
days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
for i in range(len(days)):
    day = days[i].get_attribute("value")
    if day == "saturday" or day == "wednesday":
        days[i].click()

# for day in days:
#     weekday = day.get_attribute("value")
#     if weekday == "saturday" or weekday == "wednesday":
#         day.click()

# # 4) Select last four checkboxes
# days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
# for i in range(len(days) - 4, len(days)):
#     days[i].click()

# 5) Select first two checkboxes
# days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
# for i in range(0, 2):
#     days[i].click()

# # 6) Select third to fifth checkboxes
# days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
# for i in range(2,5):
#     days[i].click()

time.sleep(5)
# # 4) Clear all checkboxes
# days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
for day in days:
    if day.is_selected():
        day.click()
