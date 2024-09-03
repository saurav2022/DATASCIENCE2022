from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-shooting-star.com/my-travels/")
driver.maximize_window()

locations = driver.find_elements(By.CSS_SELECTOR, "span.kt-btn-inner-text")
print(locations)
print(f"Total locations mentioned : {len(locations)}")
for location in locations:
    print(location.text)

driver.quit()
