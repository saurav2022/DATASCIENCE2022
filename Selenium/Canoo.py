from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)
# driver.get("https://investors.canoo.com/company-information/faq")

# # Handling the cookies notifications  //*[@id="onetrust-accept-btn-handler"]
# driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

# # Scrapping all the questions and answers
# questions = driver.find_elements(By.XPATH, "//dt[@class='question']")

# answers = driver.find_elements(By.XPATH, "//dt[@class='question']/parent::dl//dd")

# qa = {}

# for qi in range(len(questions)):
#     qa[questions[qi].text] = answers[qi].text

# for k in qa.keys():
#     print(k)
#     print()
#     print(qa[k])
#     print("\n" * 5)


driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, '//*[@id="monday"]').click()
