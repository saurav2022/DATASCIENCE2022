from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://linkedin.com")
print(f"1 --> {driver.title}")

# open new tab
driver.execute_script("window.open('https://twitter.com')")
print(f"{driver.title} --> {driver.current_window_handle}")
print(f"2 --> {driver.title}")
time.sleep(2)
driver.execute_script("window.open('https://www.google.com')")
print(f"2a --> {driver.title}")
print(f"All handles : {driver.window_handles}")

# open new window
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
print(f"{driver.title} --> {driver.current_window_handle}")
print(f"3 --> {driver.title}")
driver.get("http://facebook.com")
print(f"4 --> {driver.title}")
print(f"All handles : {driver.window_handles}")

# driver.quit()
