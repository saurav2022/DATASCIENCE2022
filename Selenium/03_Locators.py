from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# <input
# 		type="text"
# 		class="search-box-text ui-autocomplete-input" id="small-searchterms"
# 		autocomplete="off"
# 		name="q"
# 		placeholder="Search store"
# 		aria-label="Search store">

# Access by id
# driver.find_element(By.ID, "small-searchterms").send_keys("Book")

# # Access by Name
# driver.find_element(By.NAME, "q").send_keys("Electronics")

# Access by class
# driver.find_element(By.CLASS_NAME, "newsletter-subscribe-text").send_keys(
#     "sb@gmail.com"
# )

# # Access by Link Text
driver.find_element(By.LINK_TEXT, "nopCommerce").click()

# Access by Partial Link Text
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
