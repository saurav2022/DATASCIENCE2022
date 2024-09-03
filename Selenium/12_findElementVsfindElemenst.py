from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")

# Find a single element
searchBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
searchBox.send_keys("Phones")

# Find all elements and store as a list
footer_hyperlinks = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
for link in footer_hyperlinks:
    print(link.text, " --> ", link.get_attribute("href"))
# How to get the reference URL - TBD

# Location matching no web element
# findElement returns NoSuchElementException if correspodning web element is not found.
# aWebElement = driver.find_element(By.XPATH, "//input[@id='small-umbrella']")
# print(aWebElement.send_keys("rains"))

# find_elements() will not throw any exception if matching web element is not found. It will return a blank list
aListOfWebElements = driver.find_elements(By.XPATH, "//input[@id='small-umbrella']")
print(aListOfWebElements)
