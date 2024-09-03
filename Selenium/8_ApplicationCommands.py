from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.orangehrm.com/en/book-a-free-demo/")
print(driver.title)
print("\n" * 5)
print(driver.current_url)
print("\n" * 5)
print(driver.page_source)
driver.quit()
