from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
# time.sleep(3)

# Self
# stock_name = driver.find_element(By.XPATH, "//a[contains(text(),'NCC')]/self::a").text
# print(stock_name)

# Parent
# stock_name = driver.find_element(
#     By.XPATH, "//a[contains(text(),'Thermax')]/parent::td"
# ).text
# print(stock_name)

# Ancestor, Child
# stock_row = driver.find_elements(
#     By.XPATH, "//a[contains(text(),'Thermax')]/ancestor::tr/child::td"
# )
# print(stock_row)
# print(f"Total number of elements in a row : {len(stock_row)}")

# Ancestor
# stock_row = driver.find_element(
#     By.XPATH, "//a[contains(text(),'Thermax')]/ancestor::tr"
# ).text
# print(stock_row)

driver.get("https://the-internet.herokuapp.com/tables")

# Descendants
# descendants = driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::tr")
# print(f"Total number of descendant rows : {len(descendants)}")


# following
# followers = driver.find_elements(
#     By.XPATH, "//table[@id='table1']//tr[3]/td[2]/following::td"
# )
# print(f"Total number of following cells : {len(followers)}")

# following-sibling
# follower_sibling = driver.find_elements(
#     By.XPATH, "//table[@id='table1']//tr[3]/td[2]/following-sibling::td"
# )
# print(f"Total number of following cells in the same row : {len(follower_sibling)}")

# preceding
predecessors = driver.find_elements(
    By.XPATH, "//table[@id='table1']//tr[3]/td[2]/preceding::td"
)
print(f"Total number of preceding cells : {len(predecessors)}")

# preceding-sibling
predecessor_sibling = driver.find_elements(
    By.XPATH, "//table[@id='table1']//tr[3]/td[2]/preceding-sibling::td"
)
print(f"Total number of preceding cells in the same row : {len(predecessor_sibling)}")

driver.close()
