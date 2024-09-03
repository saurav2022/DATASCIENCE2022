from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(10)

# #1.  Scroll by number of pixels
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset")
# print(f"I have moved {value} pixels.")

# # 2. Scroll down page till the search element is visible
# denmark_flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Denmark']")
# driver.execute_script("arguments[0].scrollIntoView();", denmark_flag)
# value = driver.execute_script("return window.pageYOffset")
# print(f"Denmark is located {value} pixels down.")

# 3. Scroll down till the end of the page (MOST COMMON)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset")
print(f"End of the current webpage is {value} pixels below the top.")
time.sleep(5)

# 4. Go back to the top
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset")
print(f"Back to top. Moved by {value} pixels.")

time.sleep(15)

driver.quit()
